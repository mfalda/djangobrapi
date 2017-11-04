from django.db import models
from enum import Enum


class Call(models.Model):

    call = models.CharField(max_length=100, blank=True, default='')
    datatypes = models.CharField(max_length=100, blank=True, default='')
    methods = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.datatypes = '; '.join(self.datatypes)
        self.methods = '; '.join(self.methods)
        super(Call, self).save(*args, **kwargs)

    # end def save

# end class Call


class Program(models.Model):

    programDbId = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, default='')
    abbreviation = models.CharField(max_length=100, blank=True, default='')
    objective = models.CharField(max_length=100, blank=True, default='')
    leadPerson = models.CharField(max_length=100, blank=True, default='')

# end class Program


class Crop(models.Model):

    data = models.CharField(max_length=100, blank=True, default='')

# end class Crop


class Map(models.Model):

    mapDbId = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, blank=True, default='')
    species = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, blank=True, default='')
    unit = models.CharField(max_length=100, blank=True, default='')
    publishedDate = models.DateField()
    markerCount = models.IntegerField()
    comments = models.CharField(max_length=100, blank=True, default='')

# end class Map


class MapLinkage(models.Model):

    mapDbId = models.ForeignKey(Map, db_column='mapDbId', related_name='linkageGroups', on_delete=models.CASCADE, default='', to_field='mapDbId')
    markerDbId = models.IntegerField()
    markerName = models.CharField(max_length=100, blank=True, default='')
    location = models.IntegerField()
    linkageGroupId = models.IntegerField()

# end class MapLinkage


class Location(models.Model):

    locationDbId = models.CharField(max_length=100, blank=True, default='')
    locationType = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    abbreviation = models.CharField(max_length=100, blank=True, default='')
    countryCode = models.CharField(max_length=100, blank=True, default='')
    countryName = models.CharField(max_length=100, blank=True, default='')
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.CharField(max_length=100, blank=True, default='')
    instituteName = models.CharField(max_length=100, blank=True, default='')
    instituteAdress = models.CharField(max_length=100, blank=True, default='')

# end class Location


class Marker(models.Model):

    markerDbId = models.IntegerField()
    defaultDisplayName = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, blank=True, default='')
    synonyms = models.CharField(max_length=100, blank=True, default='')
    refAlt = models.CharField(max_length=100, blank=True, default='')
    analysisMethods = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.synonyms = '; '.join(self.synonyms)
        self.refAlt = '; '.join(self.refAlt)
        self.analysisMethods = '; '.join(self.analysisMethods)
        super(Marker, self).save(*args, **kwargs)

    # end def save

# end class Marker


class Trait(models.Model):

    traitDbId = models.IntegerField()
    traitId = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    observationVariables = models.CharField(max_length=100, blank=True, default='')
    defaultValue = models.IntegerField(null=True)

    def save(self, *args, **kwargs):

        self.observationVariables = '; '.join(self.observationVariables)
        super(Trait, self).save(*args, **kwargs)

    # end def save

# end class Trait


class GAList(models.Model):

    attributeCategoryDbId = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, default='')

# end class GAList


class GAAttrAvail(models.Model):

    attributeCategoryDbId = models.IntegerField()
    code = models.CharField(max_length=100, blank=True, default='')
    uri = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    datatype = models.CharField(max_length=100, blank=True, default='')
    values = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.values = '; '.join(self.values)
        super(GAAttrAvail, self).save(*args, **kwargs)

    # end def save

# end class GAAttrAvail


class GermplasmAttr(models.Model):

    # TODO: this should be a foreign key
    germplasmDbId = models.CharField(max_length=100, blank=True, default='')
    attributeDbId = models.CharField(max_length=100, blank=True, default='')
    attributeName = models.CharField(max_length=100, blank=True, default='')
    attributeCode = models.CharField(max_length=100, blank=True, default='')
    value = models.CharField(max_length=100, blank=True, default='')
    dateDetermined = models.DateField()

