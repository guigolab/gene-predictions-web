from flask import Response, request
from flask import current_app as app
from db.models import TaxonFile,GeneIdResults
from flask_restful import Resource
from flask import send_file
import services.geneid_service as service
from mongoengine.errors import ValidationError, DoesNotExist
from errors import InternalServerError, SchemaValidationError, NotFound
import json



class GeneIdServerApi(Resource):
    #get param files for formulary
    def get(self,id):
        try:
            # jpg = GeneIdResults.objects().first()
            result_model = GeneIdResults.objects(id = id).first()
            if not result_model:
                for result in GeneIdResults.objects():
                    if id == str(result.ps.grid_id):
                        file = result.ps.read()
                        content_type = result.ps.content_type
                    if id == str(result.jpg.grid_id):
                        file = result.jpg.read()
                        content_type = result.jpg.content_type
                return Response(file, content_type=content_type, status=200)
            else:
                app.logger.info(result_model.to_json())
                return Response(result_model.to_json(),mimetype="application/json", status=200)
        except DoesNotExist:
            raise NotFound
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError

    def post(self):
        try:
            data = request.form
            files = request.files
            app.logger.info("PASSING HERE")
            geneid_result = service.programs_configs(data,files)
            app.logger.info(geneid_result.to_json())
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