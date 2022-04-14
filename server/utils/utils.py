from lxml import etree
# from .constants import CHECKLIST_PARSER
from flask import make_response,jsonify
import os

RANKS = os.getenv('RANKS').split(',')

MAX_NODES = os.getenv('MAX_NODES')

def parse_taxon(xml):
    root = etree.fromstring(xml)
    species = root[0].attrib
    lineage = []
    for taxon in root[0]:
        if taxon.tag == 'lineage':
            for node in taxon:
                lineage.append(node.attrib)
    lineage.insert(0,species)
    return lineage


#aggregation pipeline returns unordered list of taxon lineage
def sort_lineage(lineage):
    values_obj=dict()
    for idx, rank in enumerate(RANKS):
        values_obj[rank] = idx
    lineage.sort(key=lambda x: values_obj[x['rank']],reverse=True)
    return lineage



