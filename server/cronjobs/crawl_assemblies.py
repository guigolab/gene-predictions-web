# import requests
# from lxml import etree


# # PRJEB33226 25 genomes
# # PRJEB40665 DTOL
# # PRJNA489243 VGP
# # PRJNA312960 200 Mammals
# # PRJNA512907 DNA Zoo

# def parse_related_projects(root_xml):
#     secondary_projects = list()
#     related_projects = root_xml.findall('.//RELATED_PROJECTS')
#     if related_projects:
#         for project in related_projects[0]:
#             if project[0].tag == 'CHILD_PROJECT':
#                 secondary_projects.append(project[0].attrib['accession'])
#     return secondary_projects

# def get_xml(accession):
#     resp = requests.get(f'https://www.ebi.ac.uk/ena/browser/api/xml/{accession}?download=true')
#     return etree.fromstring(resp.content)

# def get_chromosomes_and_taxon(project_accession, taxons):
#     resp = requests.get(f'https://www.ebi.ac.uk/ena/portal/api/links/study?accession={project_accession}&format=JSON&result=assembly')
#     if resp.status_code != 200:
#         return 
#     else:
#         for assembly in resp.json():
#             ass_xml = get_xml(assembly['accession'])
#             for el in ass_xml[0]:
#                 if el.tag == 'CHROMOSOMES':
#                     taxon = dict()
#                     taxon['assembly'] = assembly['accession'] 
#                     taxon['chromosomes'] = get_chromosomes(el)
#                     taxon_tag = ass_xml[0].find('TAXON')
#                     taxon['taxid'] = taxon_tag.find('TAXON_ID').text
#                     taxon['name'] = taxon_tag.find('SCIENTIFIC_NAME').text
#                     if not any(tax['taxid'] == taxon['taxid'] for tax in taxons):
#                         file_name = taxon['taxid']+'.txt'
#                         full_name = os.path.join(PATH,file_name)
#                         file = open(full_name, "w")
#                         file.write(taxon)
#                         file.close()
#         return
                
# def get_chromosomes(element):
#     chromosomes = list()
#     for t in element:
#         chromosomes.append(t.attrib['accession'])
#     return chromosomes

# def find_organism_infos(element):
#     organism = element.findall('.//TAXON')
#     if organism:
#         return organism
#     else:
#         if len(element) > 0:
#             for el in element:
#                 find_organism_infos(el)
#         else:
#             return

# def crawl_assemblies(project_accession, taxons):
#     project = get_xml(project_accession)
#     related_projects = parse_related_projects(project)
#     if related_projects:
#         for pr in related_projects:
#             crawl_assemblies(pr,taxons)
#     else:
#         get_chromosomes_and_taxon(project_accession, taxons) 




# taxons = list()
# crawl_assemblies("$accession", taxons)