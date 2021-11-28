# from typing_extensions import Required
from . import db
from enum import Enum

class FileType(Enum):
    FASTA = 'fasta'
    GFF = 'gff'
    PARAM = 'param'
    OTHER = 'other'

class TaxonNode(db.Document):
    children = db.ListField(db.LazyReferenceField('self', passthrough=True))
    name = db.StringField(required=True,unique=True)
    taxonId = db.IntField(required=True)
    rank = db.StringField()
    leaves = db.IntField()

class Organism(db.Document):
    ##use geographical coords for Map API (mongoengine provides specific geo fields)
    name = db.StringField(required=True,unique=True)
    taxonId = db.IntField(required=True)
    taxon_lineage = db.ListField(db.LazyReferenceField(TaxonNode))

class TaxonFile(db.Document):
    organism = db.LazyReferenceField(Organism, required=True)
    type = db.EnumField(FileType, default=FileType.GFF)
    name = db.StringField(required=True, unique=True)
    file = db.FileField(required=True)

class ResultFiles(db.Document):
    file = db.FileField(required=True)
    type = db.StringField()
    name = db.StringField()

##implementation of geneid model to temporally persist ouput files, removed by client delete request
class GeneIdResults(db.Document):
    jpg = db.LazyReferenceField(ResultFiles)
    ps = db.LazyReferenceField(ResultFiles)
    run_time = db.StringField()
    output_file = db.LazyReferenceField(ResultFiles)
    output = db.StringField()
    geneid_cmd = db.StringField()
    param_species = db.StringField()