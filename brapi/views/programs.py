from rest_framework.views import APIView
import logging

from brapi.models import Program
from brapi.serializers import ProgramSerializer
from brapi.aux_fun import search_get_qparams, search_post_params_in, paginate


class ProgramView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Program.objects.all()
        queryset = search_get_qparams(self, queryset, [('programName', 'programName'), ('abbreviation', 'abbreviation')])

        return paginate(queryset, request, ProgramSerializer)

    # end def get

# end class ProgramView


class ProgramSearchView(APIView):

    # def get(self, request, format=None, *args, **kwargs):
    #
    #     queryset = Program.objects.all()
    #
    #     queryset = search_get_qparams(self, queryset, [
    #         ('programDbId', 'programDbId'),
    #         ('name', 'name'),
    #         ('abbreviation', 'abbreviation'),
    #         ('objective', 'objective'),
    #         ('leadPerson', 'leadPerson')
    #     ])
    #
    #     return paginate(queryset, request, ProgramSerializer)
    #
    # # end def get


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
