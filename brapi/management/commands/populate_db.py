from django.core.management.base import BaseCommand, CommandError

from brapi.models.call import Call
from brapi.models.location import Location
from brapi.models.program import Program
from brapi.models.crop import Crop
from brapi.models.map import Map, MapLinkage
from brapi.models.marker import Marker
from brapi.models.trait import Trait
from brapi.models.germplasm_attributes import GAList, GAAttrAvail, GermplasmAttr
from brapi.models.taxon import Taxon
from brapi.models.germplasm import Germplasm, GPPedigree, GPDonor, GPMarkerP
from brapi.models.study import (Study, Trial, DataLink, StudyObsUnit, Treatment,
                                StudySeason, StudyType, StudyObsLevel, StudyPlot)
from brapi.models.sample import Sample
from brapi.models.observation import (Observation, ObservationUnitXref, Ontology, 
                                      Datatype, ObsVValue, ObsScale, ObsTrait, 
                                      ObsMethod, ObsVariable)
from brapi.models.phenotype import Phenotype
from brapi.models.markerprofile import (AlleleMatrix, AlleleMSearch, MarkerProfile,
                                        MarkerProfilesData)


class Command(BaseCommand):
    
    help = 'Populate the DB starting from a (well-formed) TSV file'

    def add_arguments(self, parser):

        parser.add_argument('TSV_dir')
    
    # end def add_arguments


    def _populate_table(self, filename, Classname, composite_fields=[]):

        with open(filename) as fp:
            for (i, line) in enumerate(fp):
                if i > 0:
                    fields = line.rstrip().split('\t')
                    for f in range(len(fields)):
                        if fields[f] == '' or 'NULL' in fields[f]:
                            fields[f] = None
                        # end if
                    # end for
                    for f in composite_fields:
                        fields[f] = fields[f].split('; ')
                    # end for
                    row = Classname(None, *fields)
                    print('INSERT: %s(None, %s)' % (Classname.__name__, fields))
                    row.save()
                # end if
            # end for
        # end with

        self.stdout.write(self.style.SUCCESS('Successfully populated table "%s"' % Classname.__name__))

    # end def _populate_table


    def handle(self, *args, **options):
       
        tsv = options['TSV_dir']

#        self._populate_table(tsv + '/calls.tsv', Call, [1, 2])
#        self._populate_table(tsv + '/crops.tsv', Crop)
#        self._populate_table(tsv + '/programs.tsv', Program)
#
#        self._populate_table(tsv + '/mapsLinkages.tsv', MapLinkage)
#        self._populate_table(tsv + '/maps.tsv', Map)
#
#        self._populate_table(tsv + '/locations.tsv', Location)
#
#        self._populate_table(tsv + '/markers.tsv', Marker, [3, 4, 5])
#        self._populate_table(tsv + '/traits.tsv', Trait, [4])
#
#        self._populate_table(tsv + '/germplasm_attributes_list.tsv', GAList)
#        self._populate_table(tsv + '/germplasm_attributes_avail.tsv', GAAttrAvail, [6])
#        self._populate_table(tsv + '/germplasm_attributes.tsv', GermplasmAttr)
        
#        self._populate_table(tsv + '/taxon.tsv', Taxon)
#        self._populate_table(tsv + '/germplasm.tsv', Germplasm, [7, 13, 19])
#        self._populate_table(tsv + '/germplasm_pedigrees.tsv', GPPedigree)
#        self._populate_table(tsv + '/germplasm_donors.tsv', GPDonor)
#
#        self._populate_table(tsv + '/markerprofiles.tsv', MarkerProfile)
#        self._populate_table(tsv + '/germplasm_markerprofiles.tsv', GPMarkerP)
#
#        self._populate_table(tsv + '/datalinks.tsv', DataLink) 
#        self._populate_table(tsv + '/studies.tsv', Study, [14]) 
#        self._populate_table(tsv + '/trials.tsv', Trial)
#
#        self._populate_table(tsv + '/samples.tsv', Sample)
#
#        self._populate_table(tsv + '/observations.tsv', Observation)

        # this cannot be standardized because of the (original) field named 'id'
#        with open(tsv + '/observationUnitXrefs.tsv') as fp:
#            for (i, line) in enumerate(fp):
#                if i > 0:
#                    fields = line.rstrip().split('	')
#                    row = ObservationUnitXref(*fields)
#                    row.save()
#                # end if
#            # end for
#        # end with
#        self.stdout.write(self.style.SUCCESS('Successfully populated table "ObservationUnitXref"'))
#
#        self._populate_table(tsv + '/treatments.tsv', Treatment)
#        self._populate_table(tsv + '/phenotypes.tsv', Phenotype)
#
#        self._populate_table(tsv + '/variables_datatypes.tsv', Datatype)
#        self._populate_table(tsv + '/variables_ontologies.tsv', Ontology)
#
#        self._populate_table(tsv + '/study_seasons.tsv', StudySeason)
#        self._populate_table(tsv + '/study_types.tsv', StudyType)
#        self._populate_table(tsv + '/study_obs_levels.tsv', StudyObsLevel)
#        self._populate_table(tsv + '/study_plot_layouts.tsv', StudyPlot)
#
#        self._populate_table(tsv + '/allele_matrices.tsv', AlleleMatrix)
#        self._populate_table(tsv + '/allele_matrix.tsv', AlleleMSearch, [0])
#        self._populate_table(tsv + '/markerprofiles_data.tsv', MarkerProfilesData, [5])
#
        self._populate_table(tsv + '/obs_vvalues.tsv', ObsVValue, [1])
#        self._populate_table(tsv + '/obs_scales.tsv', ObsScale)
#        self._populate_table(tsv + '/obs_traits.tsv', ObsTrait)
#        self._populate_table(tsv + '/obs_methods.tsv', ObsMethod)
#        self._populate_table(tsv + '/obs_variables.tsv', ObsVariable)
        
#        self._populate_table(tsv + '/study_obs_units.tsv', StudyObsUnit)

    # end def handle

# end class Command
