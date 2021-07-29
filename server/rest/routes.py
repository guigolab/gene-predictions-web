from .taxon_node import TaxonNodeApi, TaxonNodesApi
from .taxon_files import TaxonFilesApi, TaxonFileApi

def initialize_routes(api):
	api.add_resource(TaxonNodeApi, '/api/taxon-node/<tax_id>')
	api.add_resource(TaxonNodesApi, '/api/taxon-nodes','/api/taxon-nodes/<to_tree>')

	##is it a good practice to change endpoint between 2 related models?
	api.add_resource(TaxonFileApi, '/api/file/<name>')
	api.add_resource(TaxonFilesApi, '/api/files/<tax_id>')
