from os import name
from flask import Response, request
from flask import current_app as app
from db.models import TaxonFile, TaxonNode
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from errors import InternalServerError, SchemaValidationError, UserNotFoundError, EmailAlreadyExistError
import json

class TaxonFilesApi(Resource):
    def get(self,tax_id):
        taxon = TaxonNode.objects(tax_id=tax_id).first()
        app.logger.info(taxon)
        taxon_files= TaxonFile.objects(taxon = taxon).to_json()
        app.logger.info(taxon_files)
        return Response(taxon_files, mimetype="application/json", status=200)
   
    def post(self,tax_id):
        try:
            file = request.files.get('file')
            app.logger.info(request.form['json'])
            data = json.loads(request.form['json'])
            name = "Sarcophilus Harrisii"
            new_taxon = TaxonNode(tax_id=tax_id, name=name).save() ##should use get || create
            taxon_files = TaxonFile(**data, file=file, taxon = new_taxon).save()
            return  201
        except NotUniqueError:
            raise EmailAlreadyExistError
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError

class TaxonFileApi(Resource):

     def post(self, name):
        try:
            taxon_file = TaxonFile.objects(name=name).first()
            file = taxon_file.file.read()
            content_type = taxon_file.file.content_type
            return Response(file, content_type=content_type, status=200)
        except NotUniqueError:
            raise EmailAlreadyExistError
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError
    #TODO expose endopoint to upload files from workflow
	# def put(self, id):
	# 	body = request.get_json()
	# 	TaxonFiles.objects.get(id=id).update(**body)
	# 	return '', 200
    # def get(self, name):
    #     try:
    #         taxon_file = TaxonFile.objects(name=name).first()
    #         file = taxon_file.file.read()
    #         content_type = file.content_type
    #         return Response(taxon_file, content_type=content_type, status=200)
    #     except DoesNotExist:
    #         raise UserNotFoundError

	# def delete(self, id):
	# 	taxon_files = TaxonFiles.objects.get(id=id).delete()
	# 	return '', 200
# TODO create endpoints for retrieving files and send them to client
# class TaxonNodeFilesApi(Resource):

# 	def get(self,id):
# 		try:
# 			taxon_node = TaxonNode.objects