# end class GermplasmAttr


class Germplasm(models.Model):

    germplasmDbId = models.IntegerField(unique=True)
    defaultDisplayName = models.CharField(max_length=100, blank=True, default='')
    accessionNumber = models.CharField(max_length=100, blank=True, default='')
    germplasmName = models.CharField(max_length=100, blank=True, default='')
    germplasmPUI = models.CharField(max_length=100, blank=True, default='')
    pedigree = models.CharField(max_length=100, blank=True, default='')
    germplasmSeedSource = models.CharField(max_length=100, blank=True, default='')
    synonyms = models.CharField(max_length=100, blank=True, default='')
    commonCropName = models.CharField(max_length=100, blank=True, default='')
    instituteCode = models.CharField(max_length=100, blank=True, default='')
    instituteName = models.CharField(max_length=100, blank=True, default='')
    biologicalStatusOfAccessionCode = models.IntegerField()
    countryOfOriginCode = models.CharField(max_length=100, blank=True, default='')
    typeOfGermplasmStorageCode = models.IntegerField()
    genus = models.CharField(max_length=100, blank=True, default='')
    species = models.CharField(max_length=100, blank=True, default='')
    speciesAuthority = models.CharField(max_length=100, blank=True, default='')
    subtaxa = models.CharField(max_length=100, blank=True, default='')
    subtaxaAuthority = models.CharField(max_length=100, blank=True, default='')
    # TODO: this should be a FK, but it is a circular constraint!
    donors = models.CharField(max_length=100, blank=True, default='')
    acquisitionDate = models.DateField()
    # TODO: represent as a list of objects
    taxonIds = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.synonyms = '; '.join(self.synonyms)
        self.typeOfGermplasmStorageCode = '; '.join(self.typeOfGermplasmStorageCode)
        self.donors = '; '.join(self.donors)
        super(Germplasm, self).save(*args, **kwargs)

    # end def save

# end class Germplasm


class GPPedigree(models.Model):

    germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmDbId', related_name='gppedigrees-details+', on_delete=models.CASCADE, default='', to_field='germplasmDbId')
    defaultDisplayName = models.CharField(max_length=100, blank=True, default='')
    pedigree = models.CharField(max_length=100, blank=True, default='')
    # TODO: is this a foreign key?
    parent1Id = models.IntegerField()
    # TODO: is this a foreign key?
    parent2Id = models.IntegerField()

# end class GPPedigree


class GPDonor(models.Model):

    germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmDbId', related_name='gpdonors-details+', on_delete=models.CASCADE, default='', to_field='germplasmDbId')
    donorAccessionNumber = models.CharField(max_length=100, blank=True, default='')
    donorInstituteCode = models.CharField(max_length=100, blank=True, default='')
    germplasmPUI = models.CharField(max_length=100, blank=True, default='')

# end class GPDonor


class MarkerProfile(models.Model):

    germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmDbId', related_name='mprofiles-details+', on_delete=models.CASCADE, default='', to_field='germplasmDbId')
    markerProfilesDbId = models.IntegerField()
    uniqueDisplayName = models.CharField(max_length=100, blank=True, default='')
    sampleDbId = models.IntegerField()
    extractDbId = models.IntegerField()
    studyDbId = models.IntegerField()
    analysisMethod = models.CharField(max_length=100, blank=True, default='')
    resultCount = models.IntegerField()

# end class MarkerProfile


class GPMarkerP(models.Model):

    germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmDbId', related_name='germplasmDbId_details', on_delete=models.CASCADE, default='', to_field='germplasmDbId')
    markerProfilesDbIds = models.IntegerField()

    def save(self, *args, **kwargs):

        self.markerProfilesDbIds = '; '.join(self.markerProfilesDbIds)

    # end def save

# end class GPMarkerP


class Trial(models.Model):

    trialDbId = models.IntegerField(unique=True)
    trialName = models.CharField(max_length=100, blank=True, default='')
    programDbId = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, default='')
    startDate = models.DateField()
    endDate = models.DateField()
    active = models.BooleanField()

