from flask import request
from flask import current_app as app
from db.models import  Annotation,Genome, ParamFile,TaxonNode,Organism,GeneIdResults,GeneIdStats
from flask_restful import Resource
from errors import Unauthorized
import os

API_KEY = os.getenv('API_KEY')
REQUIRED_PARAMS=['taxid','API_KEY','type']

class InputDataApi(Resource):

##drop db
    def delete(self):
        req = request.args
        if 'API_KEY' in req.keys() and req['API_KEY'] == API_KEY:
            TaxonNode.drop_collection()
            Organism.drop_collection()
            Genome.drop_collection()
            Annotation.drop_collection()
            ParamFile.drop_collection()
            # for result in GeneIdResults.objects(ps__ne=None):
            #     result.ps.delete()
            # for result in GeneIdResults.objects(jpg__ne=None):
            #     result.jpg.delete()  
            GeneIdResults.drop_collection()
            GeneIdStats.drop_collection()
            # for entry in os.scandir('/tmp'):
            #     os.remove(entry)
        else:
            raise Unauthorized
        return 200

class FilesUploadApi(Resource):
    def post(self):
        file = request.files['file']
        file.save(os.path.join(app.root_path,'static', file.filename))
        return 201,file.filename
