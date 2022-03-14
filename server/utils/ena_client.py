import requests

def get_taxon_from_ena(taxon_id):
    response = requests.get(f"https://www.ebi.ac.uk/ena/browser/api/xml/{taxon_id}?download=false") ## 
    if response.status_code != 200:
        return
    # if response.is_json:
    return response.content