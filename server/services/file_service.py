from db.models import Annotation, Genome, ParamFile
from errors import NotFound, SchemaValidationError
from services import organism_service
from flask import current_app as app
from utils import common_functions

GENERAL_PARAMS = ['name','taxid']
GENOME_LOCATIONS = ['fastaLocation','faiLocation','gziLocation']
ANNOTATION_LOCATIONS = ['gffGzLocation','tabIndexLocation','targetGenome','evidenceSource']
PARAM_FILE_LOCATIONS = ['paramLocation']

def validate_params(params, required_fields):
    return [key for key in required_fields if key not in params.keys()]

#return model
def model_handler(model):
    if model == 'genomes':
        return Genome
    elif model == 'annotations':
        return Annotation
    elif model == 'parameters':
        return ParamFile
    else:
        return None

def organism_handler(model, file, organism):
    if model == 'genomes':
        organism.genomes.append(file)
    elif model == 'annotations':
        organism.annotations.append(file)
    elif model == 'parameters':
        organism.param_files.append(file)
    else:
        return
    organism.save()
    return organism

def reference_handler(model, organism):
    if model == 'genomes':
        return organism.genomes
    elif model == 'annotations':
        return organism.annotations
    else:
        return organism.param_files

def location_handler(model):
    if model == 'genomes':
        return GENOME_LOCATIONS 
    elif model == 'annotations':
        return ANNOTATION_LOCATIONS
    elif model == 'parameters':
        return PARAM_FILE_LOCATIONS
    else:
        return None
#model to retrieve file path for download
def create_file_model(params, model):
    saved_file_model = model(**params).save()
    return saved_file_model

def payload_parser(request, model):
    params = dict(**request.json) if request.is_json else dict(**request.form)
    if not 'API_KEY' in params.keys() or not common_functions.auth_request(params['API_KEY']):
        raise NotFound
    else:
        params.pop('API_KEY')
    error_keys=validate_params(params, GENERAL_PARAMS+location_handler(model))
    if error_keys:
        return error_keys
    model_obj = model_handler(model)
    ##pop taxid from payload dict
    taxid = params.pop('taxid')
    organism = organism_service.get_or_create_organism(taxid)
    saved_file_object=create_file_model(params,model_obj)
    updated_organism = organism_handler(model,saved_file_object,organism)
    if updated_organism:
        return saved_file_object.to_json()
    else:
        return list()

def search_by_taxid(request, model):
    args = request.args
    if 'taxid' in args.keys():
        taxid = args['taxid']
        organism = organism_service.get_or_create_organism(taxid)
        model_obj = model_handler(model)
        ids = [ref.id for ref in reference_handler(model,organism)]
        return  model_obj.objects(id__in=ids).exclude('id').to_json()
    else:
        return []
#manage file deletion and organism and taxon deletion cascade
def delete_file(name,model):
    model_obj = model_handler(model)
    file_obj = model_obj.objects(name=name).first()

    

