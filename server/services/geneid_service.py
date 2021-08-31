import os
import subprocess
import tempfile
from db.models import TaxonFile,GeneIdResults
from flask import current_app as app

GFF2PS = '/soft/GeneID/geneid_1.2/bin/gff2ps'
GFF2PS_PARAM= '/soft/GeneID/geneid_1.2/bin/gff2ps.param'
GENEID = '/soft/GeneID/geneid_1.2/bin/geneid'


def create_tempfile(suffix,**kwargs):
    return tempfile.NamedTemporaryFile(suffix='.'+suffix,dir='/tmp',**kwargs)

# def generate(geneid_result):
#     if geneid_result.jpg:
#         yield geneid_result.jpg
#     app.logger.info('request started')
#     for file in output_files:
#         yield file
#         file.close()
#     app.logger.info('request finished')
#     yield ''

def programs_configs(data,files):
    geneid_result = GeneIdResults()
    param = create_tempfile('param')
    options = geneid_options(data,geneid_result,param) 
    for key in files.keys():
        if key == 'fastaFile':
            fasta = create_tempfile('fasta')
            files[key].save(fasta.name)
        elif key == 'gffFile':
            gff = create_tempfile('gff')
            files[key].save(gff.name)
    for key in data.keys():
        if key == 'fastaText':
            fasta = create_tempfile('fasta')
            fasta.write(data[key].encode())
            fasta.seek(0)
        elif key == 'gffText':
            gff = create_tempfile('gff')
            gff.write(data[key].encode())
            gff.seek(0)
        elif key == 'selectedMode':
            if gff.name:
                cmd = '-R' if data[key] == 'normal' or data[key] == '-o' else data[key]
                options.extend([cmd, gff.name])
            else:
                options.append(data[key])
        elif key == 'graphicalRap':
            psfile = create_tempfile('ps')
    ##run geneid
    options.append(fasta.name)
    app.logger.info(options)
    geneid_result.geneid_cmd = ' '.join(options)
    output = create_tempfile('stdout')
    output.write(launch_geneid(options))
    param.close()
    output.seek(0)
    fasta.close()
    if gff:
        gff.close()
    if psfile:
        jpg = create_tempfile('jpg')
        ##run gff2ps
        psfile.write(launch_gff2ps(output))
        args = ('convert', '-rotate', '90', psfile.name,jpg.name)
        # os.system('convert -rotate 90 ' + psfile.name + ' ' + jpg.name) #convert ps to jpg 
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        psfile.seek(0)
        geneid_result.ps.put(psfile, content_type='application/PostScript', filename=psfile.name)
        geneid_result.jpg.put(jpg, content_type='image/jpg', filename=jpg.name)
        psfile.close()
        jpg.close()
    try:
        with open(output.name, 'r') as output:
            geneid_result.output = "\n".join(output.readlines())
            app.logger.info(geneid_result.output)
        geneid_result.save() 
    except Exception as e:
        app.logger.error(e)
    return geneid_result
    
def launch_geneid(options):
    ##should check if works on windows machines
    popen = subprocess.Popen(tuple(options), stdout=subprocess.PIPE)
    popen.wait()
    return popen.stdout.read()

def launch_gff2ps(output):
    args = (GFF2PS,'-C',GFF2PS_PARAM, output.name)
    popen = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
    popen.wait()
    return popen.stdout.read()

def geneid_options(data,geneid_model,param):
    options= []
    options.append(GENEID)
    param_file = TaxonFile.objects(name=data['selectedParam']).first()
    geneid_model.param_species = param_file.taxon.name ## name field is required
    param.write(param_file.file.read())
    options.append('-P')
    options.append(param.name) ##param tmpfile path
    if 'selectedOptions' in data:
        for value in data.getlist('selectedOptions'):
            if value:
                options.extend(value.split(","))
    if 'outputOption' in data:
        options.append(data['outputOption'])
    if 'selectedMode' in data and data['selectedMode'] == '-o':
        options.append(data['selectedMode'])  
    return options

