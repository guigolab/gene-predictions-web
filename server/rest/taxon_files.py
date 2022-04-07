from flask import Response, request, send_file
from flask import current_app as app
from db.models import TaxonFile, TaxonNode, TaxaFile
from flask_restful import Resource
from mongoengine.queryset.visitor import Q
# import services.taxon_service as service
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from errors import InternalServerError, NotFound, SchemaValidationError, Unauthorized, EmailAlreadyExistError
import os

API_KEY = os.getenv('SECRET_KEY')


class TaxonFilesApi(Resource):
    #get files of a taxon
    def get(self):
        # try:
        args = request.args
        if 'taxid' in args.keys():
            taxid = args['taxid']
            return Response(TaxaFile.objects(taxid=taxid).to_json())
        
            # tax_id = params.get('taxId')
            # type= params.get('type')
            # if tax_id and type:
            #     app.logger.info(TaxonFile.objects(Q(organism__taxonId = tax_id) & Q(type=type)))
            # elif tax_id:
            #     organism = Organism.objects(taxonId=tax_id).first()
            #     taxon_files= TaxonFile.objects(organism = organism)
            # elif type:
            #     taxon_files = TaxonFile.objects(type=type)
            # else:
        #     #     taxon_files = TaxonFile.objects()
        #     json_resp = []            
        #     for file in taxon_files:
        #         json_file = json.loads(file.to_json())
        #         organism = file.organism.fetch()
        #         json_file['organism'] = organism.name
        #         json_resp.append(json_file)
        #     return Response(json.dumps(json_resp), mimetype="application/json", status=200)
        # except ValidationError:
        #     raise SchemaValidationError
        # except Exception as e:
        #     app.logger.error(e)
        # raise InternalServerError
    #delete files of a taxon
    # def delete(self,tax_id):
    #     # taxon = TaxonNode.objects(tax_id=tax_id).first()
    #     taxon_files= TaxonFile.objects().delete()
    #     return '', 200

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
            taxon_file = TaxaFile.objects(name=name).first()
            file = taxon_file.file
            mimetype = taxon_file.mimetype
            # content_type = taxon_file.file.content_type
            return send_file(file, mimetype=mimetype)
            # return Response(file, content_type=content_type, status=200)
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError
    
    def delete(self,name):
        req = request.args
        if 'API_KEY' in req.keys() and req['API_KEY'] == API_KEY:
            file = TaxonFile.objects(name=name).first()
            if not file:
                raise NotFound
            taxon = TaxonNode(taxid=file.taxid).first()
            app.logger.info()   
            file.file.delete()
            file.delete()
            return name + 'correctly deleted', 200
        else:
            raise Unauthorized

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