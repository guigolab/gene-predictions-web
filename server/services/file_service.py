from db.models import Annotation, FileStorage, Genome, ParamFile

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

def store_file(params):
    file_to_store = params['file']
    name = file_to_store.filename
    #mimetype here
    file_obj = FileStorage(name=name, file=file_to_store).save()
    return file_obj
