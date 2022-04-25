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

