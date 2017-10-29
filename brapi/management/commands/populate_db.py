
from django.core.management.base import BaseCommand, CommandError

from brapi.models import Call, Location, Program, Crop, Map, MapLinkage, Marker, Trait


class Command(BaseCommand):
    
    help = 'Populate the DB starting from a (well-formed) TSV file'

    def add_arguments(self, parser):

        parser.add_argument('TSV_dir')
    
    # end def add_arguments


    def _populate_table(self, filename, classname):

        with open(filename) as fp:
            for (i, line) in enumerate(fp):
                if i > 0:
                    fields = line.rstrip().split('\t')
                    row = eval('%s(None, *fields)' % classname)
                    row.save()
                # end if
            # end for
        # end with

        self.stdout.write(self.style.SUCCESS('Successfully populated table "%s"' % classname))

    # end def _populate_table


    def handle(self, *args, **options):
       
        tsv = options['TSV_dir']

        # this cannot be generalized into a function because of semi-colons
        # with open(tsv + '/calls.tsv') as fp:
        #     for (i, line) in enumerate(fp):
        #         if i > 0:
        #             fields = line.rstrip().split('\t')
        #             row = Call(call=fields[0], datatypes=fields[1].split('; '),
        #                           methods=fields[2].split('; '))
        #             row.save()
        #         # end if
        #     # end for
        # # end with

        # self.stdout.write(self.style.SUCCESS('Successfully populated table "Calls"'))

        #self._populate_table(tsv + '/crops.tsv', 'Crop')
        #self._populate_table(tsv + '/programs.tsv', 'Program')
        #self._populate_table(tsv + '/mapsLinkages.tsv', 'MapLinkage')
        #self._populate_table(tsv + '/maps.tsv', 'Map')
        #self._populate_table(tsv + '/locations.tsv', 'Location')

        # this cannot be generalized into a function because of semi-colons
        # with open(tsv + '/markers.tsv') as fp:
        #     for (i, line) in enumerate(fp):
        #         if i > 0:
        #             fields = line.rstrip().split('\t')
        #             row = Marker(markerDbId=fields[0], defaultDisplayName=fields[1], type=fields[2],
        #                 synonyms=fields[3].split('; '), refAlt=fields[4].split('; '), 
        #                 analysisMethods=fields[5].split('; '))
        #             row.save()
        #         # end if
        #     # end for
        # # end with


        # this cannot be generalized into a function because of semi-colons
        with open(tsv + '/traits.tsv') as fp:
            for (i, line) in enumerate(fp):
                if i > 0:
                    fields = line.rstrip().split('\t')
                    row = Trait(traitDbId=fields[0], traitId=fields[1], name=fields[2],
                        description=fields[3], observationVariables=fields[4].split('; '), 
                        defaultValue=fields[5])
                    row.save()
                # end if
            # end for
        # end with

    # end def handle

# end class Command
