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

    programDbId = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    abbreviation = models.CharField(max_length=100, blank=True, default='')
    objective = models.CharField(max_length=100, blank=True, default='')
    leadPerson = models.CharField(max_length=100, blank=True, default='')

# end class Program


class Crop(models.Model):

    data = models.CharField(max_length=100, blank=True, default='')

# end class Crop


class Map(models.Model):

    mapDbId = models.CharField(max_length=100, unique=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    species = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, blank=True, default='')
    unit = models.CharField(max_length=100, blank=True, default='')
    publishedDate = models.DateField()
    markerCount = models.CharField(max_length=100, blank=True, default='')
    comments = models.CharField(max_length=100, blank=True, default='')

# end class Map


class MapLinkage(models.Model):

    mapDbId = models.ForeignKey(Map, db_column='mapDbId', related_name='linkageGroups', on_delete=models.CASCADE, default='', to_field='mapDbId')
    markerDbId = models.CharField(max_length=100, blank=True, default='')
    markerName = models.CharField(max_length=100, blank=True, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    linkageGroupId = models.CharField(max_length=100, blank=True, default='')

# end class MapLinkage


class Location(models.Model):

    locationDbId = models.CharField(max_length=100, blank=True, default='')
    locationType = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    abbreviation = models.CharField(max_length=100, blank=True, default='')
    countryCode = models.CharField(max_length=100, blank=True, default='')
    countryName = models.CharField(max_length=100, blank=True, default='')
    latitude = models.CharField(max_length=100, blank=True, default='')
    longitude = models.CharField(max_length=100, blank=True, default='')
    altitude = models.CharField(max_length=100, blank=True, default='')
    instituteName = models.CharField(max_length=100, blank=True, default='')
    instituteAdress = models.CharField(max_length=100, blank=True, default='')

# end class Location


class Marker(models.Model):

    markerDbId = models.CharField(max_length=100, blank=True, default='')
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

    traitDbId = models.CharField(max_length=100, blank=True, default='')
    traitId = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    observationVariables = models.CharField(max_length=100, blank=True, default='')
    defaultValue = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.observationVariables = '; '.join(self.observationVariables)
        super(Trait, self).save(*args, **kwargs)

    # end def save

# end class Trait


class GAList(models.Model):

    attributeCategoryDbId = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')

# end class GAList


class GAAttrAvail(models.Model):

    attributeCategoryDbId = models.CharField(max_length=100, blank=True, default='')
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

    germplasmDbId = models.CharField(max_length=100, unique=True, default='')
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
    biologicalStatusOfAccessionCode = models.CharField(max_length=100, blank=True, default='')
    countryOfOriginCode = models.CharField(max_length=100, blank=True, default='')
    typeOfGermplasmStorageCode = models.CharField(max_length=100, blank=True, default='')
    genus = models.CharField(max_length=100, blank=True, default='')
    species = models.CharField(max_length=100, blank=True, default='')
    speciesAuthority = models.CharField(max_length=100, blank=True, default='')
    subtaxa = models.CharField(max_length=100, blank=True, default='')
    subtaxaAuthority = models.CharField(max_length=100, blank=True, default='')
    # TODO: this should be a FK, but it is a circular constraint!
    donors = models.CharField(max_length=100, blank=True, default='')
    acquisitionDate = models.CharField(max_length=100, blank=True, default='')
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
    parent1Id = models.CharField(max_length=100, blank=True, default='')
    # TODO: is this a foreign key?
    parent2Id = models.CharField(max_length=100, blank=True, default='')

# end class GPPedigree


class GPDonor(models.Model):

    germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmDbId', related_name='gpdonors-details+', on_delete=models.CASCADE, default='', to_field='germplasmDbId')
    donorAccessionNumber = models.CharField(max_length=100, blank=True, default='')
    donorInstituteCode = models.CharField(max_length=100, blank=True, default='')
    germplasmPUI = models.CharField(max_length=100, blank=True, default='')

# end class GPDonor


class MarkerProfile(models.Model):

    germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmDbId', related_name='mprofiles-details+', on_delete=models.CASCADE, default='', to_field='germplasmDbId')
    markerProfilesDbId = models.CharField(max_length=100, unique=True, default='')
    uniqueDisplayName = models.CharField(max_length=100, blank=True, default='')
    sampleDbId = models.CharField(max_length=100, blank=True, default='')
    extractDbId = models.CharField(max_length=100, blank=True, default='')
    studyDbId = models.CharField(max_length=100, blank=True, default='')
    analysisMethod = models.CharField(max_length=100, blank=True, default='')
    resultCount = models.CharField(max_length=100, blank=True, default='')

# end class MarkerProfile


class GPMarkerP(models.Model):

    germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmDbId', related_name='germplasmDbId_details', on_delete=models.CASCADE, default='', to_field='germplasmDbId')
    markerProfilesDbIds = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.markerProfilesDbIds = '; '.join(self.markerProfilesDbIds)

    # end def save

# end class GPMarkerP


class Trial(models.Model):

    trialDbId = models.CharField(max_length=100, unique=True, default='')
    trialName = models.CharField(max_length=100, blank=True, default='')
    programDbId = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    startDate = models.DateField()
    endDate = models.DateField()
    active = models.BooleanField()

# end class Trial


class Study(models.Model):
    
    studyDbId = models.CharField(max_length=100, unique=True, default='')
    studyName = models.CharField(max_length=100, blank=True, default='')
    locationName = models.CharField(max_length=100, blank=True, default='')
    trialDbId = models.ForeignKey(Trial, db_column='trialDbId', related_name='studies', on_delete=models.CASCADE, default='', to_field='trialDbId')

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
    sampleTimestamp = models.CharField(max_length=100, blank=True, default='')
    sampleType = models.CharField(max_length=100, blank=True, default='')
    tissueType = models.CharField(max_length=100, blank=True, default='')
    notes = models.CharField(max_length=100, blank=True, default='')
    studyName = models.CharField(max_length=100, blank=True, default='')
    season = models.CharField(max_length=100, blank=True, choices=SeasonType.choices())
    locationName = models.CharField(max_length=100, blank=True, default='')
    entryNumber = models.CharField(max_length=100, blank=True, default='')
    plotNumber = models.CharField(max_length=100, blank=True, default='')
    germplasmDbId = models.CharField(max_length=100, blank=True, default='')
    plantingTimestamp = models.DateTimeField()
    harvestTimestamp = models.DateTimeField()

# end class Sample


class Observation(models.Model):

    observationDbId = models.CharField(max_length=100, unique=True, default='')
    observationVariableDbId = models.CharField(max_length=100, blank=True, default='')
    observationVariableName = models.CharField(max_length=100, blank=True, default='')
    observationTimeStamp = models.DateTimeField()
    season = models.CharField(max_length=100, blank=True, default='')
    collector = models.CharField(max_length=100, blank=True, default='')
    value = models.CharField(max_length=100, blank=True, default='')

# end class Observation


class ObservationUnitXref(models.Model):

    ouXrefId = models.CharField(max_length=100, unique=True, default='')
    source = models.CharField(max_length=100, blank=True, default='')
    id = models.CharField(db_column='id_field', primary_key=True, max_length=100, default='')

# end class ObservationUnitXref


class Treatment(models.Model):

    treatmentId = models.CharField(max_length=100, unique=True, default='')
    factor = models.CharField(max_length=100, blank=True, default='')
    modality = models.CharField(max_length=100, blank=True, default='')

# end class Treatment


class Phenotype(models.Model):

    observationUnitDbId = models.CharField(max_length=100, blank=True, default='')
    observationLevel = models.CharField(max_length=100, blank=True, default='')
    observationLevels = models.CharField(max_length=100, blank=True, default='')
    plotNumber = models.CharField(max_length=100, blank=True, default='')
    plantNumber = models.CharField(max_length=100, blank=True, default='')
    blockNumber = models.CharField(max_length=100, blank=True, default='')
    replicate = models.CharField(max_length=100, blank=True, default='')
    observationUnitName = models.CharField(max_length=100, blank=True, default='')
    germplasmDbId = models.CharField(max_length=100, blank=True, default='')
    germplasmName = models.CharField(max_length=100, blank=True, default='')
    studyDbId = models.CharField(max_length=100, blank=True, default='')
    studyName = models.CharField(max_length=100, blank=True, default='')
    studyLocationDbId = models.CharField(max_length=100, blank=True, default='')
    studyLocation = models.CharField(max_length=100, blank=True, default='')
    programName = models.CharField(max_length=100, blank=True, default='')
    X = models.CharField(max_length=100, blank=True, default='')
    Y = models.CharField(max_length=100, blank=True, default='')
    entryType = models.CharField(max_length=100, blank=True, default='')
    entryNumber = models.CharField(max_length=100, blank=True, default='')
    treatments = models.ForeignKey(Treatment, db_column='treatments', related_name='treatments', on_delete=models.CASCADE, default='', to_field='treatmentId')    
    observationUnitXref = models.ForeignKey(ObservationUnitXref, db_column='observationUnitXrefs', related_name='observationUnitXref', on_delete=models.CASCADE, default='', to_field='ouXrefId')
    observations = models.ForeignKey(Observation, db_column='observations', related_name='observations', on_delete=models.CASCADE, default='', to_field='observationDbId')

# end class Phenotype


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
