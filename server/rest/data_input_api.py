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
REQUIRED_PARAMS=['taxid','API_KEY','type']

class InputDataApi(Resource):

## add file replace here (PUT)
    def post(self):
        req = request.json if request.is_json else request.form
        app.logger.info(req['type'])
        if not request.files or not 'file' in request.files.keys() \
             or not all(key in REQUIRED_PARAMS for key in req.keys()) \
                 or not req['type'] in [enum.value for enum in FileType]:
            raise SchemaValidationError
        if req['API_KEY'] != API_KEY:
            raise Unauthorized
        type = req['type']
        taxid = req['taxid']
        filename= request.files['file'].filename
        if len(TaxonFile.objects(name=filename)) > 0:
            raise RecordAlreadyExistError
        organism = organism_service.get_or_create_organism(taxid)
        if not organism:
            raise NotFound
        saved_file = TaxonFile(taxid=taxid, file = request.files['file'], name=filename, type=FileType[type.upper()]).save()
        if saved_file.type == FileType.PARAM:
            organism.param_files.append(saved_file)
        elif saved_file.type == FileType.FASTA:
            organism.fastas.append(saved_file)
        elif saved_file.type == FileType.GFF:
            organism.gffs.append(saved_file)
        else:
            raise SchemaValidationError
        organism.save()
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