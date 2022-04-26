import services.search_service as service
from utils import pipelines,utils
from flask import Response, request
from db.models import Organism, FileModel
from flask_restful import Resource
from mongoengine.errors import DoesNotExist
from errors import NotFound
from flask import current_app as app
import json
# import json

class OrganismsApi(Resource):
	def get(self):
		return Response(service.default_query_params(request.args,Organism),mimetype="application/json", status=200)


class OrganismsSearchApi(Resource):
	def get(self):
		return Response(service.full_text_search(request.args,Organism),mimetype="application/json", status=200)

class OrganismApi(Resource):
	def get(self,name):
		try:
			organism = Organism.objects(name=name).aggregate(*pipelines.OrganismPipeline).next()
			utils.sort_lineage(organism['taxon_lineage']) #sort lineage (aggregation pipeline returns unordered list)
			return Response(json.dumps(organism),mimetype="application/json", status=200)
		except DoesNotExist:
			raise NotFound