# end class Trial


class Study(models.Model):
    
    studyDbId = models.IntegerField()
    studyName = models.CharField(max_length=100, blank=True, default='')
    trialDbId = models.ForeignKey(Trial, db_column='trialDbId', related_name='studies', on_delete=models.CASCADE, default='', to_field='trialDbId')
    locationName = models.CharField(max_length=100, blank=True, default='')
    trialName = models.CharField(max_length=100, blank=True, default='')
    studyType = models.CharField(max_length=100, blank=True, default='')
    seasons = models.CharField(max_length=100, blank=True, default='')
    locationDbId = models.IntegerField()
    locationName = models.CharField(max_length=100, blank=True, default='')
    programDbId = models.IntegerField()
    programName = models.CharField(max_length=100, blank=True, default='')
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    active = models.BooleanField()
    contactDbId = models.CharField(max_length=100, blank=True, default='')
    dataLinks = models.ForeignKey(Trial, db_column='dataLinks', related_name='studies1', on_delete=models.CASCADE, default='', to_field='trialDbId')
    lastUpdate = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.contactDbId = '; '.join(self.contactDbId)

    # end def save
    
# end class Study


class ChoiceEnum(Enum):

    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)
    # end def choices

# end class ChoiceEnum

class SeasonType(ChoiceEnum):

    SPRING = 'Spring'
    SUMMER = 'Summer'
    AUTUMN = 'Autumn'
    WINTER = 'Winter'

# end class SeasonType

class Sample(models.Model):

    studyDbId = models.CharField(max_length=100, blank=True, default='')
    locationDbId = models.CharField(max_length=100, blank=True, default='')
    plotId = models.CharField(max_length=100, blank=True, default='')
    plantId = models.CharField(max_length=100, blank=True, default='')
    sampleId = models.CharField(max_length=100, blank=True, default='')
    takenBy = models.CharField(max_length=100, blank=True, default='')
    sampleTimestamp = models.DateTimeField(max_length=100, blank=True, default='')
    sampleType = models.CharField(max_length=100, blank=True, default='')
    tissueType = models.CharField(max_length=100, blank=True, default='')
    notes = models.CharField(max_length=100, blank=True, default='')
    studyName = models.CharField(max_length=100, blank=True, default='')
    season = models.CharField(max_length=100, blank=True, choices=SeasonType.choices())
    locationName = models.CharField(max_length=100, blank=True, default='')
    entryNumber = models.IntegerField()
    plotNumber = models.IntegerField()
    germplasmDbId = models.IntegerField()
    plantingTimestamp = models.DateTimeField()
    harvestTimestamp = models.DateTimeField()

# end class Sample


class ObservationUnitXref(models.Model):

    ouXrefId = models.IntegerField()
    source = models.CharField(max_length=100, blank=True, default='')
    id = models.CharField(db_column='id_field', primary_key=True, max_length=100, default='')

# end class ObservationUnitXref


class Treatment(models.Model):

    treatmentId = models.IntegerField()
    factor = models.CharField(max_length=100, blank=True, default='')
    modality = models.CharField(max_length=100, blank=True, default='')

# end class Treatment


class Datatype(models.Model):
    
    data = models.CharField(max_length=100, blank=True, default='')

# end class Datatype


class Ontology(models.Model):
    
    ontologyDbId = models.CharField(max_length=100, blank=True, default='')
    ontologyName = models.CharField(max_length=100, blank=True, default='')
    authors = models.CharField(max_length=100, blank=True, default='')
    version = models.CharField(max_length=100, blank=True, default='')
    copyright = models.CharField(max_length=100, blank=True, default='')
    licence = models.CharField(max_length=100, blank=True, default='')

# end class Ontology


class StudySeason(models.Model):
    
    seasonDbId = models.IntegerField(primary_key=True, db_column='id')
    season = models.CharField(max_length=100, blank=True, default='')
    year = models.IntegerField()

