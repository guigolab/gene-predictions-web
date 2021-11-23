from os import name
from flask import Response, request
from flask import current_app as app
from db.models import Organism, TaxonFile, TaxonNode
from flask_restful import Resource
import services.taxon_service as service
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from errors import InternalServerError, SchemaValidationError, UserNotFoundError, EmailAlreadyExistError
import json



class TaxonFilesApi(Resource):
    #get files of a taxon
    def get(self):
        try:
            params = request.args
            tax_id = params.get('taxId')
            type= params.get('type')
            if tax_id:
                organism = Organism.objects(taxonId=tax_id).first()
                taxon_files= TaxonFile.objects(organism = organism)
            elif type:
                taxon_files = TaxonFile.objects(type=type)
            else:
                taxon_files = TaxonFile.objects()
            return Response(taxon_files.to_json(), mimetype="application/json", status=200)
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError
    #delete files of a taxon
    def delete(self,tax_id):
        # taxon = TaxonNode.objects(tax_id=tax_id).first()
        taxon_files= TaxonFile.objects().delete()
        return '', 200

    # def post(self,tax_id):
    #     try:
    #         taxon = service.return_taxon(tax_id)
    #         file = request.files.get('file')
    #         data = json.loads(request.form['json'])
    #         taxon_files = TaxonFile(**data, file=file, taxon = taxon).save()
    #         return  201
    #     except ValidationError:
    #         raise SchemaValidationError
    #     except Exception as e:
    #         app.logger.error(e)
    #     raise InternalServerError


class TaxonFileApi(Resource):
    ##download file by name
    def get(self, name):
        try:
            taxon_file = TaxonFile.objects(name=name).first()
            file = taxon_file.file.read()
            content_type = taxon_file.file.content_type
            return Response(file, content_type=content_type, status=200)
        except NotUniqueError:
            raise EmailAlreadyExistError
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError
    
    # def delete(self,name):
    #     file = TaxonFile.objects(name=name).delete()
    #     return '',200

    # def get(self,name):
    #     try:
    #         # tmp_file = "tmp.txt"
    #         # taxon_file = TaxonFile.objects(name=name).first()
    #         # to_json={}
    #         # arr=[{'id': "gene 1", 'start': 10000, 'end': 20000, 'strand': 1}]
    #         # # with open(tmp_file,'wb') as tmp:
    #         # #     tmp.write(taxon_file.file.read())
    #         # #     for rec in GFF.parse(tmp_file):
    #         # #         for gene in rec.features:
    #         # #             track={}
    #         # #             track["id"] = gene.id
    #         # #             track["start"] = gene.location._start.position
    #         # #             track["end"] = gene.location._end.position
    #         # #             track["strand"] = gene.location._strand
    #         # #         arr.append(track)
    #         # #     to_json['content'] = arr
    #         # return Response(json.dumps(arr), mimetype="application/json", status=200)
    #     except NotUniqueError:
    #         raise EmailAlreadyExistError
    #     except ValidationError:
    #         raise SchemaValidationError
    #     except Exception as e:
    #         app.logger.error(e)
    #     raise InternalServerError  