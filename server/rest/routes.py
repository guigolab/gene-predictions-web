from .organisms import OrganismsApi,OrganismApi, OrganismsSearchApi
from .files_api import FilesModelApi
from .geneid_server import GeneIdServerApi
from .tree_api import TreeApi,TaxNodesApi
from .data_input_api import InputDataApi

def initialize_routes(api):

	api.add_resource(InputDataApi, '/api/input') ##data input endpoint

	api.add_resource(OrganismsApi, '/api/organisms')
	api.add_resource(OrganismsSearchApi, '/api/organisms/search')
	api.add_resource(OrganismApi, '/api/organisms/<name>')

	api.add_resource(TaxNodesApi, '/api/taxons/<name>')

	api.add_resource(FilesModelApi, '/api/files/<model>', '/api/<model>/<name>')

	api.add_resource(GeneIdServerApi, '/api/geneid','/api/geneid/<id>') ##geneid web server
	# api.add_resource(ResultFilesApi, '/api/results/<id>')
	api.add_resource(TreeApi,'/api/tree/<node>') 


