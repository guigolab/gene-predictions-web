from db.models import Organism, TaxonFile,FileType
from services import organism_service


def delete_file(name):
    tax_file = TaxonFile.objects(name=name).first()
    organism = Organism.objects(taxid=tax_file.taxid)
    if tax_file.type == FileType.FASTA:
        organism.update(fastas__pull=tax_file.id)
    elif tax_file.type == FileType.GFF:
        organism.update(gffs__pull=tax_file.id)
    else:
        organism.update(params__pull=tax_file.id)
    