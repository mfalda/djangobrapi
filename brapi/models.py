from django.db import models
from djangobrapi import settings


class Call(models.Model):

    cropdbid = models.ForeignKey('Crop', models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    calldbid = models.TextField(primary_key=True)
    call = models.TextField(blank=True, null=True)
    datatypes = models.TextField(blank=True, null=True)
    methods = models.TextField(blank=True, null=True)


    class Meta:

        managed = settings.IS_TESTING
        db_table = "call"
        ordering = ('calldbid',)

    # end class Meta


    def save(self, *args, **kwargs):

        self.datatypes = '; '.join(self.datatypes)
        self.methods = '; '.join(self.methods)
        super(Call, self).save(*args, **kwargs)

    # end def save

# end class Call


class Contact(models.Model):

    cropdbid = models.ForeignKey('Crop', models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    contactDbId = models.TextField(db_column='contactdbid', primary_key=True, default='')
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    orcid = models.TextField(blank=True, null=True)
    instituteName = models.TextField(db_column='institutename', blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'contact'
        ordering = ('contactDbId',)

    # end class Meta

# end class Contact


class Crop(models.Model):


    cropdbid = models.TextField(primary_key=True)
    commonname = models.TextField()

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'crop'

    # end class Meta

# end class Crop


class Donor(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    germplasmDbId = models.ForeignKey('Germplasm', models.DO_NOTHING, db_column='germplasmdbid', related_name='donors', blank=True, null=True)
    donorAccessionNumber = models.TextField(db_column='donoraccessionnumber', blank=True, null=True)
    donorInstituteCode = models.TextField(db_column='', blank=True, null=True)
    donorGermplasmPUI = models.TextField(db_column='', blank=True, null=True)
    donordbid = models.TextField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'donor'

    # end class Meta

# end class Donor


class Germplasm(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    germplasmDbId = models.TextField(db_column='germplasmdbid', primary_key=True, default='')
    germplasmPUI = models.TextField(db_column='germplasmpui', blank=True, null=True)
    germplasmName = models.TextField(db_column='germplasmname', default='')
    defaultDisplayName = models.TextField(db_column='defaultdisplayname', default='')
    accessionNumber = models.TextField(db_column='accessionnumber', blank=True, null=True)
    pedigree = models.TextField(blank=True, null=True)
    seedSource = models.TextField(db_column='seedsource', blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    instituteCode = models.TextField(db_column='institutecode', default='')
    instituteName = models.TextField(db_column='institutename', blank=True, null=True)
    biologicalStatusOfAccessionCode = models.TextField(db_column='biologicalstatusofaccessioncode', blank=True, null=True)
    countryOfOriginCode = models.TextField(db_column='countryoforigincode', blank=True, null=True)
    typeOfGermplasmStorageCode = models.TextField(db_column='typeofgermplasmstoragecode', blank=True, null=True)
    genus = models.TextField(blank=True, null=True)
    commonCropName = models.TextField(db_column='commoncropname', blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    speciesAuthority = models.TextField(db_column='speciesauthority', blank=True, null=True)
    subtaxa = models.TextField(db_column='subtaxa', blank=True, null=True)
    subtaxaAuthority = models.TextField(db_column='subtaxaauthority', blank=True, null=True)
    acquisitionDate = models.DateField(db_column='acquisitiondate', blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'germplasm'

    # end class Meta

# end class Germplasm


class GermplasmAttribute(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    attributeCategoryDbId = models.ForeignKey('GermplasmAttributeCategory', models.DO_NOTHING, db_column='attributecategorydbid', default='')
    attributeDbId = models.TextField(db_column='attributedbid', primary_key=True, default='')
    code = models.TextField(blank=True, null=True)
    uri = models.TextField(blank=True, null=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    datatype = models.TextField(blank=True, null=True)
    values = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'germplasm_attribute'

    # end class Meta

# end class GermplasmAttribute


class GermplasmAttributeCategory(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    attributeCategoryDbId = models.TextField(db_column='attributecategorydbid', primary_key=True, default='')
    name = models.TextField(db_column='attributecategoryname', blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'germplasm_attribute_category'

    # end class Meta

# end class GermplasmAttributeCategory


class GermplasmAttributeValue(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    germplasmDbId = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='germplasmdbid')
    attributeDbId = models.ForeignKey(GermplasmAttribute, models.DO_NOTHING, db_column='attributedbid', default='')
    determinedDate = models.DateField(db_column='determineddate', blank=True, null=True)
    value = models.TextField()
    attributeCode = models.TextField(db_column='attributecode', blank=True, null=True)
    attributeName = models.TextField(db_column='attributename', blank=True, null=True)
    germplasmattributevaluedbid = models.TextField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'germplasm_attribute_value'

    # end class Meta

# end class GermplasmAttributeValue


class Location(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    locationDbId = models.TextField(primary_key=True, db_column='locationdbid')
    type = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    abbreviation = models.TextField(blank=True, null=True)
    countryCode = models.TextField(blank=True, null=True, db_column='countrycode')
    countryName = models.TextField(blank=True, null=True, db_column='countryname')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    instituteName = models.TextField(blank=True, null=True, db_column='institutename')
    instituteAddress = models.TextField(blank=True, null=True, db_column='instituteaddress')

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'location'

    # end class Meta

# end class Location


class LocationAdditionalInfo(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    locationdbid = models.ForeignKey(Location, models.DO_NOTHING, db_column='locationdbid', related_name='additionalInfo', blank=True, null=True)
    key = models.TextField()
    value = models.TextField()
    locationaddinfodbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'location_additional_info'

    # end class Meta

# end class LocationAdditionalInfo


class Marker(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    markerDbId = models.IntegerField(db_column='markerdbid', primary_key=True)
    defaultDisplayName = models.TextField(db_column='defaultdisplayname', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    refAlt = models.TextField(db_column='refalt', blank=True, null=True)
    analysisMethods = models.TextField(db_column='analysismethods', blank=True, null=True)


    class Meta:

        managed = settings.IS_TESTING
        db_table = 'marker'
        ordering = ('markerDbId',)

    # end class Meta


    def save(self, *args, **kwargs):

        self.synonyms = '; '.join(self.synonyms)
        self.refalt = '; '.join(self.refalt)
        self.analysismethods = '; '.join(self.analysismethods)
        super(Marker, self).save(*args, **kwargs)

    # end def save

# end class Marker


class AlleleMatrix(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, default='')
    matrixDbId = models.IntegerField(db_column='matrixdbid', primary_key=True)
    description = models.CharField(max_length=100, blank=True, default='')
    lastUpdated = models.DateField(db_column='lastupdated')
    studyDbId = models.IntegerField(db_column='studydbid')


    class Meta:

        managed = settings.IS_TESTING
        ordering = ('matrixDbId',)
        db_table = 'allelematrix'

    # end class Meta

# end class AlleleMatrix


class AlleleMatrixSearch(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    allelematrixsearchDbId = models.IntegerField(db_column='allelematrixsearchdbid', primary_key=True)
    data = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.data = '; '.join(self.data)

    # end def save


    class Meta:

        managed = settings.IS_TESTING
        ordering = ('allelematrixsearchDbId',)
        db_table = 'allelematrixsearch'

    # end class Meta

# end class AlleleMatrixSearch


class Method(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    methodDbId = models.TextField(db_column='methoddbid', primary_key=True, default='')
    name = models.TextField(blank=True, null=True)
    classis = models.TextField(db_column='class', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    formula = models.TextField(blank=True, null=True)
    reference = models.TextField(blank=True, null=True)


    class Meta:

        managed = settings.IS_TESTING
        db_table = 'method'

    # end class Meta

# end class Method


class Observation(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    observationUnit = models.ForeignKey('ObservationUnit', models.DO_NOTHING, db_column='observationunitdbid', related_name='observations', blank=True, null=True)
    obsVariable = models.ForeignKey('ObservationVariable', models.DO_NOTHING, db_column='observationvariabledbid', related_name='obsVariable', blank=True, null=True)
    observationDbId = models.TextField(db_column='observationdbid', primary_key=True, default='')
    observationTimestamp = models.TextField(db_column='observationtimestamp', blank=True, null=True)
    seasonDbId = models.ForeignKey('Season', models.DO_NOTHING, db_column='seasondbid', blank=True, null=True)
    collector = models.TextField(blank=True, null=True)
    uploadedBy = models.TextField(db_column='uploadedby', blank=True, null=True)
    value = models.TextField(blank=True, null=True)


    class Meta:

        managed = settings.IS_TESTING
        ordering = ('observationDbId',)
        db_table = 'observation'

    # end class Meta

# end class Observation


class ObservationVariable(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    ontologyDbId = models.ForeignKey('Ontology', models.DO_NOTHING, db_column='ontologydbid')
    observationVariableDbId = models.TextField(db_column='observationvariabledbid', primary_key=True, default='')
    observationVariableName = models.TextField(db_column='observationvariablename', blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    contextOfUse = models.TextField(db_column='contextofuse', blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    xref = models.TextField(blank=True, null=True)
    institution = models.TextField(blank=True, null=True)
    scientist = models.TextField(blank=True, null=True)
    submissionTimestamp = models.DateTimeField(db_column='submissiontimestamp', blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    growthStage = models.TextField(blank=True, null=True)
    defaultValue = models.TextField(db_column='defaultvalue', blank=True, null=True)
    traitDbId = models.ForeignKey('Trait', models.DO_NOTHING, db_column='traitdbid', related_name='observationVariables', to_field='traitDbId', blank=True, null=True)
    methodDbId = models.ForeignKey(Method, models.DO_NOTHING, db_column='methoddbid', blank=True, null=True)
    scales = models.ForeignKey('Scale', models.DO_NOTHING, db_column='scaledbid', blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'observation_variable'

    # end class Meta

# end class ObservationVariable


class ObservationVariableDatatype(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    observationvariabledatatypedbid = models.IntegerField(db_column='observationvariabledatatypedbid', primary_key=True)
    data = models.TextField(blank=True, default='')


    class Meta:

        ordering = ('observationvariabledatatypedbid',)
        db_table = 'observation_variable_datatype'

        # end class Meta

# end class ObservationVariableDatatype


class Ontology(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    ontologyDbId = models.TextField(db_column='ontologydbid', primary_key=True, default='')
    ontologyName = models.TextField(db_column='ontologyname', blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    copyright = models.TextField(blank=True, null=True)
    license = models.TextField(blank=True, null=True)


    class Meta:

        managed = settings.IS_TESTING
        db_table = 'ontology'

    # end class Meta

# end class Ontology


class Pedigree(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    germplasmDbId = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='germplasmdbid', related_name='germplasm')
    pedigree = models.TextField()
    defaultDisplayName = models.TextField(db_column='defaultdisplayname', null=True, blank=True)
    parent1DbId = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='parent1dbid', related_name='parents1')
    parent2DbId = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='parent2dbid', related_name='parents2')
    pedigreeDbId = models.TextField(primary_key=True, db_column='pedigreedbid')

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'pedigree'

    # end class Meta

# end class Pedigree


class Program(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    programDbId = models.TextField(db_column='programdbid', primary_key=True, default='')
    name = models.TextField()
    abbreviation = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    leadPerson = models.TextField(db_column='leadperson', blank=True, null=True)


    class Meta:

        managed = settings.IS_TESTING
        db_table = 'program'

    # end class Meta

# end class Program


class ObservationUnit(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    studyDbId = models.ForeignKey('Study', models.DO_NOTHING, db_column='studydbid', default='', related_name='studies')
    germplasmDbId = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='germplasmdbid')
    observationUnitDbId = models.TextField(db_column='observationunitdbid', primary_key=True, default='')
    observationUnitName = models.TextField(db_column='name', default='')
    observationLevel = models.TextField(db_column='observationlevel', blank=True, null=True)
    observationLevels = models.TextField(db_column='observationlevels', blank=True, null=True)
    entryNumber = models.TextField(db_column='entrynumber', blank=True, null=True)
    entryType = models.TextField(db_column='entrytype', blank=True, null=True)
    plotNumber = models.TextField(db_column='plotnumber', blank=True, null=True)
    blockNumber = models.TextField(db_column='blocknumber', blank=True, null=True)
    plantNumber = models.TextField(db_column='plantnumber', blank=True, null=True)
    X = models.TextField(db_column='x', blank=True, null=True)
    Y = models.TextField(db_column='y', blank=True, null=True)
    replicate = models.TextField(blank=True, null=True)
    programDbId = models.ForeignKey(Program, models.DO_NOTHING, db_column='programdbid')


    class Meta:

        managed = settings.IS_TESTING
        db_table = 'observation_unit'

    # end class Meta

# end class ObservationUnit


class ObservationUnitAdditionalInfo(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    observationunitdbid = models.ForeignKey(ObservationUnit, models.DO_NOTHING, db_column='trialdbid', related_name='observationunitdbid', blank=True, null=True)
    key = models.TextField()
    value = models.TextField()
    observationunitadditionalinfodbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'observation_unit_additional_info'

        # end class Meta

# end class ObservationUnitAdditionalInfo


class ObservationUnitXref(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    observationunitdbid = models.ForeignKey(ObservationUnit, models.DO_NOTHING, db_column='observationunitdbid', related_name='observationUnitXref')
    source = models.TextField()
    identifier = models.TextField()
    observationunitxrefdbid = models.TextField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'observation_unit_xref'

    # end class Meta

# end class ObservationUnitXref


class ValidValue(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    min = models.IntegerField(db_column='min')
    max = models.IntegerField(db_column='max')
    validValueDbId = models.TextField(db_column='validvaluedbid', primary_key=True)
    categories = models.TextField()


    class Meta:

        managed = settings.IS_TESTING
        db_table = 'validvalue'

    # end class Meta

# end class ValidValue


class Scale(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    scaleDbId = models.TextField(db_column='scaledbid', primary_key=True, default='')
    name = models.TextField(default='')
    datatypeDbId = models.ForeignKey(ObservationVariableDatatype, models.DO_NOTHING, db_column='data', blank=True, null=True)
    decimalPlaces = models.IntegerField(db_column='decimalplaces', default=0)
    xref = models.TextField(blank=True, null=True)
    validValues = models.ForeignKey(ValidValue, models.DO_NOTHING, db_column='vvalueid', blank=True, null=True)
    defaultValue = models.TextField(db_column='', blank=True, null=True)


    class Meta:

        managed = settings.IS_TESTING
        db_table = 'scale'

    # end class Meta

# end class Scale


class Season(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    seasonDbId = models.TextField(db_column='seasondbid', primary_key=True, default='')
    year = models.TextField(blank=True, null=True)
    season = models.TextField(blank=True, null=True)


    class Meta:

        managed = settings.IS_TESTING
        db_table = 'season'

    # end class Meta

# end class Season


class Trial(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    programDbId = models.ForeignKey(Program, models.DO_NOTHING, db_column='programdbid', blank=True, null=True)
    trialDbId = models.TextField(db_column='trialdbid', primary_key=True, default='')
    trialName = models.TextField(db_column='name', default='')
    startDate = models.DateField(db_column='startdate', blank=True, null=True)
    endDate = models.DateField(db_column='enddate', blank=True, null=True)
    active = models.NullBooleanField()
    datasetAuthorshipLicence = models.TextField(db_column='datasetauthorshiplicence', blank=True, null=True)
    datasetAuthorshipDatasetPUI = models.TextField(db_column='datasetauthorshipdatasetpui', blank=True, null=True)


    class Meta:

        managed = settings.IS_TESTING
        db_table = 'trial'
        ordering = ('trialDbId',)

    # end class Meta

# end class Trial


class StudyType(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    name = models.TextField(primary_key=True)
    description = models.TextField(blank=True, null=True)


    class Meta:

        managed = settings.IS_TESTING
        db_table = 'study_type'

    # end class Meta

# end class StudyType


class Study(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    trialDbId = models.ForeignKey(Trial, models.DO_NOTHING, db_column='trialdbid', related_name='studies')
    locationDbId = models.ForeignKey(Location, models.DO_NOTHING, db_column='locationdbid', related_name='locations', blank=True, null=True)
    studyType = models.ForeignKey(StudyType, models.DO_NOTHING, db_column='studytype', related_name='studies', blank=True, null=True, default='')
    studyDbId = models.TextField(db_column='studydbid', primary_key=True, default='')
    studyName = models.TextField(default='', db_column='studyname')
    studyDescription = models.TextField(db_column='description', blank=True, null=True)
    startDate = models.DateField(db_column='startdate', blank=True, null=True)
    endDate = models.DateField(db_column='enddate', blank=True, null=True)
    active = models.NullBooleanField()
    license = models.TextField(blank=True, null=True)
    lastUpdateVersion = models.TextField(db_column='lastupdateversion', blank=True, null=True)
    lastUpdateTimestamp = models.DateTimeField(db_column='lastupdatetimestamp', blank=True, null=True)


    class Meta:

        managed = settings.IS_TESTING
        db_table = 'study'
        ordering = ('studyDbId',)

    # end class Meta

# end class Study


class MarkerProfile(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmdbid', related_name='mprofiles-details+', on_delete=models.CASCADE, default='')
    markerprofileDbId = models.IntegerField(db_column='markerprofiledbid', primary_key=True)
    uniqueDisplayName = models.CharField(db_column='uniquedisplayname', max_length=100, blank=True, default='')
    sampleDbId = models.IntegerField(db_column='sampledbid')
    extractDbId = models.IntegerField(db_column='extractdbid')
    studyDbId = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid', blank=True, null=True)
    analysisMethod = models.CharField(db_column='analysismethod', max_length=100, blank=True, default='')
    resultCount = models.IntegerField(db_column='resultcount')


    class Meta:

        managed = settings.IS_TESTING
        ordering = ('markerprofileDbId',)
        db_table = 'markerprofile'

    # end class Meta

# end class MarkerProfile


class MarkerProfilesData(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    markerDbId = models.ForeignKey(Marker, models.DO_NOTHING, db_column='markerdbid', blank=True, null=True)
    markerprofileDbId = models.ForeignKey(MarkerProfile, models.DO_NOTHING, db_column='markerprofiledbid', blank=True, null=True)
    alleleCall = models.CharField(max_length=100, db_column='allelecall', blank=True, default='')
    markerprofilesdatadbid = models.TextField(primary_key=True)

    def save(self, *args, **kwargs):

        self.data = '; '.join(self.data)

    # end def save


    class Meta:

        ordering = ('markerprofilesdatadbid',)
        db_table = 'markerprofilesdata'

    # end class Meta

# end class MarkerProfilesData


# class GermplasmMarkerProfile(models.Model):
#
#     germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmdbid', related_name='germplasmDbId_details', on_delete=models.CASCADE, default='', to_field='germplasmdbid')
#     markerProfilesDbIds = models.OneToOneField(MarkerProfile, db_column='markerprofilesdbids', related_name='markerProfilesDbId_details', on_delete=models.CASCADE, default='', to_field='markerprofileDbId')
#
#     class Meta:
#
#         ordering = ('id',)
#
#     # end class Meta
#
# # end class GermplasmMarkerProfile


class Sample(models.Model):

    cropDbId = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    sampleDbId = models.TextField(db_column='sampledbid', primary_key=True)
    studyDbId = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid', blank=True, null=True)
    locationDbId = models.ForeignKey(Location, models.DO_NOTHING, db_column='locationdbid', blank=True, null=True)
    plotId = models.CharField(db_column='plotid', max_length=100, blank=True, default='')
    plantId = models.CharField(db_column='plantid', max_length=100, blank=True, default='')
    sampleId = models.CharField(db_column='sampleid', max_length=100, blank=True, default='')
    observationUnitDbId = models.ForeignKey(ObservationUnit, models.DO_NOTHING, db_column='observationunitdbid', blank=True, null=True)
    takenBy = models.CharField(db_column='takenby', max_length=100, blank=True, default='')
    sampleTimestamp = models.DateTimeField(db_column='sampletimestamp', max_length=100, blank=True, default='')
    sampleType = models.CharField(db_column='sampletype', max_length=100, blank=True, default='')
    tissueType = models.CharField(db_column='tissuetype', max_length=100, blank=True, default='')
    notes = models.CharField(max_length=100, blank=True, default='')
    seasonDbId = models.ForeignKey(Season, models.DO_NOTHING, db_column='seasondbid', blank=True, null=True)
    germplasmDbId = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='germplasmdbid', blank=True, null=True)
    plantingTimestamp = models.DateTimeField(db_column='plantingtimestamp')
    harvestTimestamp = models.DateTimeField(db_column='harvesttimestamp')


    class Meta:

        ordering = ('sampleDbId',)
        managed = settings.IS_TESTING
        db_table = 'sample'

    # end class Meta

# end class Sample


class StudyAdditionalInfo(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    studyDbId = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid', blank=True, null=True, default='')
    key = models.TextField()
    value = models.TextField()
    studyadditionalinfodbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'study_additional_info'

    # end class Meta

# end class StudyAdditionalInfo


class StudyContact(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    studydbid = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid')
    contactdbid = models.ForeignKey(Contact, models.DO_NOTHING, db_column='contactdbid')
    studycontactdbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'study_contact'

    # end class Meta

# end class StudyContact


class StudyDataLink(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    studydbid = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid', related_name='dataLinks')
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    url = models.TextField()
    studydatalinkdbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'study_data_link'

    # end class Meta

# end class StudyDataLink


class StudyObservationLevel(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    studyobservationleveldbid = models.IntegerField(primary_key=True)
    data = models.TextField(blank=True, default='')


    class Meta:

        ordering = ('studyobservationleveldbid',)
        db_table = 'study_observation_level'

    # end class Meta

# end class StudyObservationLevel


class StudySeason(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    studyDbId = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid', related_name='seasons', default='')
    seasonDbId = models.ForeignKey(Season, models.DO_NOTHING, db_column='seasondbid', related_name='seasons1', default='')
    studyseasondbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'study_season'

    # end class Meta

# end class StudySeason


class TaxonXref(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    taxondbid = models.TextField(primary_key=True)
    source = models.TextField()
    rank = models.TextField(blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'taxon_xref'

    # end class Meta

# end class TaxonXref


class TaxonXrefGermplasm(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    taxondbid = models.ForeignKey(TaxonXref, models.DO_NOTHING, db_column='taxondbid', related_name='taxa', blank=True, null=True)
    germplasmDbId = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='germplasmdbid', related_name='germplasm1', blank=True, null=True)
    taxonxrefgermplasmdbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'taxon_xref_germplasm'

    # end class Meta

# end class TaxonXrefGermplasm


class Trait(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    traitDbId = models.TextField(primary_key=True, db_column='traitdbid')
    traitId = models.TextField(db_column='traitid', blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    classis = models.TextField(blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    mainAbbreviation = models.TextField(db_column='mainabbreviation', blank=True, null=True)
    alternativeAbbreviations = models.TextField(db_column='alternativeabbreviations', blank=True, null=True)
    entity = models.TextField(blank=True, null=True)
    attribute = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    xref = models.TextField(blank=True, null=True)
    defaultValue = models.CharField(db_column='defaultvalue', max_length=100, blank=True, default='')

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'trait'

    # end class Meta

# end class Trait


class Treatment(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    observationUnitDbId = models.ForeignKey(ObservationUnit, models.DO_NOTHING, db_column='observationunitdbid')
    factor = models.TextField()
    modality = models.TextField()
    treatmentdbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'treatment'

    # end class Meta

# end class Treatment


class TrialAdditionalInfo(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    trialdbid = models.ForeignKey(Trial, models.DO_NOTHING, db_column='trialdbid', related_name='additionalInfo', blank=True, null=True)
    key = models.TextField()
    value = models.TextField()
    trialadditionalinfodbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'trial_additional_info'

    # end class Meta

# end class TrialAdditionalInfo


class TrialContact(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    trialdbid = models.ForeignKey(Trial, models.DO_NOTHING, db_column='trialdbid', related_name='contacts', blank=True, null=True)
    contactdbid = models.ForeignKey(Contact, models.DO_NOTHING, db_column='contactdbid', related_name='contacts1', blank=True, null=True)
    trialcontactdbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'trial_contact'

    # end class Meta

# end class TrialContact


class Map(models.Model):

    mapDbId = models.IntegerField(primary_key=True, default='')
    name = models.CharField(max_length=100, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=100, blank=True, null=True)
    publishedDate = models.DateField(blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)


    class Meta:

       ordering = ('mapDbId',)
       managed = settings.IS_TESTING
       db_table = 'map'

    # end class Meta

# end class Map


class MapLinkage(models.Model):

    mapDbId = models.ForeignKey(Map, db_column='mapDbId', related_name='linkageGroups', on_delete=models.CASCADE, default='', to_field='mapDbId')
    markerDbId = models.IntegerField()
    markerName = models.CharField(max_length=100, blank=True, null=True)
    location = models.IntegerField()
    linkageGroupId = models.IntegerField()


    class Meta:

        ordering = ('id',)
        managed = settings.IS_TESTING
        db_table = 'map_linkage'

    # end class Meta

# end class MapLinkage


class Phenotype(models.Model):

    cropdbid = models.TextField(db_column='cropdbid')
    observationUnitDbId = models.TextField(db_column='observationunitdbid', primary_key=True)
    observationUnitName = models.TextField(db_column='observationunitname')
    entryNumber = models.TextField(db_column='entrynumber')
    entryType = models.TextField(db_column='entrytype')
    studyDbId = models.TextField(db_column='studydbid')
    studyName = models.TextField(db_column='studyname')
    locationDbId = models.TextField(db_column='locationdbid')
    locationName = models.TextField(db_column='locationname')
    observationLevel = models.TextField(db_column='observationlevel')
    observationLevels = models.TextField(db_column='observationlevels')
    plotNumber = models.TextField(db_column='plotnumber')
    plantNumber = models.TextField(db_column='plantnumber')
    blockNumber = models.TextField(db_column='blocknumber')
    replicate = models.TextField()
    programName = models.TextField(db_column='programname')
    germplasmDbId = models.TextField(db_column='germplasmdbid')
    germplasmName = models.TextField(db_column='germplasmname')
    X = models.TextField(db_column='x')
    Y = models.TextField(db_column='y')
    treatmentDbId = models.TextField(db_column='treatmentdbid')
    observationUnitXref = models.TextField(db_column='observationunitxrefdbid')
    observationVariableDbId = models.TextField(db_column='observationvariabledbid')
    seasonDbId = models.TextField(db_column='seasondbid')
    season = models.TextField()
    observationDbId = models.TextField(db_column='observationdbid')
    observationTimestamp = models.TextField(db_column='observationtimestamp')


    class Meta:

        managed = False
        db_table = 'phenotype'

    # end class Meta

# end class Phenotype
