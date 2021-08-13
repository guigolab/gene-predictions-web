from posixpath import dirname
import subprocess
import tempfile
from db.models import TaxonFile
from flask import current_app as app




def launch_geneid(data,files):
        with tempfile.NamedTemporaryFile(mode='w+',suffix='.fasta', dir='/tmp') as fasta, tempfile.NamedTemporaryFile(mode='w+',suffix='.gff', dir='/tmp') as gff, tempfile.NamedTemporaryFile(mode='wb',suffix='.param', dir='/tmp') as param,tempfile.NamedTemporaryFile(mode='wb',prefix='output', dir='/tmp') as output:
            if not files:
                if data['fastaText']:
                    fasta.write(data['fastaText']) 
                if data['gffText']:
                    gff.write(data['gffText'])
            else:
                for key in files.keys():
                    if key == 'fastaFile':
                        files[key].save(fasta.name)
                    if key == 'gffFile':
                        files[key].save(gff.name)
            param_file = TaxonFile.objects(name=data['selectedParam']).first()
            param.write(param_file.file.read())
            args = ("/soft/GeneID/geneid_1.2/bin/geneid", "-P", param.name,'-G','-R' ,gff.name, fasta.name, )
            ##should check if works on windows machines
            popen = subprocess.Popen(args, stdout=subprocess.PIPE)
            popen.wait()
            output.write(popen.stdout.read())
            if data['graphicalRap']:
                args = ("/soft/GeneID/geneid_1.2/bin/gff2ps", '/soft/GeneID/geneid_1.2/bin/gff2ps.param',"--", output.name)
                popen = subprocess.Popen(args, stdout=subprocess.PIPE)
                popen.wait()
                app.logger.info(popen.stdout.read())
