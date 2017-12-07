from rest_framework import viewsets
from rest_framework.views import APIView
import logging

from brapi.models import Program
from brapi.serializers import ProgramSerializer
from brapi.aux_fun import search_get_qparams, search_post_params_in, paginate


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProgramSerializer

    def get_queryset(self):

        queryset = Program.objects.all()

        return search_get_qparams(self, queryset, [('programName', 'programName'), ('abbreviation', 'abbreviation')])

    # end def get_queryset

# end class ProgramViewSet



class ProgramSearchView(APIView):

    def post(self, request, format=None, *args, **kwargs):

        queryset = Program.objects.all()

        # PARAMS:
        # {
        #     "programDbId": "123",
        #     "name": "Wheat Resistance Program",
        #     "abbreviation" : "DRP1",
        #     "objective" : "Disease resistance",
        #     "leadPerson" : "Dr. Henry Beachell"
        # } 

        params = self.request.data

        logger = logging.getLogger(__name__)
        logger.warning("Search parameters: %s" % params)

        queryset = search_post_params_in(self, queryset, [('programDbId', 'programDbId'), 
            ('name', 'name'), ('abbreviation', 'abbreviation'), 
            ('objective', 'objective'), ('leadPerson', 'leadPerson')], False)

        return paginate(queryset, request, ProgramSerializer)        

    # end def post

# end class ProgramSearchView
