from ast import Index
from logging import error
from ete3 import NCBITaxa
from db.models import TaxonNode
from flask import current_app as app
import os
## create a service to retrieve lineage from taxon_id and create taxon_nodes from that
## check http://etetoolkit.org/docs/latest/tutorial/tutorial_ncbitaxonomy.html

def insert_taxons_from_lineage(tax_id):
        taxa_db = NCBITaxa()
        lineage = taxa_db.get_lineage(tax_id)
        for node in lineage:
            if TaxonNode.objects(tax_id=str(node)).first():
                continue
            else:
                taxon_node = TaxonNode(tax_id=str(node), name=taxa_db.get_taxid_translator([node]).get(node))
                taxon_node.save()
        return lineage

# creating the children bottom up direction
def create_children(lineage):
    rev_lineage = list(reversed(lineage))
    for index in range(len(rev_lineage)-1):
        next_taxid = str(rev_lineage[index + 1])
        taxon = TaxonNode.objects(tax_id=str(rev_lineage[index])).first()
        father_taxon = TaxonNode.objects(tax_id=next_taxid).first()
        if not any(child_node.id == taxon.id for child_node in father_taxon.children):
            father_taxon.children.append(taxon)
            father_taxon.save()
        else:
            continue

def return_taxon(tax_id):
    taxon = TaxonNode.objects(tax_id=tax_id).first()
    if taxon:
        return TaxonNode.objects(tax_id=tax_id).first()
    else:
        lineage = insert_taxons_from_lineage(tax_id) ## we insert every node from species to root around 30
        create_children(lineage)
        taxon = TaxonNode.objects(tax_id=tax_id).first()
        return taxon
