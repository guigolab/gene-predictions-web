from flask import Response, request
from flask import current_app as app
from db.models import TaxonFile
from flask_restful import Resource
import services.geneid_service as service
from mongoengine.errors import ValidationError
from errors import InternalServerError, SchemaValidationError
import json



class GeneIdServerApi(Resource):
    #get param files for formulary
    def get(self):
        try:
            taxon_files = TaxonFile.objects(type="param")
            taxon_names=[]
            for file in taxon_files:
                data={}
                data['text'] = file.taxon.name ##need to dereference taxon
                data['value'] = file.name
                taxon_names.append(data)
            return Response(json.dumps([taxon_names]), mimetype="application/json", status=200)
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError

    def post(self):
        try:
            app.logger.info(request.form)
            data = request.form
            files = request.files
            # fasta = request.files.getlist('fastaFile')
            # gff = request.files.getlist('gffFile')
            # app.logger.info(fasta[0].read())
            # app.logger.info(gff[0].read())
            # body = request.get_json()
            service.launch_geneid(data,files)
            # file = request.files.get('file')
            # data = json.loads(request.form['json'])
            # taxon_files = TaxonFile(**data, file=file, taxon = taxon).save()
            return  201
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError
