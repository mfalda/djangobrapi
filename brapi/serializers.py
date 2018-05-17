from rest_framework import serializers
import logging
from pprint import pformat

from brapi.models import *
from brapi.aux_fun import in_list
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
        exclude = ['cropdbid', 'donordbid', 'germplasmDbId', 'donorGermplasmPUI']

    # end class Meta

# end class DonorSerializer


class PedigreeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pedigree
        exclude = ['cropdbid', 'pedigreeDbId']

    # end class Meta

# end class PedigreeSerializer


class GermplasmAttributeValueSerializer(serializers.ModelSerializer):

    germplasmDbId = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()


    class Meta:

        model = GermplasmAttributeValue
        fields = ['germplasmDbId', 'data']

    # end class Meta


    def get_germplasmDbId(self, obj):

        return obj.germplasmDbId_id

    # end def get_germplasmDbId


    def get_data(self, obj):

        return GermplasmAttributeValue.objects.values('attributeDbId',
                                                      'attributeName',
                                                      'attributeCode',
                                                      'value',
                                                      'determinedDate')

    # end def get_data

# end class GermplasmAttributeValueSerializer


class GermplasmAttributeSerializer(ExtendedSerializer):

    attributes = GermplasmAttributeValueSerializer(many=True, read_only=True)
    values = StringListField()


    class Meta:

        model = GermplasmAttribute
        exclude = ['cropdbid', 'attributeDbId']
        extra_fields = ['attributes']

    # end class Meta


    def to_representation(self, instance: Call):

        instance.values = [str(s) for s in instance.values.split('; ')]

        return super(GermplasmAttributeSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(GermplasmAttributeSerializer, self).to_internal_value(data)

        if ret['values']:
            ret['values'] = '; '.join(str(s) for s in ret['values'])
        # end if

        return ret

    # end def to_internal_value

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

    data = serializers.SerializerMethodField()


    class Meta:

        model = MarkerprofileData
        exclude = ['cropdbid', 'markerprofilesdatadbid', 'alleleCall', 'markerDbId', 'markerprofileDbId']

    # end class Meta


    def get_data(self, obj):

        return [
            ( mpd.markerDbId.markerDbId, mpd.markerprofileDbId.markerprofileDbId, mpd.alleleCall )
            for mpd in MarkerprofileData.objects.filter(markerprofileDbId=obj.markerprofileDbId)
        ]

    # end def get_data

# end class AlleleMatrixSearchSerializer


class MarkerprofileSerializer(ExtendedSerializer):

    resultCount = serializers.SerializerMethodField()


    class Meta:

        model = Markerprofile
        exclude = ['cropdbid', 'studyDbId']

    # end class Meta


    def get_resultCount(self, obj):

        return MarkerprofileData.objects.filter(markerprofileDbId=obj.markerprofileDbId).count()

    # end def get_resultCount

# end class MarkerprofileSerializer


class GermplasmMarkerprofileSerializer(ExtendedSerializer):

    markerprofileDbIds = serializers.SerializerMethodField()


    class Meta:

        model = Markerprofile
        fields = ['germplasmDbId', 'markerprofileDbIds']

    # end class Meta


    def get_markerprofileDbIds(self, obj):

        return [ str(mp.markerprofileDbId) for mp in Markerprofile.objects.filter(germplasmDbId=obj.germplasmDbId) ]

    # end def get_markerprofileDbIds

# end class MarkerprofileSerializer


class MarkerprofileDataSerializer(serializers.ModelSerializer):

    data = serializers.SerializerMethodField()


    class Meta:

        model = Markerprofile
        exclude = ['cropdbid', 'sampleDbId', 'studyDbId']

    # end class Meta


    def get_data(self, obj):

        return [
            { mpd.markerDbId.defaultDisplayName: mpd.alleleCall }
            for mpd in MarkerprofileData.objects.filter(markerprofileDbId=obj.markerprofileDbId)
        ]

    # end def get_data

# end class MarkerprofilesDataSerializer


class ObservationSerializer(serializers.ModelSerializer):

    observationVariableName = serializers.SerializerMethodField()
    observationVariableDbId = serializers.SerializerMethodField()

    class Meta:

        model = Observation
        exclude = ['cropdbid', 'observationUnit', 'obsVariable', 'observationTimestamp', 'seasonDbId', 'uploadedBy']

    # end class Meta


    def get_observationVariableName(self, obj):

        return ObservationVariable.objects.get(pk=obj.obsVariable.observationVariableDbId).observationVariableName

    # end def get_observationVariableName


    def get_observationVariableDbId(self, obj):

        return obj.obsVariable.observationVariableDbId

    # end def get_observationVariableDbId

# end class ObservationSerializer


class ObservationUnitXrefSerializer(serializers.ModelSerializer):

    id = serializers.SerializerMethodField('get_identifier')


    class Meta:

        model = ObservationUnitXref
        fields = ('id', 'source')

    # end class Meta


    def get_identifier(self, obj):

        return obj.identifier

    # end def get_identifier

# end class ObservationUnitXrefSerializer


class ObservationUnitSerializer(ExtendedSerializer):

    germplasmName = serializers.SerializerMethodField()
    observationUnitXref = ObservationUnitXrefSerializer(many=True, read_only=True)
    observations = ObservationSerializer(many=True, read_only=True)


    class Meta:

        model = ObservationUnit
        exclude = ['cropdbid', 'observationLevels', 'programDbId', 'studyDbId']
        extra_fields = ['germplasmName', 'observations', 'observationUnitXref']

    # end class Meta


    def get_germplasmName(self, obj):

        return Germplasm.objects.get(pk=obj.germplasmDbId.germplasmDbId).germplasmName

    # end def get_germplasmName

# end class ObservationUnitSerializer


class StudyObservationUnitByObservationVariableSerializer(ExtendedSerializer):

    studyDbId = serializers.SerializerMethodField()
    observationVariableName = serializers.SerializerMethodField()
    observationVariableDbId = serializers.SerializerMethodField()
    observationUnitDbId = serializers.SerializerMethodField()
    observationUnitName = serializers.SerializerMethodField()
    observationLevel = serializers.SerializerMethodField()
    germplasmDbId = serializers.SerializerMethodField()
    germplasmName = serializers.SerializerMethodField()


    class Meta:

        model = Observation
        exclude = ['cropdbid', 'obsVariable', 'observationUnit']

    # end class Meta


    def get_germplasmDbId(self, obj):

        return obj.observationUnit.germplasmDbId.germplasmDbId

    # end def get_germplasmDbId


    def get_germplasmName(self, obj):

        return Germplasm.objects.get(pk=obj.observationUnit.germplasmDbId.germplasmDbId).germplasmName

    # end def get_germplasmName


    def get_studyDbId(self, obj):

        return obj.observationUnit.studyDbId.studyDbId

    # end def get_studyDbId


    def get_observationUnitName(self, obj):

        return obj.observationUnit.observationUnitName

    # end def get_observationUnitName


    def get_observationUnitDbId(self, obj):

        return obj.observationUnit.observationUnitDbId

    # end def get_observationUnitDbId


    def get_observationVariableDbId(self, obj):

        return obj.obsVariable.observationVariableDbId

    # end def get_observationVariableDbId


    def get_observationVariableName(self, obj):

        return obj.obsVariable.observationVariableName

    # end def get_observationVariableName


    def get_observationLevel(self, obj):

        return obj.observationUnit.observationLevel

    # end def get_observationLevel


    def get_value(self, obj):

        return obj.observationUnit.value

    # end def get_value

# end class StudyObservationUnitByObservationVariableSerializer


class ObservationVariableSerializer(ExtendedSerializer):

    name = serializers.SerializerMethodField()
    synonyms = StringListField()
    ontologyName = serializers.SerializerMethodField()
    contextOfUse = StringListField()
    crop = serializers.SerializerMethodField()
    scale = serializers.SerializerMethodField()
    trait = serializers.SerializerMethodField()
    method = serializers.SerializerMethodField()


    class Meta:

        model = ObservationVariable
        exclude = ['cropdbid', 'traitDbId', 'methodDbId', 'scales', 'observationVariableName']
        extra_fields = ['crop', 'trait', 'method']

    # end class Meta


    def get_name(self, obj):

        return obj.observationVariableName

    # end def get_name


    def to_representation(self, instance: ObservationVariable):

        instance.synonyms = [str(s) for s in instance.synonyms.split('; ')]
        instance.contextOfUse = [str(s) for s in instance.contextOfUse.split('; ')]

        return super(ObservationVariableSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(ObservationVariableSerializer, self).to_internal_value(data)

        if ret['synonyms']:
            ret['synonyms'] = '; '.join(str(s) for s in ret['synonyms'])
        # end if

        if ret['contextOfUse']:
            ret['contextOfUse'] = '; '.join(str(s) for s in ret['contextOfUse'])
        # end if

        return ret

    # end def to_internal_value


    def get_ontologyName(self, obj):

        return Ontology.objects.get(pk=obj.ontologyDbId.ontologyDbId).ontologyName

    # end def get_ontologyName


    def get_crop(self, obj):

        return Crop.objects.get(pk=obj.cropdbid.cropdbid).commonname

    # end def get_crop


    def get_scale(self, obj):

        return ScaleSerializer(Scale.objects.get(pk=obj.scales.scaleDbId)).data

    # end def get_scale


    def get_trait(self, obj):

        return OVTraitSerializer(Trait.objects.get(pk=obj.traitDbId.traitDbId)).data

    # end def get_trait


    def get_method(self, obj):

        if obj.methodDbId is not None:
            return MethodSerializer(Method.objects.filter(methodDbId=obj.methodDbId.methodDbId).first()).data
        else:
            return None
    # end if

    # end def get_method


    def get_datatype(self, obj):

        return obj.scales.datatypeDbId.data

    # end def get_datatype

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


    def to_representation(self, instance: Method):

        data = super(MethodSerializer, self).to_representation(instance)

        # generate a list of the keys and replace the key 'classis'
        keys = list(data.keys())
        keys.insert(keys.index('classis'), 'class')
        keys.remove('classis')

        # remove 'classis' and assign its value to a new key 'class'
        classis = data.pop('classis')
        data.update({'class': classis})

        return data

    # end def to_representation

# end class MethodSerializer


class OntologySerializer(ExtendedSerializer):

    observationVariables = ObservationVariableSerializer(many=True, read_only=True)

    class Meta:

        model = Ontology
        exclude = ['cropdbid']
        extra_fields = ['observationVariables']

    # end class Meta

# end class OntologySerializer


class ValidValueSerializer(ExtendedSerializer):

    categories = StringListField()


    class Meta:

        model = ValidValue
        exclude = ['cropdbid', 'validValueDbId']
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

    datatype = serializers.SerializerMethodField()
    validValues = serializers.SerializerMethodField()


    class Meta:

        model = Scale
        exclude = ['cropdbid', 'datatypeDbId', 'defaultValue']
        extra_fields = ['datatype', 'validValues']

    # end class Meta


    def get_datatype(self, obj):

        return obj.datatypeDbId.data

    # end def get_datatype


    def get_validValues(self, obj):

        logger = logging.getLogger(__name__)

        # get all related objects in a One-to-Many relation
        vv = ValidValue.objects.get(pk=obj.validValues.validValueDbId)
        logger.warning("Getting valid values for scale %s" % pformat(vv.__dict__))

        # serialize the retrieved object(s), the JSON is in the 'data' field
        return ValidValueSerializer(vv).data

    # end def get_validValues

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


class StudyDataLinkSerializer(ExtendedSerializer):

    class Meta:

        model = StudyDataLink
        exclude = ['cropdbid', 'studydatalinkdbid', 'studydbid']

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
    locationName = serializers.SerializerMethodField()
    #studyName = serializers.SerializerMethodField()
    plotNumber = serializers.SerializerMethodField()
    entryNumber = serializers.SerializerMethodField()


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


    def get_locationName(self, obj):

        return Location.objects.get(pk=obj.locationDbId.locationDbId).name

    # end def get_locationName


    def get_studyName(self, obj):

        return Study.objects.get(pk=obj.studyDbId.studyDbId).studyName

    # end def get_studyName


    def get_plotNumber(self, obj):

        return ObservationUnit.objects.get(pk=obj.observationUnitDbId.observationUnitDbId).plotNumber

    # end def get_plotNumber


    def get_entryNumber(self, obj):

        return ObservationUnit.objects.get(pk=obj.observationUnitDbId.observationUnitDbId).entryNumber

    # end def get_entryNumber

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
        exclude = ['cropdbid', 'attribute', 'alternativeAbbreviations', 'xref', 'classis',
                   'entity', 'status', 'mainAbbreviation', 'synonyms']
        extra_fields = ['traitDbId', 'observationVariables', 'defaultValue']

    # end class Meta

# end class TraitSerializer


class OVTraitSerializer(ExtendedSerializer):

    synonyms = StringListField()
    alternativeAbbreviations = StringListField()


    class Meta:

        model = Trait
        exclude = ['cropdbid', 'traitId', 'defaultValue']

    # end class Meta


    def to_representation(self, instance: Trait):

        instance.synonyms = [str(s) for s in instance.synonyms.split('; ')]
        instance.alternativeAbbreviations = [str(s) for s in instance.alternativeAbbreviations.split('; ')]

        data = super(OVTraitSerializer, self).to_representation(instance)

        # generate a list of the keys and replace the key 'classis'
        keys = list(data.keys())
        keys.insert(keys.index('classis'), 'class')
        keys.remove('classis')

        # remove 'classis' and assign its value to a new key 'class'
        classis = data.pop('classis')
        data.update({'class': classis})

        return data

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(OVTraitSerializer, self).to_internal_value(data)

        if ret['synonyms']:
            ret['synonyms'] = '; '.join(str(s) for s in ret['synonyms'])
        # end if

        if ret['alternativeAbbreviations']:
            ret['alternativeAbbreviations'] = '; '.join(str(s) for s in ret['alternativeAbbreviations'])
        # end if

        return ret

    # end def to_internal_value

# end class OVTraitSerializer


class TreatmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Treatment
        exclude = ['cropdbid', 'treatmentdbid', 'observationUnitDbId']

    # end class Meta

# end class TreatmentSerializer


class StudyPlotLayoutSerializer(ExtendedSerializer):

    germplasmName = serializers.SerializerMethodField()
    additionalInfo = serializers.SerializerMethodField()


    class Meta:

        model = ObservationUnit
        exclude = ['cropdbid', 'plotNumber', 'plantNumber', 'programDbId', 'entryNumber',
                   'observationLevels']
        extra_fields = ['germplasmName']

    # end class Meta


    def get_germplasmName(self, obj):

        return Germplasm.objects.get(pk=obj.germplasmDbId.germplasmDbId).germplasmName

    # end def get_germplasmName


    def get_additionalInfo(self, obj):

        return {
            info.key: info.value
            for info in ObservationUnitAdditionalInfo.objects.all()
        }

    # end def get_addInfo

# end class StudyPlotLayoutSerializer


class StudySerializer(ExtendedSerializer):

    dataLinks = StudyDataLinkSerializer(many=True, read_only=True)
    seasons = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    trialName = serializers.SerializerMethodField()
    lastUpdate = serializers.SerializerMethodField()
    contacts = serializers.SerializerMethodField()
    additionalInfo = serializers.SerializerMethodField()

    class Meta:

        model = Study
        exclude = ['cropdbid']
        extra_fields = ['contacts', 'dataLinks', 'seasons', 'additionalInfo', 'location']

    # end class Meta


    def get_seasons(self, obj):

        logger = logging.getLogger(__name__)

        ss = StudySeason.objects.filter(studyDbId=obj.studyDbId).all()
        logger.warning("Getting seasons for study %s" % str([pformat(ss.__dict__) for ss in ss]))

        seasons = Season.objects.filter(seasonDbId__in=ss)
        logger.warning("Season: %s" % str([pformat(season.__dict__) for season in seasons]))

        return ["%s %s" % (season.year, season.season) for season in seasons]

    # end def get_seasons


    def get_trialName(self, obj):

        return Trial.objects.get(pk=obj.trialDbId.trialDbId).trialName

    # end def get_trialName


    def get_location(self, obj):

        return LocationSerializer(Location.objects.get(pk=obj.locationDbId.locationDbId)).data

    # end def get_location


    def get_lastUpdate(self, obj):

        return {
            'version': obj.lastUpdateVersion,
            'timestamp': obj.lastUpdateTimestamp
        }

    # end def get_lastUpdate


    def get_contacts(self, obj):

        sc = StudyContact.objects.filter(studydbid=obj.studyDbId).all()

        logger = logging.getLogger(__name__)
        logger.warning("Study contacts: %s" % str([pformat(s.__dict__) for s in sc]))

        contacts = Contact.objects.filter(contactDbId__in=sc)
        logger.warning("Contact: %s" % str([pformat(contact.__dict__) for contact in contacts]))

        return [ContactSerializer(contact).data for contact in contacts]

    # end def get_contacts


    def get_additionalInfo(self, obj):

        return {
            info.key: in_list(info.value)
            for info in StudyAdditionalInfo.objects.all()
        }

    # end def get_addInfo

# end class StudySerializer


class StudySearchSerializer(ExtendedSerializer):

    name = serializers.SerializerMethodField()
    active = serializers.SerializerMethodField()
    seasons = serializers.SerializerMethodField()
    locationName = serializers.SerializerMethodField()
    programDbId = serializers.SerializerMethodField()
    programName = serializers.SerializerMethodField()
    trialName = serializers.SerializerMethodField()
    additionalInfo = serializers.SerializerMethodField()


    class Meta:

        model = Study
        exclude = ['cropdbid', 'lastUpdateTimestamp', 'lastUpdateVersion', 'licence',
                   'studyDescription', 'studyName']
        extra_fields = ['seasons', 'additionalInfo', 'locationDbId', 'locationName',
                        'programDbId', 'programName']

    # end class Meta


    def get_name(self, obj):

        return obj.studyName

    # end def get_name


    def get_active(self, obj):

        return str(obj.active).lower()

    # end def get_active


    def get_seasons(self, obj):

        logger = logging.getLogger(__name__)

        ss = StudySeason.objects.filter(studyDbId=obj.studyDbId).all()
        logger.warning("Getting seasons for study %s" % str([pformat(ss.__dict__) for ss in ss]))

        seasons = Season.objects.filter(seasonDbId__in=ss)
        logger.warning("Season: %s" % str([pformat(season.__dict__) for season in seasons]))

        return ["%s %s" % (season.year, season.season) for season in seasons]

    # end def get_seasons


    def get_trialName(self, obj):

        return Trial.objects.get(pk=obj.trialDbId.trialDbId).trialName

    # end def get_trialName


    def get_locationName(self, obj):

        return Location.objects.get(pk=obj.locationDbId.locationDbId).name

    # end def get_locationName


    def get_programDbId(self, obj):

        return obj.trialDbId.programDbId.programDbId

    # end def get_programDbId


    def get_programName(self, obj):

        return Program.objects.get(pk=obj.trialDbId.programDbId.programDbId).name

    # end def get_programName


    def get_additionalInfo(self, obj):

        return {
            info.key: in_list(info.value)
            for info in StudyAdditionalInfo.objects.all()
        }

        # end def get_addInfo

# end class StudySearchSerializer


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
        exclude = ['cropdbid', 'type']
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
    typeOfGermplasmStorageCode = StringListField()
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

        return [ { 'sourceName': t.source, 'taxonId': t.rank } for t in t2 ]

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


class StudyGermplasmSerializer(ExtendedSerializer):

    entryNumber = serializers.SerializerMethodField()
    synonyms = StringListField()


    class Meta:

        model = Germplasm
        exclude = ['cropdbid', 'species', 'subtaxa', 'genus',
                   'speciesAuthority', 'subtaxaAuthority',
                   'typeOfGermplasmStorageCode', 'commonCropName',
                    'instituteName', 'countryOfOriginCode',
                    'defaultDisplayName', 'instituteCode',
                    'biologicalStatusOfAccessionCode',
                    'acquisitionDate']
        extra_fields = ['synonyms', 'entryNumber']

    # end class Meta


    def get_entryNumber(self, obj):

        return ObservationUnit.objects.get(pk=obj.germplasmDbId).entryNumber

    # end def get_entryNumber


    def to_representation(self, instance: Germplasm):

        instance.synonyms = [str(s) for s in instance.synonyms.split('; ')]

        return super(StudyGermplasmSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(StudyGermplasmSerializer, self).to_internal_value(data)

        if ret['synonyms']:
            ret['synonyms'] = '; '.join(str(s) for s in ret['synonyms'])
        # end if

        return ret

    # end def to_internal_value

# end class StudyGermplasmSerializer


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
        fields = ['studyDbId', 'locationDbId', 'studyName', 'locationName']

    # end class Meta


    def get_locationName(self, obj):

        return Location.objects.get(pk=obj.locationDbId.locationDbId).name

    # end def get_locationName

# end class TrialStudySerializer


class TrialSerializer(ExtendedSerializer):

    studies = TrialStudySerializer(many=True, read_only=True)
    programName = serializers.SerializerMethodField()
    additionalInfo = serializers.SerializerMethodField()


    class Meta:

        model = Trial
        exclude = ['cropdbid', 'datasetAuthorshipLicence', 'datasetAuthorshipDatasetPUI']
        extra_fields = ['studies', 'additionalInfo']

    # end class Meta


    def get_datasetAuthorship(self, obj):

        return {
            'licence': obj.datasetAuthorshipLicence,
            'datasetPUI': obj.datasetAuthorshipDatasetPUI
        }

    # end def get_addInfo


    def get_contacts(self, obj):

        tc = TrialContact.objects.filter(trialdbid=obj.trialDbId).all()
        logger = logging.getLogger(__name__)
        logger.warning("Trial contact: %s" % tc)

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

    markerDbId = serializers.SerializerMethodField()
    linkageGroupName = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()


    class Meta:

        model = MapLinkage
        exclude = ['id', 'mapDbId', 'linkageGroupId']

    # end class Meta


    def get_markerDbId(self, obj):

        return str(obj.markerDbId)

    # end def get_markerDbId


    def get_linkageGroupName(self, obj):

        return str(obj.linkageGroupId)

    # end def get_linkageGroupName


    def get_location(self, obj):

        return str(obj.location)

    # end def get_location

# end class MapLinkageSerializer


class MapSerializer(serializers.ModelSerializer):

    mapDbId = serializers.SerializerMethodField()
    linkageGroupCount = serializers.SerializerMethodField()
    markerCount = serializers.SerializerMethodField()


    class Meta:

        model = Map
        fields = '__all__'

    # end class Meta


    def get_mapDbId(self, obj):

        return str(obj.mapDbId)

    # end def get_mapDbId


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

    mapDbId = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()


    class Meta:

        model = Map
        fields = ['mapDbId', 'name', 'type', 'unit', 'data']

    # end class Meta


    def get_mapDbId(self, obj):

        return str(obj.mapDbId)

    # end def get_mapDbId


    def get_data(self, obj):

        value = (Map.objects
                .annotate(linkageGroupId=models.F('linkageGroups__linkageGroupId'))
                .values('linkageGroupId')
                .annotate(linkageGroupName=models.F('linkageGroups__linkageGroupId'))
                .annotate(markerCount=models.Count('linkageGroups__markerDbId'))
                .annotate(maxPosition=models.Max('linkageGroups__location'))
                .values('linkageGroupName', 'markerCount', 'maxPosition'))

        return [{ 'linkageGroupName': str(v['linkageGroupName']),
                  'markerCount': v['markerCount'],
                  'maxPosition': v['maxPosition'] } for v in value
               ]

    # end def get_linkageGroups

# end class MapDetailSerializer


class MapLinkagePositionsSerializer(serializers.ModelSerializer):

    markerDbId = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()


    class Meta:

        model = MapLinkage
        exclude = ['id', 'mapDbId', 'linkageGroupId']

    # end class Meta


    def get_markerDbId(self, obj):

        return str(obj.markerDbId)

    # end def get_markerDbId


    def get_location(self, obj):

        return str(obj.location)

    # end def get_location

# end class MapLinkagePositionsSerializer


class PhenotypeSerializer(serializers.ModelSerializer):

    observationUnitXref = serializers.SerializerMethodField()
    observations = serializers.SerializerMethodField()
    treatments = serializers.SerializerMethodField()
    studyLocationDbId = serializers.SerializerMethodField('get_study_location')


    class Meta:

        model = Phenotype
        exclude = ['cropdbid', 'programDbId', 'locationName']

    # end class Meta

    
    def get_study_location(self, obj):

        return obj.locationDbId

    # end def get_study_location


    class Meta:

        model = Phenotype
        exclude = ['cropdbid', 'programDbId', 'locationDbId', 'locationName']

    # end class Meta


    def get_observationUnitXref(self, obj):

        x = ObservationUnitXref.objects.filter(observationunitdbid=obj.observationUnitDbId).all()
        return [ObservationUnitXrefSerializer(x).data for x in x]

    # end def get_observationUnitXref


    def get_observations(self, obj):

        o = Observation.objects.filter(observationUnit=obj.observationUnitDbId).all()
        return [ObservationSerializer(o).data for o in o]

    # end def get_observations


    def get_treatments(self, obj):

        o = Treatment.objects.filter(observationUnitDbId=obj.observationUnitDbId).all()
        return [TreatmentSerializer(o).data for o in o]

    # end def get_treatments

# end class PhenotypeSerializer
