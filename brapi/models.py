from django.db import models
from tutorial import settings

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
    contactdbid = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    orcid = models.TextField(blank=True, null=True)
    institutename = models.TextField(blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'contact'

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
    germplasmdbid = models.ForeignKey('Germplasm', models.DO_NOTHING, db_column='germplasmdbid', blank=True, null=True)
    donoraccessionnumber = models.TextField(blank=True, null=True)
    donorinstitutecode = models.TextField(blank=True, null=True)
    donorgermplasmpui = models.TextField(blank=True, null=True)
    donordbid = models.TextField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'donor'

    # end class Meta

# end class Donor


class Germplasm(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    germplasmdbid = models.TextField(primary_key=True)
    germplasmpui = models.TextField(blank=True, null=True)
    germplasmname = models.TextField()
    defaultdisplayname = models.TextField()
    accessionnumber = models.TextField(blank=True, null=True)
    pedigree = models.TextField(blank=True, null=True)
    seedsource = models.TextField(blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    institutecode = models.TextField()
    institutename = models.TextField(blank=True, null=True)
    biologicalstatusofaccessioncode = models.TextField(blank=True, null=True)
    countryoforigincode = models.TextField(blank=True, null=True)
    typeofgermplasmstoragecode = models.TextField(blank=True, null=True)
    genus = models.TextField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    speciesauthority = models.TextField(blank=True, null=True)
    subtaxa = models.TextField(blank=True, null=True)
    subtaxaauthority = models.TextField(blank=True, null=True)
    acquisitiondate = models.TextField(blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'germplasm'

    # end class Meta

# end class Germplasm


class GermplasmAttribute(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    attributecategorydbid = models.ForeignKey('GermplasmAttributeCategory', models.DO_NOTHING, db_column='attributecategorydbid')
    attributedbid = models.TextField(primary_key=True)
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
    attributecategorydbid = models.TextField(primary_key=True)
    attributecategoryname = models.TextField(blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'germplasm_attribute_category'

    # end class Meta

# end class GermplasmAttributeCategory


class GermplasmAttributeValue(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    germplasmdbid = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='germplasmdbid')
    attributedbid = models.ForeignKey(GermplasmAttribute, models.DO_NOTHING, db_column='attributedbid')
    determineddate = models.TextField(blank=True, null=True)
    value = models.TextField()
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


class Map(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    mapdbid = models.TextField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'map'

    # end class Meta

# end class Map


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
    methoddbid = models.TextField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'method'

    # end class Meta

# end class Method


class Observation(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    observationunitdbid = models.ForeignKey('ObservationUnit', models.DO_NOTHING, db_column='observationunitdbid', blank=True, null=True)
    observationvariabledbid = models.ForeignKey('ObservationVariable', models.DO_NOTHING, db_column='observationvariabledbid', blank=True, null=True)
    observationdbid = models.TextField(primary_key=True)
    observationtimestamp = models.TextField(blank=True, null=True)
    seasondbid = models.ForeignKey('Season', models.DO_NOTHING, db_column='seasondbid', blank=True, null=True)
    collector = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'observation'

    # end class Meta

# end class Observation


class ObservationUnit(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    studydbid = models.ForeignKey('Study', models.DO_NOTHING, db_column='studydbid')
    germplasmdbid = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='germplasmdbid')
    observationunitdbid = models.TextField(primary_key=True)
    name = models.TextField()
    observationlevel = models.TextField(blank=True, null=True)
    observationlevels = models.TextField(blank=True, null=True)
    entrynumber = models.TextField(blank=True, null=True)
    entrytype = models.TextField(blank=True, null=True)
    plotnumber = models.TextField(blank=True, null=True)
    blocknumber = models.TextField(blank=True, null=True)
    plantnumber = models.TextField(blank=True, null=True)
    x = models.TextField(blank=True, null=True)
    y = models.TextField(blank=True, null=True)
    replicate = models.TextField(blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'observation_unit'

    # end class Meta

# end class ObservationUnit


class ObservationUnitXref(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    observationunitdbid = models.ForeignKey(ObservationUnit, models.DO_NOTHING, db_column='observationunitdbid')
    source = models.TextField()
    identifier = models.TextField()
    observationunitxrefdbid = models.TextField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'observation_unit_xref'

    # end class Meta

# end class ObservationUnitXref


class ObservationVariable(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    ontologydbid = models.ForeignKey('Ontology', models.DO_NOTHING, db_column='ontologydbid')
    observationvariabledbid = models.TextField(primary_key=True)
    observationvariablename = models.TextField(blank=True, null=True)
    traitdbid = models.ForeignKey('Trait', models.DO_NOTHING, db_column='traitdbid', related_name='observationVariables', to_field='traitDbId', blank=True, null=True)
    methoddbid = models.ForeignKey(Method, models.DO_NOTHING, db_column='methoddbid', blank=True, null=True)
    scaledbid = models.ForeignKey('Scale', models.DO_NOTHING, db_column='scaledbid', blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'observation_variable'

    # end class Meta

# end class ObservationVariable


class Ontology(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    ontologydbid = models.TextField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'ontology'

    # end class Meta

# end class Ontology


class Pedigree(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    germplasmDbId = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='germplasmdbid', related_name='germplasm')
    pedigree = models.TextField()
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
    programdbid = models.TextField(primary_key=True)
    name = models.TextField()
    abbreviation = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    leadperson = models.TextField(blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'program'

    # end class Meta

# end class Program


class Scale(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    scaledbid = models.TextField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'scale'

    # end class Meta

# end class Scale


class Season(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    seasondbid = models.TextField(primary_key=True)
    year = models.TextField(blank=True, null=True)
    season = models.TextField(blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'season'

    # end class Meta

# end class Season


class Study(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    trialdbid = models.ForeignKey('Trial', models.DO_NOTHING, db_column='trialdbid', related_name='studies')
    locationdbid = models.ForeignKey(Location, models.DO_NOTHING, db_column='locationdbid', blank=True, null=True)
    studytype = models.ForeignKey('StudyType', models.DO_NOTHING, db_column='studytype', related_name='studies', blank=True, null=True)
    studydbid = models.TextField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    startdate = models.TextField(blank=True, null=True)
    enddate = models.TextField(blank=True, null=True)
    active = models.NullBooleanField()
    license = models.TextField(blank=True, null=True)
    lastupdateversion = models.TextField(blank=True, null=True)
    lastupdatetimestamp = models.TextField(blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'study'

    # end class Meta

# end class Study


class MarkerProfile(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmdbid', related_name='mprofiles-details+', on_delete=models.CASCADE, default='', to_field='germplasmdbid')
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
#         # end class Meta
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
    studydbid = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid', blank=True, null=True)
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
    studydbid = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid')
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    url = models.TextField()
    studydatalinkdbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'study_data_link'

    # end class Meta

# end class StudyDataLink


class StudySeason(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    studydbid = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid')
    seasondbid = models.ForeignKey(Season, models.DO_NOTHING, db_column='seasondbid')
    studyseasondbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'study_season'

    # end class Meta

# end class StudySeason


class StudyType(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    name = models.TextField(primary_key=True)
    description = models.TextField(blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'study_type'

    # end class Meta

# end class StudyType


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
    taxondbid = models.ForeignKey(TaxonXref, models.DO_NOTHING, db_column='taxondbid', blank=True, null=True)
    germplasmdbid = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='germplasmdbid', blank=True, null=True)
    taxonxrefgermplasmdbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'taxon_xref_germplasm'

    # end class Meta

# end class TaxonXrefGermplasm


class Trait(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    traitDbId = models.TextField(primary_key=True, db_column='traitdbid')
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'trait'

    # end class Meta

# end class Trait


class Treatment(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    observationunitdbid = models.ForeignKey(ObservationUnit, models.DO_NOTHING, db_column='observationunitdbid')
    factor = models.TextField()
    modality = models.TextField()
    treatmentdbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'treatment'

    # end class Meta

# end class Treatment


class Trial(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    programdbid = models.ForeignKey(Program, models.DO_NOTHING, db_column='programdbid', blank=True, null=True)
    trialdbid = models.TextField(primary_key=True)
    name = models.TextField()
    startdate = models.TextField(blank=True, null=True)
    enddate = models.TextField(blank=True, null=True)
    active = models.NullBooleanField()
    datasetauthorshiplicence = models.TextField(blank=True, null=True)
    datasetauthorshipdatasetpui = models.TextField(blank=True, null=True)


    class Meta:

        managed = settings.IS_TESTING
        db_table = 'trial'

    # end class Meta

# end class Trial


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
    contactdbid = models.ForeignKey(Contact, models.DO_NOTHING, db_column='contactdbid', related_name='contacts', blank=True, null=True)
    trialcontactdbid = models.IntegerField(primary_key=True)

    class Meta:

        managed = settings.IS_TESTING
        db_table = 'trial_contact'

    # end class Meta

# end class TrialContact


class Phenotype(models.Model):

    cropdbid = models.TextField(db_column='cropdbid')
    observationUnitDbId = models.TextField(db_column='observationunitdbid', primary_key=True)
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
    x = models.TextField()
    y = models.TextField()
    factor = models.TextField()
    modality = models.TextField()
    source = models.TextField()
    observationUnitXrefDbId = models.TextField(db_column='observationunitxrefdbid')
    observationDbId = models.TextField(db_column='observationdbid')
    observationVariableDbId = models.TextField(db_column='observationvariabledbid')
    season = models.TextField()
    value = models.TextField()
    observationTimestamp = models.TextField(db_column='observationtimestamp')
    collector = models.TextField()


    class Meta:

        managed = False
        db_table = 'phenotype'

    # end class Meta

# end class Phenotype
