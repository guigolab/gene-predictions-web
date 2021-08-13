# from rest.taxon_files import TaxonFilesApi
from logging import root
import services.taxon_service as service
from flask import Response, request
from flask import current_app as app
from db.models import TaxonNode
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from errors import InternalServerError, SchemaValidationError, UserNotFoundError, EmailAlreadyExistError
import json

class TaxonNodesApi(Resource):
	def get(self):
		taxon_nodes = TaxonNode.objects().to_json()
		return Response(taxon_nodes, mimetype="application/json", status=200)

	def delete(self):
		taxon_nodes = TaxonNode.objects.delete()
		return '', 200
 
# class TaxonNodeApi(Resource):

# 	def get(self, tax_id):
# 		try:
# 			taxon_node = TaxonNode.objects(tax_id=tax_id).first()
# 			###fetch references
# 			children_dict = {}
# 			children_dict['children'] = [lazy_ref.fetch().to_json() for lazy_ref in taxon_node.children]
# 			return Response(json.dumps(children_dict), mimetype="application/json", status=200)
# 		except DoesNotExist:
# 			raise UserNotFoundError

# 	def delete(self, tax_id):
# 		taxonNode = TaxonNode.objects.get(tax_id=tax_id).delete()
# 		return '', 200
