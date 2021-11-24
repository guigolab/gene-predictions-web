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

def programs_configs(data,files):
    geneid_result = GeneIdResults()
    param = create_tempfile('param')
    options = geneid_options(data,geneid_result,param)
    app.logger.info(data.keys())
    if 'fastaFile' in files.keys():
        app.logger.info('fastafile')
        fasta = create_tempfile('fasta')
        files['fastaFile'].save(fasta.name)
    elif 'fastaText' in data.keys():
        fasta = create_tempfile('fasta')
        fasta.write(data['fastaText'].encode())
        fasta.seek(0)
    if 'gffFile' in files.keys():
        gff = create_tempfile('gff')
        files['gffFile'].save(gff.name)
    elif 'gffText' in data.keys():
        gff = create_tempfile('gff')
        gff.write(data['gffText'].encode())
        gff.seek(0)
    else:
        gff = None
    if 'selectedMode' in data.keys() and gff and gff.name:
        # if gff and gff.name:
        app.logger.info('SELECT MODE IS')
        app.logger.info(data['selectedMode'])
        cmd = '-R' if data['selectedMode'] == 'normal' or data['selectedMode'] == '-o' else data['selectedMode']
        options.extend([cmd, gff.name])
        # else:
        #     options.append(data['selectedMode'])
    if 'graphicalRap' in data.keys():
        psfile = create_tempfile('ps')
    # for key in files.keys():
    #     if key == 'fastaFile':
    #         fasta = create_tempfile('fasta')
    #         files[key].save(fasta.name)
    #     elif key == 'gffFile':
    #         gff = create_tempfile('gff')
    #         files[key].save(gff.name)
    # for key in data.keys():
    #     if key == 'fastaText':
    #         fasta = create_tempfile('fasta')
    #         fasta.write(data[key].encode())
    #         fasta.seek(0)
    #     elif key == 'gffText':
    #         gff = create_tempfile('gff')
    #         gff.write(data[key].encode())
    #         gff.seek(0)
    #     elif key == 'selectedMode':
    #         if gff and gff.name:
    #             cmd = '-R' if data[key] == 'normal' or data[key] == '-o' else data[key]
    #             options.extend([cmd, gff.name])
    #         else:
    #             options.append(data[key])
    #     elif key == 'graphicalRap':
    #         psfile = create_tempfile('ps')
    ##run geneid
    app.logger.info(options)
    fasta.seek(0)
    options.append(fasta.name)
    geneid_result.geneid_cmd = ' '.join(options)
    output = create_tempfile('stdout')
    app.logger.info('before launching geneid')
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
        app.logger.info('AFTER GFF2PS')
        args = ('convert', '-rotate', '90', psfile.name, jpg.name)
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
        geneid_result.save() 
    except Exception as e:
        app.logger.error(e)
    return geneid_result
    
def launch_geneid(options):
    app.logger.info("LAUNCHING GENEID...")
    app.logger.info(options)
    ##should check if works on windows machines
    popen = subprocess.Popen(tuple(options), stdout=subprocess.PIPE)
    popen.wait()
    return popen.stdout.read()

def launch_gff2ps(output):
    args = (GFF2PS,'-C',GFF2PS_PARAM, output.name)
    app.logger.info("LAUNCHING GFF2PS...")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    return popen.stdout.read()

def geneid_options(data,geneid_model,param):
    options= []
    options.append(GENEID)
    param_file = TaxonFile.objects(name=data['selectedParam']).first()
    geneid_model.param_species = param_file.organism.fetch().name ## name field is required
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

