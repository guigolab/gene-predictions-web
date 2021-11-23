from .organisms import OrganismsApi,OrganismApi, OrganismsSearchApi
from .taxon_files import TaxonFilesApi, TaxonFileApi
from .geneid_server import GeneIdServerApi
from .tree_api import TreeApi,TaxNodesApi
from .data_input_api import InputDataApi

def initialize_routes(api):
	api.add_resource(InputDataApi, '/api/input') ##data input endpoint

	api.add_resource(OrganismsApi, '/api/root_organisms')
	api.add_resource(OrganismsSearchApi, '/api/root_organisms/search')
	api.add_resource(OrganismApi, '/api/root_organisms/<name>') 
	api.add_resource(TaxNodesApi, '/api/taxons/<name>')

	api.add_resource(TaxonFileApi, '/api/files/<name>') ##download file by name
	api.add_resource(TaxonFilesApi, '/api/files') ## get all files of a taxon

	api.add_resource(GeneIdServerApi, '/api/geneid', '/api/geneid/<id>') ##geneid web server

	api.add_resource(TreeApi,'/api/tree/<node>') 


