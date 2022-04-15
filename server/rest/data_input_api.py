from flask import request, Response
from flask import current_app as app
from db.models import  Annotation, FileStorage, FileModel, Genome, ParamFile,TaxonNode,Organism,GeneIdResults,GeneIdStats
from flask_restful import Resource
from errors import  NotFound, SchemaValidationError,Unauthorized,RecordAlreadyExistError
import os
from services import organism_service, file_service

API_KEY = os.getenv('SECRET_KEY')
REQUIRED_PARAMS=['taxid','API_KEY','type']

class InputDataApi(Resource):

## separate file input logics
## add file replace here (PUT)
    # def post(self):
    #     req = request.json if request.is_json else request.form
    #     app.logger.info(req['type'])
    #     if not request.files or not 'file' in request.files.keys() \
    #          or not all(key in REQUIRED_PARAMS for key in req.keys()) \
    #              or not req['type'] in [enum.value for enum in FileType]:
    #         raise SchemaValidationError
    #     if req['API_KEY'] != API_KEY:
    #         raise Unauthorized
    #     type = req['type']
    #     taxid = req['taxid']
    #     filename= request.files['file'].filename
    #     if TaxonFile.objects(name=filename).first():
    #         raise RecordAlreadyExistError
    #     organism = organism_service.get_or_create_organism(taxid)
    #     if not organism:
    #         raise NotFound
    #     saved_file = TaxonFile(taxid=taxid, file = request.files['file'], name=filename, type=FileType[type.upper()]).save()
    #     if saved_file.type == FileType.PARAM:
    #         organism.param_files.append(saved_file)
    #     elif saved_file.type == FileType.FASTA:
    #         organism.fastas.append(saved_file)
    #     elif saved_file.type == FileType.GFF:
    #         organism.gffs.append(saved_file)
    #     else:
    #         raise SchemaValidationError
    #     organism.save()
    #     return 201

    def delete(self):
        req = request.args
        if 'API_KEY' in req.keys() and req['API_KEY'] == API_KEY:
            TaxonNode.drop_collection()
            Organism.drop_collection()
            for file in FileStorage.objects():
                file.file.delete()
            FileModel.drop_collection()
            Genome.drop_collection()
            Annotation.drop_collection()
            ParamFile.drop_collection()
            # for result in GeneIdResults.objects(ps__ne=None):
            #     result.ps.delete()
            # for result in GeneIdResults.objects(jpg__ne=None):
            #     result.jpg.delete()  
            GeneIdResults.drop_collection()
            GeneIdStats.drop_collection()
            for entry in os.scandir('/tmp'):
                os.remove(entry)
        else:
            raise Unauthorized
        return 200

class FilesUploadApi(Resource):
    def post(self):
        file = request.files['file']
        file.save(os.path.join(app.root_path,'static', file.filename))
        return 201,file.filename
