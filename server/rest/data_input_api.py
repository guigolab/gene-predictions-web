import imp
from flask import request, Response
from flask import current_app as app
from db.models import  TaxonFile,TaxonNode,Organism,GeneIdResults,GeneIdStats,FileType
from flask_restful import Resource
from errors import  NotFound, SchemaValidationError,Unauthorized,RecordAlreadyExistError
import json
import os
from services import organism_service

API_KEY = os.getenv('SECRET_KEY')
REQUIRED_PARAMS=['taxid','API_KEY']

class InputDataApi(Resource):

## add file replace here (PUT)
    def post(self):
        req = request.json if request.is_json else request.form
        if not request.files or not 'file' in request.files.keys() \
             or not all(key in REQUIRED_PARAMS for key in req.keys()):
            raise SchemaValidationError
        if req['API_KEY'] != API_KEY:
            raise Unauthorized
        taxid = req['taxid']
        file_values= request.files['file'].filename.split('.')
        filetype= file_values[-1]
        if not filetype in [type.value for type in FileType]:
            raise SchemaValidationError
        filename = file_values[0:-1]
        app.logger.info(filetype)
        app.logger.info(filename)
        if len(TaxonFile.objects(name=filename)) > 0:
            raise RecordAlreadyExistError
        organism = organism_service.get_or_create_organism(taxid)
        if not organism:
            raise NotFound
        TaxonFile(taxid=taxid, file = request.files['file'], name=filename[0], type=FileType[filetype.upper()]).save()
        return 201

    def delete(self):
        req = request.args
        app.logger.info(req)
        if 'API_KEY' in req.keys() and req['API_KEY'] == API_KEY:
            TaxonNode.drop_collection()
            Organism.drop_collection()
            for tax_file in TaxonFile.objects(file__ne=None):
                tax_file.file.delete()
            TaxonFile.drop_collection()
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