from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
import logging
import datetime

from brapi.models import Phenotype, Observation
from brapi.serializers import PhenotypeSerializer
from brapi.aux_fun import search_post_params_in, paginate


class PhenotypeSearchView(APIView):

    def post(self, request, format=None, *args, **kwargs):

        queryset = Phenotype.objects.all()

        # PARAMS:
        # {
        #     "germplasmDbIds" : [ "Blabla", "34Mtp362" ], // (optional, text, `986`) ... The name or synonym of external genebank accession identifiers
        #     "observationVariableDbIds" : [ "37373", "CO_321:00000234"], // (optional, text, `CO_321:00000234`) ... The IDs of traits, could be ontology ID, database ID or PUI
        #     "studyDbIds" : [ "383", "2929", "WHEAT_NETWK_2016_MONTPELLIER" ], // (optional, text, `2356`) ... The database ID / PK of the studies search parameter
        #     "locationDbIds" : [ "383838", "MONTPELLIER" ], // locations these traits were collected
        #     "programDbIds" : [ "3838", "Drought resistance CG 2020" ], // list of programs that have phenotyped this trait
        #     "seasonDbIds" : [ "338", "2010", "1956-2014", "2002-2003-2004", "2007 Spring" ], // (optional, text, `2001`) ... The year or Phenotyping campaign of a multiannual study (trees, grape, ...)
        #     "observationLevel" : "plot", // (optional, text, `plot`) ... The type of the observationUnit. Returns only the observaton unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
        #     "observationTimeStampRange" : ["2015-06-16T00:53:26-0800","2015-06-18T00:53:26-0800"]
        #     "pageSize" : 100, // (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
        #     "page" : 1, // (optional, integer, `10`) ... Which result page is requested
        # }

        params = self.request.data

        logger = logging.getLogger(__name__)
        logger.warning("Search parameters: %s" % params)

        queryset = search_post_params_in(self, queryset, [
            ('germplasmDbIds', 'germplasmDbId'),
            ('studyDbIds', 'studyDbId'),
            ('locationDbIds', 'locationDbId'),
            ('programDbIds', 'programDbId'),
            ('observationLevels', 'observationLevel')])

        observationVariableDbIds = params.get('observationVariableDbIds', None)
        if observationVariableDbIds is not None:
            obs = Observation.objects.filter(obsVariable__observationVariableDbId__in=observationVariableDbIds).all()
            queryset = queryset.filter(pk=obs)
        # end if

        seasonDbIds = params.get('seasonDbIds', None)
        if seasonDbIds is not None:
            obs = Observation.objects.filter(seasonDbId__in=seasonDbIds).all()
            queryset = queryset.filter(pk=obs)
        # end if

        observationTimeStampRange = params.get('observationTimeStampRange', None)
        if observationTimeStampRange is not None:

            print_date = lambda iso_date: datetime.datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%SZ").strftime('%d %b %Y - %T - %Z')

            logger.warning("Restricting dates to (%s, %s)" % (print_date(observationTimeStampRange[0]), print_date(observationTimeStampRange[1])))

            obs = Observation.objects.filter(Q(observationTimestamp__gte=observationTimeStampRange[0])
                                        &Q(observationTimestamp__lte=observationTimeStampRange[1]))
            queryset = queryset.filter(pk__in=[int(o.observationDbId) for o in obs])
        # end if 

        return paginate(queryset, request, PhenotypeSerializer)        

    # end def post

# end class PhenotypeSearchView
