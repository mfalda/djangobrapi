from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User

from brapi.models import (Call, Location, Crop, Program, Map, MapLinkage, Marker, Trait, 
    GAList, GAAttrAvail, GermplasmAttr, Germplasm, GPPedigree, GPDonor, GPMarkerP, MarkerProfile,
    Study, Trial, Sample, Observation, ObservationUnitXref, Treatment, Phenotype, Datatype, 
    Ontology, StudySeason, StudyType, StudyObsLevel, StudyPlot, AlleleMatrix, AlleleMSearch,
    MarkerProfilesData, ObsVValue, ObsMethod, ObsScale, ObsTrait, ObsVariable,
    StudyObsUnit, Study)


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )

# end class SocialSerializer


class StringListField(serializers.ListField):

    child = serializers.CharField(max_length=10, default='GET')

 # end class StringListField


class CallsSerializer(serializers.ModelSerializer):

    datatypes = StringListField()
    methods = StringListField()


    class Meta:

        model = Call
        fields = ('call', 'datatypes', 'methods')

    # end class Meta


    def to_representation(self, instance: Call):

        instance.datatypes = [str(s) for s in instance.datatypes.split('; ')]
        instance.methods = [str(s) for s in instance.methods.split('; ')]

        return super(CallsSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(CallsSerializer, self).to_internal_value(data)

        if ret['datatypes']:
            ret['datatypes'] = '; '.join(str(s) for s in ret['datatypes'])
        # end if

        if ret['methods']:
            ret['methods'] = '; '.join(str(s) for s in ret['methods'])
        # end if

        return ret

    # end def to_internal_value

# end class CallsSerializer


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:

        model = Program
        exclude = ['id']

    # end class Meta

# end class ProgramSerializer


class CropSerializer(serializers.ModelSerializer):

    class Meta:

        model = Crop
        fields = ['data']

    # end class Meta

# end class CropSerializer


class MapLinkageSerializer(serializers.ModelSerializer):

    class Meta:

        model = MapLinkage
        exclude = ['id']

    # end class Meta

# end class MapLinkageSerializer


class MapSerializer(serializers.ModelSerializer):

    linkageGroups = MapLinkageSerializer(many=True, read_only=True)

    class Meta:

        model = Map
        fields = ['mapDbId', 'name', 'species', 'type', 'unit', 'publishedDate', 
                    'markerCount', 'comments', 'linkageGroups']

    # end class Meta

# end class MapSerializer


class MapLinkageSerializer(serializers.ModelSerializer):

    class Meta:

        model = MapLinkage
        exclude = ['id']

    # end class Meta

# end class MapLinkageSerializer


class LocationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Location
        exclude = ['id']

    # end class Meta

# end class LocationSerializer


class MarkerSerializer(serializers.ModelSerializer):

    synonyms = StringListField()   
    refAlt = StringListField()   
    analysisMethods = StringListField()   

    class Meta:

        model = Marker
        fields = ('markerDbId', 'defaultDisplayName', 'type', 'synonyms', 'refAlt', 'analysisMethods')

    # end class Meta


    def to_representation(self, instance: Call):

        instance.synonyms = [str(s) for s in instance.synonyms.split('; ')]
        instance.refAlt = [str(s) for s in instance.refAlt.split('; ')]
        instance.analysisMethods = [str(s) for s in instance.analysisMethods.split('; ')]

        return super(MarkerSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(CallsSerializer, self).to_internal_value(data)

        if ret['synonyms']:
            ret['synonyms'] = '; '.join(str(s) for s in ret['synonyms'])
        # end if

        if ret['refAlt']:
            ret['refAlt'] = '; '.join(str(s) for s in ret['refAlt'])
        # end if

        if ret['analysisMethods']:
            ret['analysisMethods'] = '; '.join(str(s) for s in ret['analysisMethods'])
        # end if

        return ret

    # end def to_internal_value

# end class MarkerSerializer


class TraitSerializer(serializers.ModelSerializer):

    observationVariables = StringListField()

    class Meta:

        model = Trait
        fields = ['traitDbId', 'traitId', 'name', 'description', 'observationVariables', 'defaultValue']

    # end class Meta


    def to_representation(self, instance: Call):

        instance.observationVariables = [str(s) for s in instance.observationVariables.split('; ')]

        return super(TraitSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(TraitSerializer, self).to_internal_value(data)

        if ret['observationVariables']:
            ret['observationVariables'] = '; '.join(str(s) for s in ret['observationVariables'])
        # end if

        return ret

    # end def to_internal_value

# end class TraitSerializer


class GAListSerializer(serializers.ModelSerializer):

    class Meta:

        model = GAList
        exclude = ['id']

    # end class Meta

# end class GAListSerializer


class GAAttrAvailSerializer(serializers.ModelSerializer):

    values = StringListField()

    class Meta:

        model = GAAttrAvail
        fields = ['attributeCategoryDbId', 'code', 'uri', 'name', 'description', 'datatype', 'values']

    # end class Meta

    def to_representation(self, instance: Call):

        instance.values = [str(s) for s in instance.values.split('; ')]

        return super(GAAttrAvailSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(GAAttrAvailSerializer, self).to_internal_value(data)

        if ret['values']:
            ret['values'] = '; '.join(str(s) for s in ret['values'])
        # end if

        return ret

    # end def to_internal_value

# end class GAAttrAvailSerializer


class GermplasmAttrSerializer(serializers.ModelSerializer):

    class Meta:

        model = GermplasmAttr
        fields = ['attributeDbId', 'attributeName', 'attributeCode', 'value', 'dateDetermined']

    # end class Meta

# end class GermplasmAttrSerializer


class GermplasmSerializer(serializers.ModelSerializer):

    synonyms = StringListField()
    donors = StringListField()
    typeOfGermplasmStorageCode = StringListField()

    class Meta:

        model = Germplasm
        exclude = ['id']

    # end class Meta


    def to_representation(self, instance: Call):

        instance.synonyms = [str(s) for s in instance.synonyms.split('; ')]
        instance.donors = [str(s) for s in instance.donors.split('; ')]
        instance.typeOfGermplasmStorageCode = [str(s) for s in instance.typeOfGermplasmStorageCode.split('; ')]

        return super(GermplasmSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(GermplasmSerializer, self).to_internal_value(data)

        if ret['synonyms']:
            ret['synonyms'] = '; '.join(str(s) for s in ret['synonyms'])
        # end if

        if ret['donors']:
            ret['donors'] = '; '.join(str(s) for s in ret['donors'])
        # end if

        if ret['typeOfGermplasmStorageCode']:
            ret['typeOfGermplasmStorageCode'] = '; '.join(str(s) for s in ret['typeOfGermplasmStorageCode'])
        # end if
        #         
        return ret

    # end def to_internal_value    

# end class GermplasmSerializer


class GPPedigreeSerializer(serializers.ModelSerializer):

    class Meta:

        model = GPPedigree
        fields = ['germplasmDbId', 'defaultDisplayName', 'pedigree', 'parent1Id', 'parent2Id']

    # end class Meta

# end class GPPedigreeSerializer


class GPDonorSerializer(serializers.ModelSerializer):

    germplasmDbId = GermplasmSerializer(many=True, read_only=True)

    class Meta:

        model = GPDonor
        exclude = ['id']

    # end class Meta

# end class GPDonorSerializer


class MarkerProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = MarkerProfile
        exclude = ['id']

    # end class Meta

# end class MarkerProfileSerializer


class GPMarkerPSerializer(serializers.ModelSerializer):
    
    markerProfilesDbIds = StringListField()

    class Meta:

        model = GPMarkerP
        fields = ('germplasmDbId', 'markerProfilesDbIds')

    # end class Meta


    def to_representation(self, instance: Call):
    
        instance.markerProfilesDbIds = [str(s) for s in instance.markerProfilesDbIds.split('; ')]

        return super(GPMarkerPSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(GPMarkerPSerializer, self).to_internal_value(data)

        if ret['markerProfilesDbIds']:
            ret['markerProfilesDbIds'] = '; '.join(str(s) for s in ret['markerProfilesDbIds'])
        # end if

        return ret

    # end def to_internal_value

# end class GPMarkerPSerializer


class StudySerializer(serializers.ModelSerializer):

    StudySerializer = StringListField()
    
    
    class Meta:

        model = Study
        fields = ['studyDbId', 'studyName', 'locationName']

    # end class Meta


    def to_representation(self, instance: Call):
    
        instance.contactDbId = [str(s) for s in instance.contactDbId.split('; ')]

        return super(StudySerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(StudySerializer, self).to_internal_value(data)

        if ret['contactDbId']:
            ret['contactDbId'] = '; '.join(str(s) for s in ret['contactDbId'])
        # end if

        return ret

    # end def to_internal_value
    
# end class StudySerializer


class TrialSerializer(serializers.ModelSerializer):

    studies = StudySerializer(many=True, read_only=True)

    class Meta:

        model = Trial
        fields = ['trialDbId', 'trialName', 'programDbId', 'name', 'startDate', 'endDate', 'active', 'studies']

    # end class Meta

# end class TrialSerializer


class SampleSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sample
        exclude = ['id']

    # end class Meta

# end class SampleSerializer


class ObservationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Observation
        exclude = ['id']

    # end class Meta

# end class ObservationSerializer


class ObservationUnitXrefSerializer(serializers.ModelSerializer):

    class Meta:

        model = ObservationUnitXref
        exclude = ['id']

    # end class Meta

# end class ObservationUnitXrefSerializer


class TreatmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Treatment
        exclude = ['id']

    # end class Meta

# end class TreatmentSerializer


class PhenotypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Phenotype
        exclude = ['id']

    # end class Meta

# end class PhenotypeSerializer


class DatatypeSerializer(serializers.ModelSerializer):
    
     class Meta:

        model = Datatype
        fields = ['data']

    # end class Meta

# end class DatatypeSerializer


class OntologySerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Ontology
        exclude = ['id']

    # end class Meta

# end class OntologySerializer


class StudySeasonSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = StudySeason
        fields = '__all__'

    # end class Meta

# end class StudySeasonSerializer


class StudyTypeSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = StudyType
        exclude = ['id']

    # end class Meta

# end class StudyTypeSerializer


class StudyObsLevelSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = StudyObsLevel
        exclude = ['id']

    # end class Meta

# end class StudyObsLevelSerializer


class StudyPlotSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = StudyPlot
        exclude = ['id']

    # end class Meta

# end class StudyPlotSerializer


class AlleleMatrixSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = AlleleMatrix
        exclude = ['id']

    # end class Meta

# end class AlleleMatrixSerializer


class AlleleMSearchSerializer(serializers.ModelSerializer):
    
    data = StringListField()

    class Meta:

        model = AlleleMSearch
        exclude = ['id']

    # end class Meta

    def to_representation(self, instance: Call):
        
        instance.data = [str(s) for s in instance.data.split('; ')]

        return super(AlleleMSearchSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(AlleleMSearchSerializer, self).to_internal_value(data)

        if ret['data']:
            ret['data'] = '; '.join(str(s) for s in ret['data'])
        # end if

        return ret

    # end def to_internal_value

# end class AlleleMSearchSerializer


class MarkerProfilesDataSerializer(serializers.ModelSerializer):
    
    data = StringListField()

    class Meta:

        model = MarkerProfilesData
        exclude = ['id']

    # end class Meta

    def to_representation(self, instance: Call):
    
        instance.data = [str(s) for s in instance.data.split('; ')]

        return super(MarkerProfilesDataSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(MarkerProfilesDataSerializer, self).to_internal_value(data)

        if ret['data']:
            ret['data'] = '; '.join(str(s) for s in ret['data'])
        # end if

        return ret

    # end def to_internal_value
    
# end class MarkerProfilesDataSerializer


class ObsVValueSerializer(serializers.ModelSerializer):
        
    categories = StringListField()


    class Meta:

        model = ObsVValue
        exclude = ['id']

    # end class Meta


    def to_representation(self, instance: Call):
    
        instance.categories = [str(s) for s in instance.categories.split('; ')]

        return super(ObsVValueSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(ObsVValueSerializer, self).to_internal_value(categories)

        if ret['categories']:
            ret['categories'] = '; '.join(str(s) for s in ret['categories'])
        # end if

        return ret

    # end def to_internal_value
    
# end class ObsVValueSerializer


class ObsMethodSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = ObsMethod
        exclude = ['id']

    # end class Meta

# end class ObsMethodSerializer


class ObsScaleSerializer(serializers.ModelSerializer):
    
    validValues = ObsVValueSerializer(read_only=True)

    class Meta:

        model = ObsScale
        exclude = ['id']

    # end class Meta

# end class ObsScaleSerializer


class ObsTraitSerializer(serializers.ModelSerializer):

    class Meta:

        model = ObsTrait
        exclude = ['id']

    # end class Meta

 # end class ObsTraitSerializer


class ObsVariableSerializer(serializers.ModelSerializer):
    
    method = ObsMethodSerializer(read_only=True)
    trait = ObsTraitSerializer(read_only=True)
    scale = ObsScaleSerializer(read_only=True)

    class Meta:

        model = ObsVariable
        exclude = ['id']

    # end class Meta
 
# end class ObsVariableSerializer


class StudyObsUnitSerializer(serializers.ModelSerializer):
    
    method = ObsMethodSerializer(read_only=True)
    trait = ObsTraitSerializer(read_only=True)
    scale = ObsScaleSerializer(read_only=True)

    class Meta:

        model = StudyObsUnit
        exclude = ['id']

    # end class Meta
 
# end class StudyObsUnitSerializer