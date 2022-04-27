# from typing_extensions import Required
from . import db
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

# model for species browsing
class TaxonNode(db.Document):
    children = db.ListField(db.LazyReferenceField('self', passthrough=True))
    name = db.StringField(required=True)
    taxid = db.StringField(required=True)
    rank = db.StringField()
    leaves = db.IntField()
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
    fasta_size = db.IntField() #size of fasta file to process in kb
    command = db.StringField()
    gff2ps = db.BooleanField() #if user wants graphical representation
    created = db.DateTimeField(default=datetime.datetime.utcnow)


#model where file are stored, temporary solution
class FileStorage(db.Document):
    name = db.StringField(required=True,unique=True) #file name
    file = db.FileField(required=True)
    metadata = db.DictField()
    created = db.DateTimeField(default=datetime.datetime.utcnow)
    meta = {
        'indexes': [
            'name',
        ]
    }

class FileModel(db.Document):
    name = db.StringField(required=True,unique=True)
    organism = db.StringField(required=True)
    taxid = db.StringField(required=True)
    description = db.StringField()
    metadata = db.DictField()
    meta = {
        'allow_inheritance': True,
        'indexes': [
            'name',
            'taxid',
            'organism'
        ]
    }

class Genome(db.Document):
    name = db.StringField(required=True,unique=True)
    insdc_accession = db.StringField()
    fastaLocation = db.StringField(required=True,unique=True)
    faiLocation = db.StringField(required=True,unique=True)
    gziLocation = db.StringField(required=True,unique=True) 
    chromAlias = db.StringField()
    meta = {
        'indexes': [
            'name'
        ]
    }
   
class Annotation(db.Document):
    name = db.StringField(required=True,unique=True)
    gffGzLocation = db.StringField(required=True,unique=True)
    tabIndexLocation = db.StringField(required=True,unique=True)
    targetGenome = db.StringField(required=True)
    lengthTreshold = db.StringField()
    evidenceSource = db.StringField()
    created = db.DateTimeField(default=datetime.datetime.utcnow)
    meta = {
        'indexes': [
            'name'
        ]
    }

class ParamFile(db.Document):
    name = db.StringField(required=True,unique=True)
    paramLocation = db.StringField(required=True,unique=True)
    created = db.DateTimeField(default=datetime.datetime.utcnow)
    meta = {
        'indexes': [
            'name'
        ]
    }

class Organism(db.Document):
    name = db.StringField(required=True,unique=True)
    common_name= db.StringField()
    taxid = db.StringField(required=True)
    taxon_lineage = db.ListField(db.LazyReferenceField(TaxonNode))
    ordered_lineage = db.ListField() ##TODO fix duplicated lineage 
    genomes = db.ListField(db.LazyReferenceField(Genome))
    annotations = db.ListField(db.LazyReferenceField(Annotation))
    param_files = db.ListField(db.LazyReferenceField(ParamFile))
    meta = {
        'indexes': [
            'taxid',
            'name'
        ]
    }