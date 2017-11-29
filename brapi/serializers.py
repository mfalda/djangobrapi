from rest_framework import serializers

from brapi.models import *


class ExtendedSerializer(serializers.ModelSerializer):

    def get_field_names(self, declared_fields, info):
        
        expanded_fields = super(ExtendedSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'excluded', None):
            expanded_fields = set(expanded_fields) - set(self.Meta.excluded)
        # end if
        
        if getattr(self.Meta, 'extra_fields', None):
            return list(expanded_fields) + self.Meta.extra_fields
        else:
            return list(expanded_fields)
        # end if
        
    # end def get_field_names
        
# end class ExtendedSerializer


class ContactSerializer(serializers.ModelSerializer):

    class Meta:

        model = Contact
        excluded = ['cropdbid']

        # end class Meta

# end class ContactSerializer


class CropSerializer(serializers.ModelSerializer):

    class Meta:

        model = Crop
        excluded = ['cropdbid']

        # end class Meta

# end class CropSerializer


class DonorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Donor
        excluded = ['cropdbid']

        # end class Meta

# end class DonorSerializer


class GermplasmSerializer(serializers.ModelSerializer):

    class Meta:

        model = Germplasm
        excluded = ['cropdbid']

        # end class Meta

# end class GermplasmSerializer


class GermplasmAttributeSerializer(serializers.ModelSerializer):

    class Meta:

        model = GermplasmAttribute
        excluded = ['cropdbid']

    # end class Meta

# end class GermplasmAttributeSerializer


class GermplasmAttributeCategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = GermplasmAttributeCategory
        excluded = ['cropdbid']

        # end class Meta

# end class GermplasmAttributeCategorySerializer


class GermplasmAttributeValueSerializer(serializers.ModelSerializer):

    class Meta:

        model = GermplasmAttributeValue
        excluded = ['cropdbid']

        # end class Meta

# end class GermplasmAttributeValueSerializer


class LocationAdditionalInfoSerializer(serializers.ModelSerializer):

    class Meta:

        model = LocationAdditionalInfo
        excluded = ['cropdbid']

    # end class Meta

# end class LocationAdditionalInfoSerializer


class LocationSerializer(serializers.ModelSerializer):

    additionalInfo = LocationAdditionalInfoSerializer(many=False, read_only=True)

    class Meta:

        model = Location
        excluded = ['cropdbid']
        extra_fields = ['additionalInfo']

    # end class Meta

# end class LocationSerializer


class MapSerializer(serializers.ModelSerializer):

    class Meta:

        model = Map
        excluded = ['cropdbid']

        # end class Meta

# end class MapSerializer


class MarkerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Marker
        excluded = ['cropdbid']

        # end class Meta

# end class MarkerSerializer


class MarkerprofileSerializer(serializers.ModelSerializer):

    class Meta:

        model = Markerprofile
        excluded = ['cropdbid']

        # end class Meta
# end class MarkerprofileSerializer


class MethodSerializer(serializers.ModelSerializer):

    class Meta:

        model = Method
        excluded = ['cropdbid']

        # end class Meta

# end class MethodSerializer


class ObservationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Observation
        excluded = ['cropdbid']

        # end class Meta

# end class ObservationSerializer


class ObservationUnitSerializer(serializers.ModelSerializer):

    class Meta:

        model = ObservationUnit
        excluded = ['cropdbid']

        # end class Meta

# end class ObservationUnitSerializer


class ObservationUnitXrefSerializer(serializers.ModelSerializer):

    class Meta:

        model = ObservationUnitXref
        excluded = ['cropdbid']

        # end class Meta

# end class ObservationUnitXrefSerializer


class ObservationVariableSerializer(serializers.ModelSerializer):

    class Meta:

        model = ObservationVariable
        excluded = ['cropdbid']

        # end class Meta

# end class ObservationVariableSerializer


class OntologySerializer(serializers.ModelSerializer):

    class Meta:

        model = Ontology
        excluded = ['cropdbid']

        # end class Meta

# end class OntologySerializer


class PedigreeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pedigree
        excluded = ['cropdbid']

        # end class Meta

# end class PedigreeSerializer


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:

        model = Program
        excluded = ['cropdbid']

        # end class Meta

# end class ProgramSerializer


class SampleSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sample
        excluded = ['cropdbid']

        # end class Meta

# end class SampleSerializer


class ScaleSerializer(serializers.ModelSerializer):

    class Meta:

        model = Scale
        excluded = ['cropdbid']

        # end class Meta

# end class ScaleSerializer


class SeasonSerializer(serializers.ModelSerializer):

    class Meta:

        model = Season
        excluded = ['cropdbid']

        # end class Meta

# end class SeasonSerializer


class StudySerializer(serializers.ModelSerializer):

    class Meta:

        model = Study
        excluded = ['cropdbid']

        # end class Meta

# end class StudySerializer


class StudyAdditionalInfoSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudyAdditionalInfo
        excluded = ['cropdbid']

        # end class Meta

# end class StudyAdditionalInfoSerializer


class StudyContactSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudyContact
        excluded = ['cropdbid']

        # end class Meta

# end class StudyContactSerializer


class StudyDataLinkSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudyDataLink
        excluded = ['cropdbid']

        # end class Meta

# end class StudyDataLinkSerializer


class StudySeasonSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudySeason
        excluded = ['cropdbid']

        # end class Meta

# end class StudySeasonSerializer


class StudyTypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudyType
        excluded = ['cropdbid']

        # end class Meta

# end class StudyTypeSerializer


class TaxonXrefSerializer(serializers.ModelSerializer):

    class Meta:

        model = TaxonXref
        excluded = ['cropdbid']

        # end class Meta

# end class TaxonXrefSerializer


class TaxonXrefGermplasmSerializer(serializers.ModelSerializer):

    class Meta:

        model = TaxonXrefGermplasm
        excluded = ['cropdbid']

        # end class Meta

# end class TaxonXrefGermplasmSerializer


class TraitSerializer(serializers.ModelSerializer):

    class Meta:

        model = Trait
        excluded = ['cropdbid']

        # end class Meta

# end class TraitSerializer


class TreatmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Treatment
        excluded = ['cropdbid']

        # end class Meta

# end class TreatmentSerializer


class TrialSerializer(serializers.ModelSerializer):

    class Meta:

        model = Trial
        excluded = ['cropdbid']

        # end class Meta

# end class TrialSerializer


class TrialAdditionalInfoSerializer(serializers.ModelSerializer):

    class Meta:

        model = TrialAdditionalInfo
        excluded = ['cropdbid']

        # end class Meta

# end class TrialAdditionalInfoSerializer


class TrialContactSerializer(serializers.ModelSerializer):

    class Meta:

        model = TrialContact
        excluded = ['cropdbid']

    # end class Meta

# end class TrialContactSerializer
