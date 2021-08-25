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

class TreeApi(Resource):
    def get(self, node):
        dict={}
        root = TaxonNode.objects(name = node).first()
        tree = service.dfs(root,dict)   
        return Response(json.dumps([tree]), mimetype="application/json", status=200)
 