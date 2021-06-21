from flask import Response, request
from flask import current_app as app
from db.models import TaxonNode
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from errors import InternalServerError, SchemaValidationError, UserNotFoundError, EmailAlreadyExistError
import json

class TaxonNodesApi(Resource):
	def get(self):
		taxonNodes = TaxonNode.objects().to_json()
		return Response(taxonNodes, mimetype="application/json", status=200)

	# def delete(self):
	# 	taxonNodes = TaxonNode.objects.delete()
	# 	return '', 200
	# the taxon nodes will be created in the taxon_service, unfortunately we depend on another API: this or download and charge the taxa db in our db and query it?
	# def post(self):
	# 	try:
	# 		file = request.files.get('file')
	# 		app.logger.info(request.form['json'])
	# 		data = json.loads(request.form['json'])
	# 		app.logger.info(request.files)
	# 		taxonNode = TaxonNode(**data, files=(file)).save()
	# 		# id = taxonNode.id
	# 		return  201
	# 	except NotUniqueError:
	# 		raise EmailAlreadyExistError
	# 	except ValidationError:
	# 		raise SchemaValidationError
	# 	except Exception as e:
	# 		app.logger.error(e)
	# 		raise InternalServerError

class TaxonNodeApi(Resource):
	def put(self, id):
		body = request.get_json()
		TaxonNode.objects.get(id=id).update(**body)
		return '', 200

	def get(self, id):
		try:
			taxonNode = TaxonNode.objects.get(id=id).to_json()
			return Response(taxonNode, mimetype="application/json", status=200)
		except DoesNotExist:
			raise UserNotFoundError

	def delete(self, id):
		taxonNode = TaxonNode.objects.get(id=id).delete()
		return '', 200

		
# TODO create endpoints for retrieving files and send them to client
# class TaxonNodeFilesApi(Resource):

# 	def get(self,id):
# 		try:
# 			taxon_node = TaxonNode.objects