from .taxon_node import TaxonNodesApi
from .taxon_files import TaxonFilesApi, TaxonFileApi
from .geneid_server import GeneIdServerApi
from .tree_api import TreeApi
from .data_input_api import InputDataApi

def initialize_routes(api):
	api.add_resource(InputDataApi, '/api/input/<tax_id>') ##data input endpoint

	# api.add_resource(TaxonNodeApi, '/api/taxon-node/<tax_id>')
	api.add_resource(TaxonNodesApi, '/api/taxon-nodes') 

	api.add_resource(TaxonFileApi, '/api/file/<name>') ##download file by name
	api.add_resource(TaxonFilesApi, '/api/files','/api/files/<tax_id>') ## get all files of a taxon

	api.add_resource(GeneIdServerApi, '/api/geneid') ##geneid web server

	api.add_resource(TreeApi, '/api/tree','/api/tree/<node>') 


