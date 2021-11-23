from flask import Response, request
from flask import current_app as app
from db.models import TaxonFile,GeneIdResults
from flask_restful import Resource
from flask import send_file
import services.geneid_service as service
from mongoengine.errors import ValidationError
from errors import InternalServerError, SchemaValidationError
import json



class GeneIdServerApi(Resource):
    #get param files for formulary
    def get(self,id=None):
        try:
            if id:
                # jpg = GeneIdResults.objects().first()
                for result in GeneIdResults.objects():
                    if id == str(result.ps.grid_id):
                        file = result.ps.read()
                        content_type = result.ps.content_type
                    if id == str(result.jpg.grid_id):
                        file = result.jpg.read()
                        content_type = result.jpg.content_type
                return Response(file, content_type=content_type, status=200)
            else:
                taxon_files = TaxonFile.objects(type="param")
                taxon_names=[]
                for file in taxon_files:
                    data={}
                    data['text'] = file.organism.name ##need to dereference taxon
                    data['value'] = file.name
                    taxon_names.append(data)
                return Response(json.dumps([taxon_names]), mimetype="application/json", status=200)
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError

    def post(self):
        try:
            data = request.form
            files = request.files
            app.logger.info("PASSING HERE")
            geneid_result = service.programs_configs(data,files)
            # list_response = []
            # for file in output_files:
            #     list_response.append(file.name) ## we pass the path of the files to the client (an interval scheduler will remove them)
            return Response(geneid_result.to_json(), mimetype="application/json", status=200)
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError

    def delete(self,id):
        geneid = GeneIdResults.objects.get(id=id)
        if geneid.jpg:
            geneid.jpg.delete()
        if geneid.ps:
            geneid.ps.delete()
        geneid.delete()
        return '', 200