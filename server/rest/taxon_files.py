from os import name
from flask import Response, request
from flask import current_app as app
from db.models import TaxonFile, TaxonNode
from flask_restful import Resource
import services.taxon_service as service
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from errors import InternalServerError, SchemaValidationError, UserNotFoundError, EmailAlreadyExistError
import json
from BCBio.GFF import GFFExaminer
from BCBio import GFF


class TaxonFilesApi(Resource):
    def get(self,tax_id):
        try:
            taxon = TaxonNode.objects(tax_id=tax_id).first()
            taxon_files= TaxonFile.objects(taxon = taxon).to_json()
            return Response(taxon_files, mimetype="application/json", status=200)
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError
     
    def delete(self,tax_id):
        taxon_files = TaxonFile.objects.delete()
        return '', 200

    def post(self,tax_id):
        try:
            taxon = service.return_taxon(tax_id)
            file = request.files.get('file')
            data = json.loads(request.form['json'])
            taxon_files = TaxonFile(**data, file=file, taxon = taxon).save()
            return  201
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError


class TaxonFileApi(Resource):

     def post(self, name):
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

     def get(self,name):
         ##parse gff and send response to genome viewer
        try:
            tmp_file = "tmp.txt"
            taxon_file = TaxonFile.objects(name=name).first()
            to_json={}
            arr=[]
            with open(tmp_file,'wb') as tmp:
                tmp.write(taxon_file.file.read())
                for rec in GFF.parse(tmp_file):
                    for gene in rec.features:
                        track={}
                        track["id"] = gene.id
                        track["start"] = gene.location._start.position
                        track["end"] = gene.location._end.position
                        track["strand"] = gene.location._strand
                    arr.append(track)
                to_json['content'] = arr
            # # app.logger.info(taxon_file.file.readline(100))
            # for line in taxon_file.file.read():
            #     app.logger.info(line)
                # in_handle.write(line)
            # in_handle.close()
            # app.logger.info(in_handle[:100])
            # with open(tmp_file,'b') as f:
            #     f.write(file)
            #     for rec in GFF.parse(f):
            #         arr = [[i.location._start.position, i.location._end.position, i.location._strand, i.type,i.qualifiers] for i in rec.features]
            #     app.logger.info(arr[:10])
            # f.close()
            # file = taxon_file.file.read()
            # with open(tmp_file) as out_handle:
            #     for line in taxon_file.file.read():
            #         out_handle.write(line)
            # in_handle = open(tmp_file,'r')
            # to_json={}
            # to_json['content'] = arr
            # app.logger.info(to_json)
            # to_json['total'] = len(arr)
            # app.logger.info(in_handle)
            # for rec in GFF.parse(in_handle):
            #     arr=[]
            #     arr = [[i.location._start.position, i.location._end.position, i.location._strand, i.type,i.qualifiers] for i in rec.features]
            return Response(json.dumps(arr), mimetype="application/json", status=200)
        except NotUniqueError:
            raise EmailAlreadyExistError
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError  

    #TODO expose endopoint to upload files from workflow
	# def put(self, id):
	# 	body = request.get_json()
	# 	TaxonFiles.objects.get(id=id).update(**body)
	# 	return '', 200
    # def get(self, name):
    #     try:
    #         taxon_file = TaxonFile.objects(name=name).first()
    #         file = taxon_file.file.read()
    #         content_type = file.content_type
    #         return Response(taxon_file, content_type=content_type, status=200)
    #     except DoesNotExist:
    #         raise UserNotFoundError

	# def delete(self, id):
	# 	taxon_files = TaxonFiles.objects.get(id=id).delete()
	# 	return '', 200
# TODO create endpoints for retrieving files and send them to client
# class TaxonNodeFilesApi(Resource):

# 	def get(self,id):
# 		try:
# 			taxon_node = TaxonNode.objects