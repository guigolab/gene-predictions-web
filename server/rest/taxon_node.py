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
	def get(self, to_tree=None):
		## get the root node
		root = TaxonNode.objects(tax_id="1").first()
		if to_tree:
			# app.logger.info(root)
			# tree.children = [lazy_ref.fetch() for lazy_ref in root.children]
			# for child in root.children:
			dict={}
			tree = service.dfs(root,dict)
			app.logger.info(json.dumps(tree))
			# tree = service.recursive_children(root, json.loads(root.to_json()))
			return Response(json.dumps([tree]), mimetype="application/json", status=200)
		else:
			taxon_nodes = TaxonNode.objects().to_json()
			return Response(taxon_nodes, mimetype="application/json", status=200)

	def delete(self):
		taxon_nodes = TaxonNode.objects.delete()
		return '', 200
 
class TaxonNodeApi(Resource):

	def get(self, tax_id):
		try:
			taxon_node = TaxonNode.objects(tax_id=tax_id).first()
			###fetch references
			children_dict = {}
			children_dict['children'] = [lazy_ref.fetch().to_json() for lazy_ref in taxon_node.children]
			app.logger.info(children_dict)
			return Response(json.dumps(children_dict), mimetype="application/json", status=200)
		except DoesNotExist:
			raise UserNotFoundError

	def delete(self, tax_id):
		taxonNode = TaxonNode.objects.get(tax_id=tax_id).delete()
		return '', 200
