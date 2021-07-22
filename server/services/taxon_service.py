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
        for node in lineage:
            str_node= str(node)
            taxon_node = TaxonNode.objects(tax_id=str_node).first()
            if taxon_node:
                continue
            else:
                taxon_node = TaxonNode(tax_id=str_node, name= taxa_db.get_taxid_translator([node]).get(node))
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

def recursive_children(node,tree):
    if node.children:
        node.children = [lazy_ref.fetch() for lazy_ref in node.children]
        for child in node.children:
            app.logger.info(child.to_json())
            tree['children'].append(recursive_children(child, json.loads(child.to_json())))
    else:
        tree['children'].append(json.loads(node.to_json()))
    return tree
# def recursiveChildren(node,tree):
#     actual_tree = {'name': node.name, 'children':[]}
#     if node.children:
#         for child in node.children:
#             actual_tree['children'].extend(recursiveChildren(child),actual_tree)
#             actual_tree['children'].append(child.to_json())
#         tree['children'].append(actual_tree)
#     return tree
# def fetch_children(children):
#     children = [lazy_ref.fetch() for lazy_ref in root.children]
#     for child in children:
#     for child in root.children:
#         if child.children:
#             fetch_children(child)
#     return root
# def node_to_json(node):
#     json_node = json.loads(node.to_json())
#     if node.children:
#         json_node['children'] = [lazy_ref.fetch().to_json() for lazy_ref in node.children]
#     return json_node
# def formTree(children,tree):
#     if children:
#         tree = {'children': [lazy_ref.fetch().to_json() for lazy_ref in children]}
#         for child in children:
#             currTree = tree

#             for gson in child.children:
#                 if key not in currTree:
#                     currTree[key] = {}
#                 currTree = currTree[key]
                
#     return tree

# def create_tree(node):
#     if node.children:
#         node.children = get_children(node)
#         for child in node.children:
#             create_tree(child)
#     return node.to_json()


    # if taxon_node.children:
    #     tree.children = [lazy_ref.fetch() for lazy_ref in taxon_node.children]
    #     for child_node in taxon_node.children:
    #         create_tree(child_node,tree)
def dfs(node, tree):
    tree["name"] = node.name
    tree["children"] = []
    if node.children:
        node.children = [lazy_ref.fetch() for lazy_ref in node.children]
        for child in node.children:
            child_dict = {}
            dfs(child, child_dict)
            tree["children"].append(child_dict)
    return tree