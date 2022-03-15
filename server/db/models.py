# from typing_extensions import Required
from . import db
from enum import Enum
import datetime

def handler(event):
    """Signal decorator to allow use of callback functions as class decorators."""

    def decorator(fn):
        def apply(cls):
            event.connect(fn, sender=cls)
            return cls
        fn.apply = apply
        return fn
    return decorator

class FileType(Enum):
    FASTA = 'fasta'
    GFF = 'gff'
    PARAM = 'param'

# model for species browsing
class TaxonNode(db.Document):
    children = db.ListField(db.LazyReferenceField('self', passthrough=True))
    name = db.StringField(required=True,unique=True)
    taxid = db.StringField(required=True)
    rank = db.StringField()
    leaves = db.IntField()
    meta = {
          'indexes': [
            {'fields':('name','taxid'), 'unique':True}
        ]
    }

#file model (GFF, FASTA and PARAM)
class TaxonFile(db.Document):
    taxid = db.StringField(required=True)
    type = db.EnumField(FileType)
    name = db.StringField(required=True, unique=True)
    file = db.FileField(required=True)
    description = db.StringField()
    meta = {
          'indexes': [
            'taxid',
            'name',
        ]
    }

#data container
class Organism(db.Document):
    name = db.StringField(required=True,unique=True)
    taxid = db.StringField(required=True)
    taxon_lineage = db.ListField(db.LazyReferenceField(TaxonNode))
    param_files = db.ListField(db.LazyReferenceField(TaxonFile))
    gffs = db.ListField(db.LazyReferenceField(TaxonFile))
    fastas = db.ListField(db.LazyReferenceField(TaxonFile))
    meta = {
          'indexes': [
            {'fields':('name','taxid'), 'unique':True}
        ]
    }
##implementation of geneid model to temporally persist ouput files, removed by client delete request
class GeneIdResults(db.Document):
    jpg = db.FileField()
    ps = db.FileField()
    run_time = db.StringField()
    output_file = db.FileField(required=True)
    geneid_cmd = db.StringField()
    param_species = db.StringField()
    created = db.DateTimeField(default=datetime.datetime.utcnow)
    meta = {
        'indexes': [
            {'fields': ['created'], 'expireAfterSeconds': 86400}
        ]
    }
#stats of geneid usage
class GeneIdStats(db.Document): ## TODO: create a geneid statistics page (d3 in the front)
    ip = db.StringField() 
    run_time = db.StringField()
    fasta_size = db.IntField() #size of fasta file to process
    command = db.StringField()
    gff2ps = db.BooleanField() #if user wants graphical representation
    created = db.DateTimeField(default=datetime.datetime.utcnow)

##project model intended as a container of species
# class Project(db.Document):
#     project_accession = db.StringField()
#     species = 
