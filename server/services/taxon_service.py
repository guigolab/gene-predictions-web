from lxml import etree
import requests
from db.models import TaxonNode,Organism
from flask import current_app as app
from utils import utils

# from mongoengine.queryset.visitor import Q
## create a service to retrieve lineage from taxon_id and create taxon_nodes from that
## check http://etetoolkit.org/docs/latest/tutorial/tutorial_ncbitaxonomy.html

RANKS = ['root','superkingdom','kingdom','phylum','class','order','family','genus','species','subspecies']
LINEAGE_KEY = 'lineage_list'
DTOL_LIMIT=100

def create_taxons_from_lineage(lineage):
    taxon_lineage = []
    for node in lineage:
        if ('rank' in node.keys() and node['rank'] in utils.RANKS) or node['taxId'] == 1:
            taxon_node = TaxonNode.objects(taxid=node['taxId']).first()
            if not taxon_node:
                taxon_node = TaxonNode(taxid=node['taxId'], name=node['scientificName'], rank=node['rank']).save()
            taxon_lineage.append(taxon_node)
    #create relationship
    create_relationship(taxon_lineage)
    return taxon_lineage

#put species and subspecies at the same level for navigation purpose
def create_relationship(lineage):
    for index in range(len(lineage)-1):
        child_taxon = lineage[index]
        father_taxon = lineage[index + 1] if child_taxon.rank != 'subspecies' else lineage[index+2]
        if not any(child_node.id == child_taxon.id for child_node in father_taxon.children):
            father_taxon.children.append(child_taxon)
            father_taxon.save()
        else:
            continue

def leaves_counter(lineage_list):
    for node in lineage_list:
        # node.leaves=count_species(node)
        node.leaves=Organism.objects(taxon_lineage=node.id, taxid__ne=node.taxid).count()
        node.save()


# def create_data(taxid):
#     organism = Organism.objects(taxonId = taxid).first()
#     if not organism:
#         app.logger.info('INSIDE')
#         taxons = get_species(taxid)
#         taxon_lineage = create_taxons(taxons)
#         create_children(taxon_lineage)
#         taxon = TaxonNode.objects(taxonId = taxid).first()
#         organism = Organism(taxonId=taxid, name = taxon.name, taxon_lineage=taxon_lineage).save()
#         leaves_counter(organism.taxon_lineage)
#     return organism

# def get_species(taxid):
#     response = requests.get(f"https://www.ebi.ac.uk/ena/browser/api/xml/{taxid}?download=false")
#     root= etree.fromstring(response.content)
#     taxons = [] 
#     taxons.append(root[0].attrib)
#     for taxon in root[0]:
#         if(taxon.tag == 'lineage'):
#             for node in taxon:
#                 taxons.append(node.attrib)
#     return taxons

# def leaves_counter(lineage_list):
#     for node in lineage_list:
#         tax_node = node.fetch()
#         tax_node.leaves=count_species(tax_node)
#         tax_node.save()

# def create_taxons(lineage):
#     taxon_lineage = []
#     for taxon in lineage:
#         taxid = int(taxon['taxId'])
#         if ('rank' in taxon.keys() and taxon['rank'] in RANKS) or taxid == 1:
#             taxon_node = TaxonNode.objects(taxonId=taxid).first()
#             if not taxon_node:
#                 if taxid == 1:
#                     taxon_node = TaxonNode(taxonId=taxid, name=taxon['scientificName']).save()
#                 else:
#                     taxon_node = TaxonNode(taxonId=taxid, name=taxon['scientificName'], rank=taxon['rank']).save()
#             taxon_lineage.append(taxon_node)
#     return taxon_lineage

# def create_children(lineage):
#     app.logger.info(lineage)
#     for index in range(len(lineage)-1):
#         child_taxon = lineage[index]
#         father_taxon = lineage[index + 1]
#         if not any(child_node.id == child_taxon.id for child_node in father_taxon.children):
#             father_taxon.children.append(child_taxon)
#             father_taxon.save()
#         else:
#             continue

# def count_species(tax_node):
#     leaves = 0
#     if not tax_node:
#         return 0
#     elif len(tax_node.children) == 0:
#         return 1
#     else:
#         for child in [lazy_ref.fetch() for lazy_ref in tax_node.children]:
#             leaves += count_species(child)
#         return leaves

# def bfs(root,nodes):
#     queue = [(root,0)]
#     while queue:
#         node, level = queue.pop(0)
#         if level == 0:
#             nodes[level] = 1
#         if node.children:
#             for child in node.children:
#                 queue.append((child, level+1))
#                 nodes[level+1] = nodes.setdefault(level+1, 0) + 1
#         if nodes[level] > DTOL_LIMIT:
#             return level-1

# def dfs(stack, tree, max_level):
#     node, level = stack.pop(0)
#     tree["name"] = node.name
#     tree["isOpen"] = True
#     tree["children"] = []
#     tree['rank'] = node.rank
#     tree['leaves'] = node.leaves
#     if max_level and max_level <= level:
#         return
#     if node.children:
#         childrens = [lazy_ref.fetch() for lazy_ref in node.children]
#         for child in childrens:
#             child_dict = {}
#             dfs([(child, level+1)], child_dict, max_level)
#             tree["children"].append(child_dict)
#     return tree

# def get_max_level(counts, limit):
#     for level, nodes in counts.items():
#         if nodes > limit:
#             return level-1

# def create_tree(node):
#     node_counts={}
#     max_level = bfs(node,node_counts)
#     tree={}
#     dfs([(node,0)],tree,max_level)
#     return tree