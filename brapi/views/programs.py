from rest_framework import viewsets

from brapi.models.program import Program, ProgramSerializer

from brapi.aux_fun import _search_get_qparams


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProgramSerializer

    def get_queryset(self):

        queryset = Program.objects.all()

        return _search_get_qparams(self, queryset, [('programName', 'programName'), ('abbreviation', 'abbreviation')])

    # end def get_queryset

# end class ProgramViewSet
