from flask import request
from flask import current_app as app
from db.models import TaxonFile
from flask_restful import Resource
import services.taxon_service as service
from mongoengine.errors import ValidationError
from errors import InternalServerError, SchemaValidationError
import json

class InputDataApi(Resource):
    def post(self,tax_id):
        try:
            taxon = service.return_taxon(tax_id)
            file = request.files.get('file')
            data = json.loads(request.form['json'])
            TaxonFile(**data, file=file, taxon = taxon).save()
            return  201
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError