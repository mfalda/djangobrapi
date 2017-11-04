from django.db import models


class Contact(models.Model):

    cropdbid = models.ForeignKey('Crop', models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    contactdbid = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    orcid = models.TextField(blank=True, null=True)
    institutename = models.TextField(blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'contact'

	# end class Meta

# end class Contact


class Crop(models.Model):


    cropdbid = models.TextField(primary_key=True)
    commonname = models.TextField()

    class Meta:

        managed = False
        db_table = 'crop'

	# end class Meta

# end class Crop


class Donor(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    germplasmdbid = models.ForeignKey('Germplasm', models.DO_NOTHING, db_column='germplasmdbid', blank=True, null=True)
    donoraccessionnumber = models.TextField(blank=True, null=True)
    donorinstitutecode = models.TextField(blank=True, null=True)
    donorgermplasmpui = models.TextField(blank=True, null=True)

    class Meta:

        managed = False
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

        managed = False
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

        managed = False
        db_table = 'germplasm_attribute'

	# end class Meta

# end class GermplasmAttribute


class GermplasmAttributeCategory(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    attributecategorydbid = models.TextField(primary_key=True)
    attributecategoryname = models.TextField(blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'germplasm_attribute_category'

	# end class Meta

# end class GermplasmAttributeCategory


class GermplasmAttributeValue(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    germplasmdbid = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='germplasmdbid')
    attributedbid = models.ForeignKey(GermplasmAttribute, models.DO_NOTHING, db_column='attributedbid')
    determineddate = models.TextField(blank=True, null=True)
    value = models.TextField()

    class Meta:

        managed = False
        db_table = 'germplasm_attribute_value'

	# end class Meta

# end class GermplasmAttributeValue


class Location(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    locationdbid = models.TextField(primary_key=True)
    type = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    abbreviation = models.TextField(blank=True, null=True)
    countrycode = models.TextField(blank=True, null=True)
    countryname = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    altitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    institutename = models.TextField(blank=True, null=True)
    instituteaddress = models.TextField(blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'location'

	# end class Meta

# end class Location


class LocationAdditionalInfo(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    locationdbid = models.ForeignKey(Location, models.DO_NOTHING, db_column='locationdbid', blank=True, null=True)
    key = models.TextField()
    value = models.TextField()

    class Meta:

        managed = False
        db_table = 'location_additional_info'

	# end class Meta

# end class LocationAdditionalInfo


class Map(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    mapdbid = models.TextField(primary_key=True)

    class Meta:

        managed = False
        db_table = 'map'

	# end class Meta

# end class Map


class Marker(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    markerdbid = models.TextField()
    defaultdisplayname = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    refalt = models.TextField(blank=True, null=True)
    analysismethods = models.TextField(blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'marker'

	# end class Meta

# end class Marker


class Markerprofile(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    markerprofiledbid = models.TextField(primary_key=True)

    class Meta:

        managed = False
        db_table = 'markerprofile'

	# end class Meta

# end class Markerprofile


class Method(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    methoddbid = models.TextField(primary_key=True)

    class Meta:

        managed = False
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

        managed = False
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

        managed = False
        db_table = 'observation_unit'

	# end class Meta

# end class ObservationUnit


class ObservationUnitXref(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    observationunitdbid = models.ForeignKey(ObservationUnit, models.DO_NOTHING, db_column='observationunitdbid')
    source = models.TextField()
    id = models.TextField()

    class Meta:

        managed = False
        db_table = 'observation_unit_xref'

	# end class Meta

# end class ObservationUnitXref


class ObservationVariable(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    ontologydbid = models.ForeignKey('Ontology', models.DO_NOTHING, db_column='ontologydbid')
    observationvariabledbid = models.TextField(primary_key=True)
    observationvariablename = models.TextField(blank=True, null=True)
    traitdbid = models.ForeignKey('Trait', models.DO_NOTHING, db_column='traitdbid', blank=True, null=True)
    methoddbid = models.ForeignKey(Method, models.DO_NOTHING, db_column='methoddbid', blank=True, null=True)
    scaledbid = models.ForeignKey('Scale', models.DO_NOTHING, db_column='scaledbid', blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'observation_variable'

	# end class Meta

# end class ObservationVariable


class Ontology(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    ontologydbid = models.TextField(primary_key=True)

    class Meta:

        managed = False
        db_table = 'ontology'

	# end class Meta

# end class Ontology


class Pedigree(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    germplasmdbid = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='germplasmdbid')
    pedigree = models.TextField()
    parent1id = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='parent1id')
    parent2id = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='parent2id')

    class Meta:

        managed = False
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

        managed = False
        db_table = 'program'

	# end class Meta

# end class Program


class Sample(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    sampledbid = models.TextField(primary_key=True)

    class Meta:

        managed = False
        db_table = 'sample'

	# end class Meta

# end class Sample


class Scale(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    scaledbid = models.TextField(primary_key=True)

    class Meta:

        managed = False
        db_table = 'scale'

	# end class Meta

# end class Scale


class Season(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    seasondbid = models.TextField(primary_key=True)
    year = models.TextField(blank=True, null=True)
    season = models.TextField(blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'season'

	# end class Meta

# end class Season


class Study(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    trialdbid = models.ForeignKey('Trial', models.DO_NOTHING, db_column='trialdbid')
    locationdbid = models.ForeignKey(Location, models.DO_NOTHING, db_column='locationdbid', blank=True, null=True)
    studytype = models.ForeignKey('StudyType', models.DO_NOTHING, db_column='studytype', blank=True, null=True)
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

        managed = False
        db_table = 'study'

	# end class Meta

# end class Study


class StudyAdditionalInfo(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    studydbid = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid', blank=True, null=True)
    key = models.TextField()
    value = models.TextField()

    class Meta:

        managed = False
        db_table = 'study_additional_info'

	# end class Meta

# end class StudyAdditionalInfo


class StudyContact(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    studydbid = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid')
    contactdbid = models.ForeignKey(Contact, models.DO_NOTHING, db_column='contactdbid')

    class Meta:

        managed = False
        db_table = 'study_contact'

	# end class Meta

# end class StudyContact


class StudyDataLink(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    studydbid = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid')
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    url = models.TextField()

    class Meta:

        managed = False
        db_table = 'study_data_link'

	# end class Meta

# end class StudyDataLink


class StudySeason(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    studydbid = models.ForeignKey(Study, models.DO_NOTHING, db_column='studydbid')
    seasondbid = models.ForeignKey(Season, models.DO_NOTHING, db_column='seasondbid')

    class Meta:

        managed = False
        db_table = 'study_season'

	# end class Meta

# end class StudySeason


class StudyType(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    name = models.TextField(primary_key=True)
    description = models.TextField(blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'study_type'

	# end class Meta

# end class StudyType


class TaxonXref(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    taxondbid = models.TextField(primary_key=True)
    source = models.TextField()
    rank = models.TextField(blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'taxon_xref'

	# end class Meta

# end class TaxonXref


class TaxonXrefGermplasm(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    taxondbid = models.ForeignKey(TaxonXref, models.DO_NOTHING, db_column='taxondbid', blank=True, null=True)
    germplasmdbid = models.ForeignKey(Germplasm, models.DO_NOTHING, db_column='germplasmdbid', blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'taxon_xref_germplasm'

	# end class Meta

# end class TaxonXrefGermplasm


class Trait(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    traitdbid = models.TextField(primary_key=True)

    class Meta:

        managed = False
        db_table = 'trait'

	# end class Meta

# end class Trait


class Treatment(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    observationunitdbid = models.ForeignKey(ObservationUnit, models.DO_NOTHING, db_column='observationunitdbid')
    factor = models.TextField()
    modality = models.TextField()

    class Meta:

        managed = False
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

        managed = False
        db_table = 'trial'

	# end class Meta

# end class Trial


class TrialAdditionalInfo(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    trialdbid = models.ForeignKey(Trial, models.DO_NOTHING, db_column='trialdbid', blank=True, null=True)
    key = models.TextField()
    value = models.TextField()

    class Meta:

        managed = False
        db_table = 'trial_additional_info'

	# end class Meta

# end class TrialAdditionalInfo


class TrialContact(models.Model):

    cropdbid = models.ForeignKey(Crop, models.DO_NOTHING, db_column='cropdbid', blank=True, null=True)
    trialdbid = models.ForeignKey(Trial, models.DO_NOTHING, db_column='trialdbid', blank=True, null=True)
    contactdbid = models.ForeignKey(Contact, models.DO_NOTHING, db_column='contactdbid', blank=True, null=True)

    class Meta:

        managed = False
        db_table = 'trial_contact'

	# end class Meta

# end class TrialContact
