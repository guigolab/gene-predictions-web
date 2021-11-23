from flask import request, Response
from flask import current_app as app
from db.models import TaxonFile,TaxonNode,Organism
from flask_restful import Resource
import services.taxon_service as service
from mongoengine.errors import ValidationError
from errors import InternalServerError, SchemaValidationError
import json

class InputDataApi(Resource):
    def post(self):
        try:
            file = request.files.get('file')
            data = json.loads(request.form.get('json'))
            app.logger.info(data)
            app.logger.info(file)
            organism = service.create_data(int(data['taxid']))
            type = data['file']['type']
            if TaxonFile.objects(name = data['file']['name']).first():
                return "filename already exists", 400
            elif type.lower() != 'gff':
                tax_file = TaxonFile(name = data['file']['name'], file = file, organism = organism, type=type.lower()).save()
                return Response(tax_file.to_json(), mimetype="application/json", status=200)
            # app.logger.info(request.files)
            # data = request.__dict__
            # organism = service.create_data(data)
            # taxon = service.return_taxon(tax_id)
            # file = request.files.get('file')
            # data = json.loads(request.form['json'])
            # tax_file = TaxonFile.objects(name=data['name']).first()
            # if tax_file:
            #     return "filename already exists", 400
            # else:
            #     TaxonFile(**data, file=file, taxon = taxon).save()
            #     return  201
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError
    
    def delete(self):
        TaxonNode.drop_collection()
        Organism.drop_collection()
        TaxonFile.drop_collection()
        return 200
