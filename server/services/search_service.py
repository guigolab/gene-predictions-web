from enum import Enum
from flask import json
from flask import current_app as app
from mongoengine.queryset.visitor import Q
from db.models import TaxonNode
from utils.common_functions import resolve_params

DefaultParams = {
    'sortOrder': '',
    'sortColumn': '',
    'taxName': 'Eukaryota',
    'status': ' '
}
FilterParams = { **DefaultParams,
    'from': 0,
    'size': 20,
    'filter': '',
}

QueryParams = {
    **DefaultParams,
    'limit': 20,
    'offset': 0,
}

##when filter is present we trigger FTS
def full_text_search(params,model):
    json_resp = {}
    resolved_params = resolve_params(FilterParams,**params)
    app.logger.info(resolved_params)
    # #tax name param always present, Eukaryota by default
    tax_node = TaxonNode.objects(name=resolved_params['taxName']).first()
    query_tax = query_by_taxNode(tax_node)
    query = query_by_taxid(resolved_params['filter']) if resolved_params['filter'].isnumeric() else query_by_name(resolved_params['filter'])
    organisms = model.objects(query_tax & query)
    if resolved_params['sortColumn']:
        sort = '-'+resolved_params['sortColumn'] if resolved_params['sortOrder'] == 'true' else resolved_params['sortColumn']
        organisms = organisms.order_by(sort)
    json_resp['total'] = organisms.count()
    json_resp['data'] = organisms[int(resolved_params['from']):int(resolved_params['from'])+int(resolved_params['size'])].as_pymongo()
    return json.dumps(json_resp)

def query_by_taxNode(taxNode):
    return Q(taxon_lineage=taxNode)

def query_by_name(filter):
    return (Q(name__iexact=filter) | Q(name__icontains=filter) | Q(common_name__iexact=filter) | Q(common_name__icontains=filter))

def query_by_taxid(filter):
    return (Q(taxid__iexact=filter) | Q(taxid__icontains=filter))

##filter is not present
def default_query_params(params,model):
    json_resp = {}
    resolved_params = resolve_params(QueryParams, **params)
    tax_node = TaxonNode.objects(name=resolved_params['taxName']).first()
    query_tax = query_by_taxNode(tax_node)
    organisms = model.objects(query_tax)
    if resolved_params['sortColumn']:
        sort = '-'+resolved_params['sortColumn'] if resolved_params['sortOrder'] == 'true' else resolved_params['sortColumn']
        organisms = organisms.order_by(sort)
    json_resp['total'] = organisms.count()
    json_resp['data'] = organisms[int(resolved_params['offset']):int(resolved_params['limit'])+int(resolved_params['offset'])].as_pymongo()
    return json.dumps(json_resp)
