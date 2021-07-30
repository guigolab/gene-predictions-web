from ast import Index
from logging import error
from ete3 import NCBITaxa
from db.models import TaxonNode
from flask import current_app as app
import os
import json
## create a service to retrieve lineage from taxon_id and create taxon_nodes from that
## check http://etetoolkit.org/docs/latest/tutorial/tutorial_ncbitaxonomy.html

def insert_taxons_from_lineage(tax_id):
        taxa_db = NCBITaxa()
        lineage = taxa_db.get_lineage(tax_id)
        names = taxa_db.get_taxid_translator(lineage)
        lineage_names = [names[taxid] for taxid in lineage]
        for node in lineage:
            str_node= str(node)
            taxon_node = TaxonNode.objects(tax_id=str_node).first()
            if taxon_node:
                continue
            else:
                taxon_node = TaxonNode(tax_id=str_node,lineage=lineage_names ,name= taxa_db.get_taxid_translator([node]).get(node))
                taxon_node.save()
        return lineage

# creating the children bottom up direction
def create_children(lineage):
    rev_lineage = list(reversed(lineage))
    for index in range(len(rev_lineage)-1):
        child_taxid = str(rev_lineage[index])
        father_taxid = str(rev_lineage[index + 1])
        child_taxon = TaxonNode.objects(tax_id=child_taxid).first()
        father_taxon = TaxonNode.objects(tax_id=father_taxid).first()
        if not any(child_node.id == child_taxon.id for child_node in father_taxon.children):
            father_taxon.children.append(child_taxon)
            father_taxon.save()
        else:
            continue

def return_taxon(tax_id):
    taxon = TaxonNode.objects(tax_id=tax_id).first()
    if not taxon:
        lineage = insert_taxons_from_lineage(tax_id) ## we insert every node from species to root around 30
        create_children(lineage)
        taxon = TaxonNode.objects(tax_id=tax_id).first()
    taxon.update(has_files=True)            
    return taxon

# def recursive_children(node,tree):
#     if node.children:
#         node.children = [lazy_ref.fetch() for lazy_ref in node.children]
#         for child in node.children:
#             tree['children'].append(recursive_children(child, json.loads(child.to_json())))
#     else:
#         tree['children'].append(json.loads(node.to_json()))
#     return tree

## convert taxons in tree structure dictionary
def dfs(node, tree):
    tree["name"] = node.name
    tree["taxid"] = node.tax_id   ## should pass client attributes setting in vue model
    tree["has_files"] = node.has_files
    tree["isOpen"] = False
    tree["children"] = []
    if node.children:
        node.children = [lazy_ref.fetch() for lazy_ref in node.children]
        for child in node.children:
            child_dict = {}
            dfs(child, child_dict)
            tree["children"].append(child_dict)
    tree["leaves"] = count_leaves(tree)
    if len(tree["children"]) == 1:
        tree["isOpen"] = True
    return tree

def count_leaves(tree):
    leaves = 0
    if not tree:
        return 0
    elif len(tree["children"]) == 0:
        return 1
    else:
        for child in tree["children"]:
            leaves += count_leaves(child)
        return leaves