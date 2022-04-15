import services.search_service as service
from utils import pipelines
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
			# response = json.loads(organism.to_json())
			# # response['taxon_lineage'] = [json.loads(lazy_ref.fetch().to_json()) for lazy_ref in organism.taxon_lineage]
			# response['files'] = FileModel.objects(taxid=organism.taxid).as_pymongo()
			# app.logger.info(response)
			# response['samples'] = [json.loads(lazy_ref.fetch().to_json()) for lazy_ref in organism.samples]
			return Response(json.dumps(organism),mimetype="application/json", status=200)
		except DoesNotExist:
			raise NotFound

