import os
import subprocess
import tempfile
from db.models import TaxonFile
from flask import current_app as app

GFF2PS = '/soft/GeneID/geneid_1.2/bin/gff2ps'
GFF2PS_PARAM= '/soft/GeneID/geneid_1.2/bin/gff2ps.param'
GENEID = '/soft/GeneID/geneid_1.2/bin/geneid'

# def launch_geneid(data,files):
#     with tempfile.NamedTemporaryFile(mode='w+',suffix='.fasta', dir='/tmp') as fasta, tempfile.NamedTemporaryFile(mode='w+',suffix='.gff', dir='/tmp') as gff, tempfile.NamedTemporaryFile(mode='wb',suffix='.param', dir='/tmp') as param,tempfile.NamedTemporaryFile(suffix='.gff', dir='/tmp') as output:
#         if not files:
#             if data['fastaText']:
#                 fasta.write(data['fastaText']) 
#             if data['gffText']:
#                 gff.write(data['gffText'])
#         else:
#             for key in files.keys():
#                 app.logger.info(key)
#                 if key == 'fastaFile':
#                     files[key].save(fasta.name)
#                 if key == 'gffFile':
#                     files[key].save(gff.name)
#         param_file = TaxonFile.objects(name=data['selectedParam']).first()
#         param.write(param_file.file.read())
#         args = ("/soft/GeneID/geneid_1.2/bin/geneid", "-P", param.name,'-G','-R' , gff.name, fasta.name)
#         ##should check if works on windows machines
#         popen = subprocess.Popen(args, stdout=subprocess.PIPE)
#         popen.wait()
#         output.write(popen.stdout.read())
#         output.seek(0)
#         if data['graphicalRap']:
#             with tempfile.NamedTemporaryFile(suffix='.ps', dir='/tmp') as psfile, tempfile.NamedTemporaryFile(suffix='.jpg', dir='/tmp') as jpg:
#                 args = ("/soft/GeneID/geneid_1.2/bin/gff2ps",'-C','/soft/GeneID/geneid_1.2/bin/gff2ps.param', output.name)
#                 popen = subprocess.Popen(args, stdout=subprocess.PIPE)
#                 popen.wait()
#                 psfile.write(popen.stdout.read())
#                 psfile.seek(0)
#                 # args = ("ghostscript", psfile.name, jpg.name)
#                 # popen = subprocess.Popen(args, stdout=subprocess.PIPE)
#                 # popen.wait()
#                 # jpg_test = 'test.jpg'
#                 # # popen.stdout.read()
#                 # app.logger.info(psfile.name)
#                 os.system('convert -rotate 90 ' + psfile.name + ' ' + jpg.name)
#                 # os.system('convert -rotate 90 ' + psfile.name + ' ' + jpg.name)
#                 # psimage = Image.open(psfile.name)
#                 # app.logger.info("hello")
#                 # psimage.save(jpg.name)
#                 # args = ("convert", psfile.name, jpg.name)
#                 # popen = subprocess.Popen(args, stdout=subprocess.PIPE)
#                 # popen.wait()
#                 # popen.stdout.read()
#                 app.logger.info(jpg.read())

def create_tempfile(suffix,**kwargs):
    return tempfile.NamedTemporaryFile(suffix='.'+suffix,dir='/tmp',**kwargs)

# def generate(output_files):
#     app.logger.info('request started')
#     for file in output_files:
#         yield file
#         file.close()
#     app.logger.info('request finished')
#     yield ''

def programs_configs(data,files):
    output_files = []
    param = create_tempfile('param')
    options = geneid_options(data,param) 
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
            fasta.write(data[key])
        elif key == 'gffText':
            gff = create_tempfile('gff')
            gff.write(data[key])
        elif key == 'selectedMode':
            if gff.name:
                app.logger.info('inside gff')
                cmd = '-R' if data[key] == 'normal' or data[key] == '-o' else data[key]
                options.extend([cmd, gff.name])
            else:
                options.append(data[key])
        elif key == 'graphicalRap':
            psfile = create_tempfile('ps',delete=False)
    ##run geneid
    options.append(fasta.name)
    output = create_tempfile('stdout',delete=False)
    output.write(launch_geneid(options))
    output.seek(0)
    app.logger.info(output.read())
    output_files.append(output)
    fasta.close()
    if gff:
        gff.close()
    if psfile:
        jpg = create_tempfile('jpg',delete=False)
        ##run gff2ps
        psfile.write(launch_gff2ps(output))
        os.system('convert -rotate 90 ' + psfile.name + ' ' + jpg.name) #convert ps to jpg 
        output_files.extend([psfile,jpg])
    return output_files 
    
def launch_geneid(options):
    ##should check if works on windows machines
    app.logger.info(tuple(options))
    popen = subprocess.Popen(tuple(options), stdout=subprocess.PIPE)
    popen.wait()
    return popen.stdout.read()

def launch_gff2ps(output):
    args = (GFF2PS,'-C',GFF2PS_PARAM, output.name)
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    return popen.stdout.read()

def geneid_options(data,param):
    options= []
    options.append(GENEID)
    param_file = TaxonFile.objects(name=data['selectedParam']).first()
    param.write(param_file.file.read())
    options.append('-P')
    options.append(param.name) ##param tmpfile path
    if 'selectedOptions' in data:
        for opt in data['selectedOptions']:
            options.append(opt)
    if 'outputOption' in data:
        app.logger.info('outputOptions ')
        options.append(data['outputOption'])
    if 'selectedMode' in data and data['selectedMode'] == '-o':
        options.append(data['selectedMode'])  
    return options