# end class StudySeason


class StudyType(models.Model):
    
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')

# end class StudyType


class StudyObsLevel(models.Model):
    
    data = models.CharField(max_length=100, blank=True, default='')

# end class StudyObsLevel


class StudyPlot(models.Model):
    
    studyDbId = models.IntegerField()
    observationUnitDbId = models.IntegerField()
    observationUnitName = models.CharField(max_length=100, blank=True, default='')
    observationLevel = models.CharField(max_length=100, blank=True, default='')
    replicate = models.IntegerField()
    germplasmDbId = models.IntegerField()
    germplasmName = models.CharField(max_length=100, blank=True, default='')
    blockNumber = models.IntegerField()
    X = models.IntegerField()
    Y = models.IntegerField()
    entryType = models.CharField(max_length=100, blank=True, default='')

# end class StudyPlot


class AlleleMatrix(models.Model):
    
    name = models.CharField(max_length=100, blank=True, default='')
    matrixDbId = models.IntegerField()
    description = models.CharField(max_length=100, blank=True, default='')
    lastUpdated = models.DateField()
    studyDbId = models.IntegerField()

# end class AlleleMatrix


class AlleleMSearch(models.Model):
    
    data = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
    
        self.data = '; '.join(self.data)

    # end def save
    
# end class AlleleMSearch


class MarkerProfilesData(models.Model):
    
    germplasmDbId = models.IntegerField()
    uniqueDisplayName = models.CharField(max_length=100, blank=True, default='')
    extractDbId = models.IntegerField()
    markerprofileDbId = models.IntegerField()
    analysisMethod = models.CharField(max_length=100, blank=True, default='')
    data = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.data = '; '.join(self.data)

    # end def save

# end class MarkerProfilesData


class ObsVValue(models.Model):
    
    min = models.IntegerField()
    max = models.IntegerField()
    categories = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.categories = '; '.join(self.categories)

    # end def save

# end class ObsVValue


