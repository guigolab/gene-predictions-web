# from rest.taxon_files import TaxonFilesApi
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

 # this is what the taxon_service should do: iterate over lineage (we get only the 8/9 mayor taxonomy ranks) of a species, 
 # create a taxon_node (tax_id, name) for every element of the array. 
 # Than iterate from the children to the parent and push the children to the parent's children attribute
	# def post(self):
	# 	tax1 = TaxonNode(tax_id = "0026", name= "fadsfasd").save()
	# 	tax2= TaxonNode(tax_id = "0009",name= "afasf").save()
	# 	tax3 = TaxonNode(tax_id= "00012", name= "cacsafa").save()
	# 	taxon_node = TaxonNode(tax_id = "0015", name="test node with children 2", children = [tax1,tax2,tax3]).save()
	# 	return Response(taxon_node, mimetype="application/json", status=200)
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