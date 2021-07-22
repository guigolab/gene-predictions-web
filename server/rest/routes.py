from .user import UsersApi, UserApi
from .taxon_node import TaxonNodeApi, TaxonNodesApi
from .taxon_files import TaxonFilesApi, TaxonFileApi

def initialize_routes(api):
	api.add_resource(UsersApi, '/users')
	api.add_resource(UserApi, '/users/<id>')
	api.add_resource(TaxonNodeApi, '/taxon-node/<tax_id>')
	api.add_resource(TaxonNodesApi, '/taxon-nodes','/taxon-nodes/<to_tree>')

	##is it a good practice to change endpoint between 2 related models?
	api.add_resource(TaxonFileApi, '/file/<name>')
	api.add_resource(TaxonFilesApi, '/files/<tax_id>')