class ObsMethod(models.Model):
    
    methodDbId = models.CharField(max_length=100, unique=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    classe = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    formula = models.CharField(max_length=100, blank=True, default='')
    reference = models.CharField(max_length=100, blank=True, default='')

# end class ObsMethod


class ObsScale(models.Model):
    
    scaleDbId = models.CharField(max_length=100, unique=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    datatype = models.CharField(max_length=100, blank=True, default='')
    decimalPlaces = models.CharField(max_length=100, blank=True, default='')
    xref = models.CharField(max_length=100, blank=True, default='')
    validValues = models.ForeignKey(ObsVValue, db_column='validValues', related_name='validValues', on_delete=models.CASCADE, default='', to_field='id')

# end class ObsScale


class ObsTrait(models.Model):

    traitDbId = models.CharField(max_length=100, unique=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    classe = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    synonyms = models.CharField(max_length=100, blank=True, default='')
    mainAbbreviation = models.CharField(max_length=100, blank=True, default='')
    alternativeAbbreviations = models.CharField(max_length=100, blank=True, default='')
    entity = models.CharField(max_length=100, blank=True, default='')
    attribute = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=100, blank=True, default='')
    xref = models.CharField(max_length=100, blank=True, default='')
    uniqueDisplayName = models.CharField(max_length=100, blank=True, default='')
    extractDbId = models.IntegerField(null=True)
    markerprofileDbId = models.IntegerField(null=True)
    analysisMethod = models.CharField(max_length=100, blank=True, default='')
    data = models.CharField(max_length=100, blank=True, default='')

# end class ObsTrait


class ObsVariable(models.Model):
    
    observationVariableDbId = models.CharField(max_length=100, unique=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    ontologyDbId = models.CharField(max_length=100, blank=True, default='')
    ontologyName = models.CharField(max_length=100, blank=True, default='')
    synonyms = models.CharField(max_length=100, blank=True, default='')
    contextOfUse = models.CharField(max_length=100, blank=True, default='')
    growthStage = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=100, blank=True, default='')
    xref = models.CharField(max_length=100, blank=True, default='')
    institution = models.CharField(max_length=100, blank=True, default='')
    scientist = models.CharField(max_length=100, blank=True, default='')
    date = models.DateField()
    language = models.CharField(max_length=100, blank=True, default='')
    crop = models.CharField(max_length=100, blank=True, default='')
    defaultValue = models.CharField(max_length=100, blank=True, default='')
    trait = models.ForeignKey(ObsTrait, db_column='trait', related_name='trait', on_delete=models.CASCADE, default='', to_field='traitDbId')
    method = models.ForeignKey(ObsMethod, db_column='method', related_name='method', on_delete=models.CASCADE, default='', to_field='methodDbId')
    scale = models.ForeignKey(ObsScale, db_column='scale', related_name='scale', on_delete=models.CASCADE, default='', to_field='scaleDbId')

# end class ObsVariable


class Observation(models.Model):

    observationDbId = models.IntegerField(unique=True)
    observationVariableDbId = models.ForeignKey(ObsVariable, db_column='observations', related_name='observation_variables', on_delete=models.CASCADE, default='', to_field='observationVariableDbId')
    observationVariableName = models.CharField(max_length=100, blank=True, default='')
    observationTimeStamp = models.DateTimeField()
    season = models.CharField(max_length=100, blank=True, default='')
    collector = models.CharField(max_length=100, blank=True, default='')
    value = models.IntegerField()

# end class Observation
    
    
class Phenotype(models.Model):

    observationUnitDbId = models.CharField(max_length=100, blank=True, default='')
    observationLevel = models.CharField(max_length=100, blank=True, default='')
    observationLevels = models.CharField(max_length=100, blank=True, default='')
    plotNumber = models.CharField(max_length=100, blank=True, default='')
    plantNumber = models.IntegerField(null=True)
    blockNumber = models.IntegerField(null=True)
    replicate = models.IntegerField(null=True)
    observationUnitName = models.CharField(max_length=100, blank=True, default='')
    germplasmDbId = models.CharField(max_length=100, blank=True, default='')
    germplasmName = models.CharField(max_length=100, blank=True, default='')
    studyDbId = models.CharField(max_length=100, blank=True, default='')
    studyName = models.CharField(max_length=100, blank=True, default='')
    studyLocationDbId = models.CharField(max_length=100, blank=True, default='')
    studyLocation = models.CharField(max_length=100, blank=True, default='')
    programName = models.CharField(max_length=100, blank=True, default='')
    X = models.IntegerField(null=True)
    Y = models.IntegerField(null=True)
    entryType = models.CharField(max_length=100, blank=True, default='')
    entryNumber = models.IntegerField(null=True)
    treatments = models.IntegerField(null=True)
    observationUnitXref = models.IntegerField(null=True)
    observations = models.ForeignKey(Observation, db_column='observations', related_name='observations', on_delete=models.CASCADE, default='', to_field='observationDbId')

# end class Phenotype
    
    
class StudyObsUnit(models.Model):
    
    studyDbId = models.IntegerField()
    observationDbId = models.IntegerField(null=True)
    observationUnitDbId = models.IntegerField(null=True)
    observationUnitName = models.CharField(max_length=100, blank=True, default='')
    observationLevel = models.CharField(max_length=100, blank=True, default='')
    observationVariableDbId = models.IntegerField(null=True)
    observationVariableName = models.CharField(max_length=100, blank=True, default='')
    observationTimestamp = models.DateTimeField()
    uploadedBy = models.CharField(max_length=100, blank=True, default='')
    operator = models.CharField(max_length=100, blank=True, default='')
    germplasmDbId = models.IntegerField(null=True)
    germplasmName = models.IntegerField(null=True)
    value = models.IntegerField(null=True)
    
# end class StudyObsUnit