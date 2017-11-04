
from django.core.management.base import BaseCommand, CommandError

from brapi.models import (Call, Location, Program, Crop, Map, MapLinkage, Marker, Trait,
    GAList, GAAttrAvail, GermplasmAttr, Germplasm, GPPedigree, GPDonor, GPMarkerP, MarkerProfile,
    Study, Trial, Sample, Observation, ObservationUnitXref, Treatment, Phenotype, Datatype,
    Ontology, StudySeason, StudyType, StudyObsLevel, StudyPlot, AlleleMatrix, AlleleMSearch,
    MarkerProfilesData)


class Command(BaseCommand):
    
    help = 'Print creation calls for test DBs'

    def add_arguments(self, parser):

        parser.add_argument('TSV_file')
        parser.add_argument('class')
    
    # end def add_arguments


    def handle(self, *args, **options):
       
        tsv_file = options['TSV_file']
        classname = options['class']
        first_row = []
        second_row = []

        headers = []
        with open(tsv_file) as fp:
            for (i, line) in enumerate(fp):
                if i == 0:
                    headers = line.rstrip().split('\t')                    
                elif i < 3:
                    fields = line.rstrip().split('\t')
                    for (j, field) in enumerate(fields):
                        if ';' in field:
                            fields[j] = ['%s' % f for f in field.split('; ')]
                        # end if
                    # end for
                    if i == 1:
                        first_row = fields
                    elif i == 2:
                        second_row = fields
                    # end if
                else:
                    break
                # end if
            # end for
            f1 = []
            f2 = []
            for (i, h) in enumerate(headers):
                try:
                    f1.append("%s='%s'" % (h, first_row[i]))
                except IndexError:
                    pass
                # end try
                try:
                    f2.append("%s='%s'" % (h, second_row[i]))
                except IndexError:
                    pass
                # end try
            # end for
            print('%s.objects.create(%s)' % (classname, ', '.join(f1)))
            print('%s.objects.create(%s)' % (classname, ', '.join(f2)))
        # end with

    # end def handle

# end class Command
