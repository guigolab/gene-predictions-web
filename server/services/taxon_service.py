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
        if node['scientificName'] == 'root' or node['scientificName'] == 'cellular organisms':
            continue
        # and node['scientificName'] not in ['root', 'cellular organism']
        # if ('rank' in node.keys() and node['rank'] in utils.RANKS) or node['taxId'] == 1:
        taxon_node = TaxonNode.objects(taxid=node['taxId']).first()
        if not taxon_node:
            rank = node['rank'] if 'rank' in node.keys() else 'other'
            taxon_node = TaxonNode(taxid=node['taxId'], name=node['scientificName'], rank=rank).save()
        taxon_lineage.append(taxon_node)
    #create relationship
    create_relationship(taxon_lineage)
    return taxon_lineage

def delete_taxons(lineage):
    taxons = [tax.fetch() for tax in lineage]
    leaves_counter(taxons)
    for taxon in taxons:
        if taxon.leaves < 2:
            app.logger.info(TaxonNode.objects(children=taxon.id).update_one(pull__children=taxon.id))
            taxon.delete()

#put species and subspecies at the same level for navigation purpose
def create_relationship(lineage):
    for index in range(len(lineage)-1):
        child_taxon = lineage[index]
        father_taxon = lineage[index + 1]
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
