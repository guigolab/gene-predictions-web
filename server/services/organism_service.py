from db.models import Organism
from utils import ena_client,utils
from services import taxon_service
from errors import NotFound
from flask import current_app as app


def get_or_create_organism(taxid):
    organism = Organism.objects(taxid=taxid).first()
    if not organism:
        taxon_xml = ena_client.get_taxon_from_ena(taxid)
        if not taxon_xml:
            print('TAXID NOT FOUND')
            print(taxid)
            raise NotFound
        lineage = utils.parse_taxon(taxon_xml)
        species = lineage[0]
        taxon_lineage = taxon_service.create_taxons_from_lineage(lineage)
        taxon_list = [dict(taxid=tax.taxid,rank=tax.rank,name=tax.name) for tax in taxon_lineage]
        common_name = species['commonName'] if 'commonName' in species.keys() else ''
        organism = Organism(taxid = taxid, name = species['scientificName'], common_name=common_name, ordered_lineage = taxon_list, taxon_lineage = taxon_lineage).save()
        taxon_service.leaves_counter(taxon_lineage)
    return organism


def delete_organisms(taxids):
    organisms_to_delete = Organism.objects(taxid__in=taxids)
    deleted_organisms=list()
    for organism in organisms_to_delete:
        taxon_service.delete_taxons(organism.taxon_lineage)
        name = organism.organism
        organism.delete()
        deleted_organisms.append(name)
    return deleted_organisms