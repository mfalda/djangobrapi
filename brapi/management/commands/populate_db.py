
from django.core.management.base import BaseCommand, CommandError
from brapi.models import Call


class Command(BaseCommand):
    
    help = 'Populate the DB starting from a (well-formed) TSV file'

    def add_arguments(self, parser):

        parser.add_argument('TSV_source')
    
    # end def add_arguments


    def handle(self, *args, **options):
       
        tsv = options['TSV_source']

        with open(tsv) as fp:
            for (i, line) in enumerate(fp):
                if i > 0:
                    fields = line.rstrip().split('\t')
                    row = Call(call=fields[0], datatypes=fields[1].split('; '), methods=fields[2].split('; '))
                    row.save()
                # end if
            # end for
        # end with

        self.stdout.write(self.style.SUCCESS('Successfully populated'))

    # end def handle

# end class Command
