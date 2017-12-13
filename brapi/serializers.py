from rest_framework import serializers
import logging
from pprint import pprint

from brapi.models import *
from brapi.aux_types import StringListField, IntListField


class ExtendedSerializer(serializers.ModelSerializer):

    def get_field_names(self, declared_fields, info):
        
        expanded_fields = super(ExtendedSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'exclude', None):
            expanded_fields = set(expanded_fields) - set(self.Meta.exclude)
        # end if
        
        if getattr(self.Meta, 'extra_fields', None):
            return list(expanded_fields) + self.Meta.extra_fields
        else:
            return list(expanded_fields)
        # end if
        
    # end def get_field_names
        
# end class ExtendedSerializer


class CallSerializer(serializers.ModelSerializer):

    datatypes = StringListField()
    methods = StringListField()


    class Meta:

        model = Call
        exclude = ['cropdbid', 'calldbid']

    # end class Meta


    def to_representation(self, instance: Call):

        instance.datatypes = [str(s) for s in instance.datatypes.split('; ')]
        instance.methods = [str(s) for s in instance.methods.split('; ')]

        return super(CallSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(CallSerializer, self).to_internal_value(data)

        if ret['datatypes']:
            ret['datatypes'] = '; '.join(str(s) for s in ret['datatypes'])
        # end if

        if ret['methods']:
            ret['methods'] = '; '.join(str(s) for s in ret['methods'])
        # end if

        return ret

    # end def to_internal_value

# end class CallsSerializer


class CropSerializer(serializers.ModelSerializer):

    class Meta:

        model = Crop
        exclude = ['cropdbid']

    # end class Meta

# end class CropSerializer


class DonorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Donor
        exclude = ['cropdbid', 'donordbid', 'germplasmDbId']

    # end class Meta

# end class DonorSerializer


class PedigreeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pedigree
        exclude = ['cropdbid', 'pedigreeDbId']

    # end class Meta

# end class PedigreeSerializer


class GermplasmAttributeValueSerializer(serializers.ModelSerializer):

    class Meta:

        model = GermplasmAttributeValue
        exclude = ['cropdbid', 'germplasmattributevaluedbid']

    # end class Meta

# end class GermplasmAttributeValueSerializer


class GermplasmAttributeSerializer(ExtendedSerializer):

    attributes = GermplasmAttributeValueSerializer(many=True, read_only=True)

    class Meta:

        model = GermplasmAttribute
        exclude = ['cropdbid']
        extra_fields = ['attributes']

        # end class Meta

# end class GermplasmAttributeSerializer


class GermplasmAttributeCategorySerializer(ExtendedSerializer):

    attributes = GermplasmAttributeSerializer(many=False, read_only=True)

    class Meta:

        model = GermplasmAttributeCategory
        exclude = ['cropdbid']
        extra_fields = ['attributes']

    # end class Meta

# end class GermplasmAttributeCategorySerializer


class LocationAdditionalInfoSerializer(serializers.ModelSerializer):

    pass

# end class LocationAdditionalInfoSerializer


class MapSerializer(serializers.ModelSerializer):

    class Meta:

        model = Map
        exclude = ['cropdbid']

    # end class Meta

# end class MapSerializer


class MarkerSerializer(serializers.ModelSerializer):

    synonyms = StringListField()
    refAlt = StringListField()
    analysisMethods = StringListField()


    class Meta:

        model = Marker
        exclude = ['cropdbid']

    # end class Meta


    def to_representation(self, instance: Marker):

        instance.synonyms = [str(s) for s in instance.synonyms.split('; ')]
        instance.refAlt = [str(s) for s in instance.refAlt.split('; ')]
        instance.analysisMethods = [str(s) for s in instance.analysisMethods.split('; ')]

        return super(MarkerSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(MarkerSerializer, self).to_internal_value(data)

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


class AlleleMatrixSerializer(serializers.ModelSerializer):

    class Meta:

        model = AlleleMatrix
        exclude = ['cropdbid']

        # end class Meta

# end class AlleleMatrixSerializer


class AlleleMatrixSearchSerializer(serializers.ModelSerializer):

    data = StringListField()


    class Meta:

        model = AlleleMatrixSearch
        exclude = ['cropdbid']

    # end class Meta


    def to_representation(self, instance):

        instance.data = [str(s) for s in instance.data.split('; ')]

        return super(AlleleMatrixSearchSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(AlleleMatrixSearchSerializer, self).to_internal_value(data)

        if ret['data']:
            ret['data'] = '; '.join(str(s) for s in ret['data'])
        # end if

        return ret

    # end def to_internal_value

# end class AlleleMatrixSearchSerializer


# class GermplasmMarkerProfileSerializer(serializers.ModelSerializer):
#
#     class Meta:
#
#         model = GermplasmMarkerProfile
#         fields = ['germplasmDbId', 'markerProfilesDbIds']
#
#         # end class Meta
#
# # end class GermplasmMarkerProfileSerializer


class MarkerProfileSerializer(ExtendedSerializer):

    class Meta:

        model = MarkerProfile
        exclude = ['cropdbid', 'sampleDbId', 'resultCount', 'studyDbId']

        # end class Meta

# end class MarkerProfileSerializer


class GermplasmMarkerProfileSerializer(ExtendedSerializer):

    markerprofileDbIds = serializers.SerializerMethodField()


    class Meta:

        model = MarkerProfile
        fields = ['germplasmDbId', 'markerprofileDbIds']

    # end class Meta


    def get_markerprofileDbIds(self, obj):

        return [ mp.markerprofileDbId for mp in MarkerProfile.objects.filter(germplasmDbId=obj.germplasmDbId) ]

    # end def get_markerprofileDbIds

# end class MarkerProfileSerializer


class MarkerProfilesDataSerializer(serializers.ModelSerializer):

    data = StringListField()

    class Meta:

        model = MarkerProfilesData
        exclude = ['cropdbid']

    # end class Meta

    def to_representation(self, instance):

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


class ObservationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Observation
        exclude = ['cropdbid']

    # end class Meta

# end class ObservationSerializer


class ObservationUnitXrefSerializer(ExtendedSerializer):

    observationUnits = ObservationSerializer(many=True, read_only=True)

    class Meta:

        model = ObservationUnitXref
        exclude = ['cropdbid']
        extra_fields = ['observationUnits']

    # end class Meta

# end class ObservationUnitXrefSerializer


class ObservationVariableSerializer(ExtendedSerializer):

    observations = ObservationSerializer(many=True, read_only=True)
    scale = serializers.SerializerMethodField()

    class Meta:

        model = ObservationVariable
        exclude = ['cropdbid']
        extra_fields = ['observations']

    # end class Meta


    def get_scale(self, obj):

        return ScaleSerializer(Scale.objects.get(pk=obj.scales.scaleDbId)).data

    # end def get_scale

# end class ObservationVariableSerializer


class ObservationVariableDatatypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = ObservationVariableDatatype
        fields = ['data']

    # end class Meta

# end class ObservationVariableDatatypeSerializer


class MethodSerializer(ExtendedSerializer):

    observationVariables = ObservationVariableSerializer(many=True, read_only=True)

    class Meta:

        model = Method
        exclude = ['cropdbid']
        extra_fields = ['observationVariables']

        # end class Meta

# end class MethodSerializer


class OntologySerializer(ExtendedSerializer):

    observationVariables = ObservationVariableSerializer(many=True, read_only=True)

    class Meta:

        model = Ontology
        exclude = ['cropdbid']
        extra_fields = ['observationVariables']

    # end class Meta

# end class OntologySerializer


class PedigreeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pedigree
        exclude = ['cropdbid']

    # end class Meta

# end class PedigreeSerializer


class ValidValueSerializer(ExtendedSerializer):

    categories = StringListField()


    class Meta:

        model = ValidValue
        exclude = ['cropdbid']
        extra_fields = ['categories']

    # end class Meta


    def to_representation(self, instance: ValidValue):

        instance.categories = [str(s) for s in instance.categories.split('; ')]

        return super(ValidValueSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(ValidValueSerializer, self).to_internal_value(data)

        if ret['categories']:
            ret['categories'] = '; '.join(str(s) for s in ret['categories'])
        # end if

        return ret

    # end def to_internal_value

# end class ValidValueSerializer


class ScaleSerializer(ExtendedSerializer):

    validValues = ValidValueSerializer(many=True, read_only=True)

    class Meta:

        model = Scale
        exclude = ['cropdbid']
        extra_fields = ['validValues']

    # end class Meta

# end class ScaleSerializer


class StudyObservationLevelSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudyObservationLevel
        fields = ['data']

    # end class Meta

# end class StudyObservationLevelSerializer


class StudyAdditionalInfoSerializer(serializers.ModelSerializer):

    pass

# end class StudyAdditionalInfoSerializer


class StudyContactSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudyContact
        exclude = ['cropdbid']

    # end class Meta

# end class StudyContactSerializer


class StudyDataLinkSerializer(serializers.ModelSerializer):

    class Meta:

        model = StudyDataLink
        exclude = ['cropdbid']

    # end class Meta

# end class StudyDataLinkSerializer


class StudySeasonSerializer(serializers.ModelSerializer):

    pass

# end class StudySeasonSerializer


class SeasonSerializer(ExtendedSerializer):

    #observations = ObservationSerializer(many=True, read_only=True)
    #seasons = StudySeasonSerializer(many=True, read_only=True)

    class Meta:

        model = Season
        exclude = ['cropdbid']

    # end class Meta

# end class SeasonSerializer


class SampleSerializer(ExtendedSerializer):

    season = serializers.SerializerMethodField()


    class Meta:

        model = Sample
        exclude = ['cropDbId', 'seasonDbId']
        extra_fields = ['season']

    # end class Meta


    def get_season(self, obj):

        logger = logging.getLogger(__name__)
        logger.warning("Getting seasonID %s" % obj.seasonDbId_id)
        return Season.objects.get(pk=obj.seasonDbId_id).season

    # end def get_season

# end class SampleSerializer


class TaxonXrefGermplasmSerializer(ExtendedSerializer):

    class Meta:

        model = TaxonXrefGermplasm
        exclude = ['cropdbid']

    # end class Meta

# end class TaxonXrefGermplasmSerializer


class TaxonXrefSerializer(ExtendedSerializer):

    pass

# end class TaxonXrefSerializer


class TraitSerializer(ExtendedSerializer):

    class Meta:

        model = Trait
        exclude = ['cropdbid']
        extra_fields = ['traitDbId', 'observationVariables', 'defaultValue']

    # end class Meta

# end class TraitSerializer


class TreatmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Treatment
        exclude = ['cropdbid']

    # end class Meta

# end class TreatmentSerializer


class ObservationUnitSerializer(ExtendedSerializer):

    observations = ObservationSerializer(many=True, read_only=True)
    treatments = TreatmentSerializer(many=True, read_only=True)

    class Meta:

        model = ObservationUnit
        exclude = ['cropdbid']
        extra_fields = ['observations', 'treatments']

    # end class Meta

# end class ObservationUnitSerializer


class StudySerializer(ExtendedSerializer):

    observationUnits = ObservationUnitSerializer(many=True, read_only=True)
    contacts = StudyContactSerializer(many=True, read_only=True)
    dataLinks = StudyDataLinkSerializer(many=True, read_only=True)
    seasons = serializers.SerializerMethodField()
    additionalInfo = serializers.SerializerMethodField()

    class Meta:

        model = Study
        exclude = ['cropdbid']
        extra_fields = ['observationUnits', 'contacts', 'dataLinks', 'seasons', 'additionalInfo', 'locationName']

    # end class Meta


    def get_seasons(self, obj):

        logger = logging.getLogger(__name__)

        sID = obj.studydbid
        logger.warning("Getting seasons for study %s" % sID)

        sseasons = Season.objects.filter(seasons1__studyDbId=sID).all()
        logger.warning("Getting seasons for study %s" % sseasons.seasons1)

        return sseasons

    # end def get_seasons


    def get_additionalInfo(self, obj):

        return {
            info.key: info.value
            for info in StudyAdditionalInfo.objects.all()
        }

    # end def get_addInfo

# end class StudySerializer


class StudyTypeSerializer(ExtendedSerializer):

    #studies = StudySerializer(many=True, read_only=True)

    class Meta:

        model = StudyType
        exclude = ['cropdbid']
        #extra_fields = ['studies']

    # end class Meta

# end class StudyTypeSerializer


class LocationSerializer(ExtendedSerializer):

    studies = StudySerializer(many=True, read_only=True)
    additionalInfo = serializers.SerializerMethodField()

    class Meta:

        model = Location
        exclude = ['cropdbid']
        extra_fields = ['studies', 'additionalInfo']

    # end class Meta

    def get_additionalInfo(self, obj):

        return {
            info.key: info.value
            for info in LocationAdditionalInfo.objects.all()
        }

    # end def get_addInfo

# end class LocationSerializer


class GermplasmSerializer(ExtendedSerializer):

    synonyms = StringListField()
    typeOfGermplasmStorageCode = IntListField()
    donors = DonorSerializer(many=True, read_only=True)
    taxonIds = serializers.SerializerMethodField()
    donors = DonorSerializer(many=True, read_only=True)


    class Meta:

        model = Germplasm
        exclude = ['cropdbid']
        extra_fields = ['synonyms', 'typeOfGermplasmStorageCode', 'donors',
                        'acquisitionDate', 'taxonIds']

    # end class Meta


    def get_taxonIds(self, obj):

        logger = logging.getLogger(__name__)

        t = TaxonXrefGermplasm.objects.filter(germplasmDbId=obj.germplasmDbId)
        #pprint(t.__dict__)

        t2 = TaxonXref.objects.filter(taxondbid__in=t)
        #logger.warning("Filtering taxa:")
        #[pprint(t.__dict__) for t in t2]

        return [ { t.source: t.rank } for t in t2 ]

    # end def get_taxonIds


    def to_representation(self, instance: Germplasm):

        instance.synonyms = [str(s) for s in instance.synonyms.split('; ')]
        instance.typeOfGermplasmStorageCode = [int(s) for s in instance.typeOfGermplasmStorageCode.split('; ')]

        return super(GermplasmSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(GermplasmSerializer, self).to_internal_value(data)
        if ret['typeOfGermplasmStorageCode']:
            ret['typeOfGermplasmStorageCode'] = '; '.join(str(s) for s in ret['typeOfGermplasmStorageCode'])
        # end if

        if ret['synonyms']:
            ret['synonyms'] = '; '.join(str(s) for s in ret['synonyms'])
        # end if

        return ret

    # end def to_internal_value

# end class GermplasmSerializer


class TrialAdditionalInfoSerializer(serializers.ModelSerializer):

    class Meta:

        model = TrialAdditionalInfo
        exclude = ['cropdbid']

    # end class Meta

# end class TrialAdditionalInfoSerializer


class TrialContactSerializer(serializers.ModelSerializer):

    contacts = serializers.SerializerMethodField()


    class Meta:

        model = TrialContact
        exclude = ['cropdbid', 'trialcontactdbid']

    # end class Meta


    def get_contacts(self, obj):

        print(Contact.objects.filter(pk=obj.contactdbid.contactDbId))
        return [ContactSerializer(c).data for c in Contact.objects.filter(pk=obj.contactdbid.contactDbId)]

    # end def get_contacts

# end class TrialContactSerializer


class TrialStudySerializer(ExtendedSerializer):

    locationName = serializers.SerializerMethodField()


    class Meta:

        model = Study
        fields = ['studydbid', 'locationDbId', 'studyName', 'locationName']

    # end class Meta


    def get_locationName(self, obj):

        return Location.objects.get(pk=obj.locationDbId.locationDbId).name

    # end def get_locationName

# end class TrialStudySerializer


class TrialSerializer(ExtendedSerializer):

    studies = TrialStudySerializer(many=True, read_only=True)
    contacts = TrialContactSerializer(many=True, read_only=True)
    datasetAuthorship = serializers.SerializerMethodField()
    contacts = serializers.SerializerMethodField()
    programName = serializers.SerializerMethodField()
    additionalInfo = serializers.SerializerMethodField()


    class Meta:

        model = Trial
        exclude = ['cropdbid', 'datasetAuthorshipLicence', 'datasetAuthorshipDatasetPUI']
        extra_fields = ['studies', 'contacts', 'additionalInfo', 'datasetAuthorship']

    # end class Meta


    def get_datasetAuthorship(self, obj):

        return {
            'license': obj.datasetAuthorshipLicence,
            'datasetPUI': obj.datasetAuthorshipDatasetPUI
        }

    # end def get_addInfo


    def get_contacts(self, obj):

        tc = TrialContact.objects.filter(trialdbid=obj.trialDbId).all()
        print("TC:", tc)
        return [ContactSerializer(c).data for c in Contact.objects.filter(pk=tc)]

    # end def get_contacts


    def get_programName(self, obj):

        return Program.objects.get(pk=obj.programDbId.programDbId).name

    # end def get_programName


    def get_additionalInfo(self, obj):

        return {
            info.key: info.value
            for info in TrialAdditionalInfo.objects.all()
        }

    # end def get_addInfo

# end class TrialSerializer


class ProgramSerializer(ExtendedSerializer):

    trials = TrialSerializer(many=True, read_only=True)

    class Meta:

        model = Program
        exclude = ['cropdbid']
        extra_fields = ['trials']

    # end class Meta

# end class ProgramSerializer


class ContactSerializer(ExtendedSerializer):

    class Meta:

        model = Contact
        exclude = ['cropdbid']

    # end class Meta

# end class ContactSerializer



class MapLinkageSerializer(serializers.ModelSerializer):

    class Meta:

        model = MapLinkage
        exclude = ['id', 'mapDbId']

    # end class Meta

# end class MapLinkageSerializer


class MapSerializer(serializers.ModelSerializer):

    linkageGroupCount = serializers.SerializerMethodField()
    markerCount = serializers.SerializerMethodField()


    class Meta:

        model = Map
        fields = '__all__'

    # end class Meta


    def get_linkageGroupCount(self, obj):

        return obj.linkageGroups.count()

    # end def get_linkageGroupCount


    def get_markerCount(self, obj):

        return (Map.objects
                .aggregate(markerCount=models.Count('linkageGroups__markerDbId'))
                ['markerCount'])

    # end def get_markerCount

# end class MapSerializer


class MapDetailSerializer(serializers.ModelSerializer):

    linkageGroups = serializers.SerializerMethodField()


    class Meta:

        model = Map
        fields = ['mapDbId', 'name', 'type', 'unit', 'linkageGroups']

    # end class Meta


    def get_linkageGroups(self, obj):

        return (Map.objects
                .annotate(linkageGroupId=models.F('linkageGroups__linkageGroupId'))
                .values('linkageGroupId')
                .annotate(markerCount=models.Count('linkageGroups__markerDbId'))
                .annotate(maxPosition=models.Max('linkageGroups__location'))
                .values('linkageGroupId', 'markerCount', 'maxPosition'))

    # end def get_linkageGroups

# end class MapDetailSerializer


class PhenotypeSerializer(serializers.ModelSerializer):

    observationUnitXref = ObservationUnitXrefSerializer(many=True, read_only=True)
    observations = ObservationSerializer(read_only=True)

    class Meta:

        model = Phenotype
        exclude = ['cropdbid']

    # end class Meta

# end class PhenotypeSerializer
