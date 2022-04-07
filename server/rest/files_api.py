from flask import Response, request, send_file
from flask import current_app as app
from db.models import  FastaFile, GFF3File, ParamFile
from flask_restful import Resource
from errors import  NotFound, SchemaValidationError,Unauthorized,InternalServerError,RecordAlreadyExistError
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
import os
from services import organism_service

API_KEY = os.getenv('SECRET_KEY')
REQUIRED_PARAMS=['taxid','API_KEY','type']

class FastaApi(Resource):
    def post(self):
        req = request.json if request.is_json else request.form
        if req['API_KEY'] != API_KEY:
            raise Unauthorized
        taxid = req['taxid']
        organism = organism_service.get_or_create_organism(taxid)
        if not organism:
            raise NotFound
        #TODO check if fasta name already exists
        file = request.files['file']
        name = file.filename
        app.logger.info(FastaFile.objects().as_pymongo())
        fasta = FastaFile(taxid=taxid,name=name,file=file).save()
        organism.fastas.append(fasta)
        organism.save()
        return 201

    def get(self, name=None):
        try:
            if name:
                fasta = FastaFile.objects(name=name).first()
                # content_type = taxon_file.file.content_type
                return send_file(fasta.file, mimetype=fasta.mimetype)
            else:
                if 'taxid' in request.args.keys():
                    return Response(FastaFile.objects(taxid=request.args['taxid']).to_json())
            # return Response(file, content_type=content_type, status=200)
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError

class GFFApi(Resource):
    def post(self):
        req = request.json if request.is_json else request.form
        if req['API_KEY'] != API_KEY:
            raise Unauthorized
        taxid = req['taxid']
        organism = organism_service.get_or_create_organism(taxid)
        if not organism:
            raise NotFound
        #TODO check if fasta name already exists
        file = request.files['file']
        name = file.filename
        app.logger.info(GFF3File.objects().as_pymongo())
        fasta = GFF3File(taxid=taxid,name=name,file=file).save()
        organism.param_files.append(fasta)
        organism.save()
        return 201

    def get(self, name=None):
        try:
            if name:
                fasta = GFF3File.objects(name=name).first()
                # content_type = taxon_file.file.content_type
                return send_file(fasta.file, mimetype=fasta.mimetype)
            else:
                if 'taxid' in request.args.keys():
                    return Response(GFF3File.objects(taxid=request.args['taxid']).to_json())
            # return Response(file, content_type=content_type, status=200)
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError
# class Gff3Api(Resource):

class ParamApi(Resource):
    def post(self):
        req = request.json if request.is_json else request.form
        if req['API_KEY'] != API_KEY:
            raise Unauthorized
        taxid = req['taxid']
        organism = organism_service.get_or_create_organism(taxid)
        if not organism:
            raise NotFound
        #TODO check if fasta name already exists
        file = request.files['file']
        name = file.filename
        app.logger.info(ParamFile.objects().as_pymongo())
        fasta = ParamFile(taxid=taxid,name=name,file=file).save()
        organism.param_files.append(fasta)
        organism.save()
        return 201

    def get(self, name=None):
        try:
            if name:
                fasta = ParamFile.objects(name=name).first()
                # content_type = taxon_file.file.content_type
                return send_file(fasta.file, mimetype=fasta.mimetype)
            else:
                if 'taxid' in request.args.keys():
                    return Response(ParamFile.objects(taxid=request.args['taxid']).to_json())
            # return Response(file, content_type=content_type, status=200)
        except ValidationError:
            raise SchemaValidationError
        except Exception as e:
            app.logger.error(e)
        raise InternalServerError



# class TaxaFileApi(Resource):

# class InputDataApi(Resource):
## separate file input logics
## add file replace here (PUT)
    # def post(self):
    #     req = request.json if request.is_json else request.form
    #     app.logger.info(req['type'])
    #     if not request.files or not 'file' in request.files.keys() \
    #          or not all(key in REQUIRED_PARAMS for key in req.keys()) \
    #              or not req['type'] in [enum.value for enum in FileType]:
    #         raise SchemaValidationError
    #     if req['API_KEY'] != API_KEY:
    #         raise Unauthorized
    #     type = req['type']
    #     taxid = req['taxid']
    #     filename= request.files['file'].filename
    #     if TaxonFile.objects(name=filename).first():
    #         raise RecordAlreadyExistError
    #     organism = organism_service.get_or_create_organism(taxid)
    #     if not organism:
    #         raise NotFound
    #     saved_file = TaxonFile(taxid=taxid, file = request.files['file'], name=filename, type=FileType[type.upper()]).save()
    #     if saved_file.type == FileType.PARAM:
    #         organism.param_files.append(saved_file)
    #     elif saved_file.type == FileType.FASTA:
    #         organism.fastas.append(saved_file)
    #     elif saved_file.type == FileType.GFF:
    #         organism.gffs.append(saved_file)
    #     else:
    #         raise SchemaValidationError
    #     organism.save()
    #     return 201

    # def delete(self):
    #     req = request.args
    #     if 'API_KEY' in req.keys() and req['API_KEY'] == API_KEY:
    #         TaxonNode.drop_collection()
    #         Organism.drop_collection()
    #         for tax_file in TaxonFile.objects(file__ne=None):
    #             tax_file.file.delete()
    #         TaxonFile.drop_collection()
    #         # for result in GeneIdResults.objects(ps__ne=None):
    #         #     result.ps.delete()
    #         # for result in GeneIdResults.objects(jpg__ne=None):
    #         #     result.jpg.delete()  
    #         GeneIdResults.drop_collection()
    #         GeneIdStats.drop_collection()
    #         for entry in os.scandir('/tmp'):
    #             os.remove(entry)
    #     else:
    #         raise Unauthorized
    #     return 200