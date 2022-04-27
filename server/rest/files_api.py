from flask import Response, request
from flask import current_app as app
from flask_restful import Resource
# import services.taxon_service as service
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from errors import InternalServerError, NotFound, SchemaValidationError, Unauthorized, EmailAlreadyExistError
import os
from services import organism_service
from services import file_service

API_KEY = os.getenv('SECRET_KEY')

GENOMES='genomes'
ANNOTATIONS='annotations'
PARAMETERS='parameters'

class GenomesApi(Resource):
    def get(self):
        return Response(file_service.search_by_taxid(request,GENOMES))
        
    def post(self):
        return Response(file_service.payload_parser(request, GENOMES))

    # def put(self, name):
    #     model_obj = file_service.model_handler(GENOMES)
    #     obj = model_obj.objects(name=name).first()
    #     ## add validating step
    #     obj.modify(**request.form)

    # def delete(self, name):
    #     model_obj = file_service.model_handler(GENOMES)
    #     obj = model_obj.objects(name=name).first()
    #     obj.delete()

class AnnotationApi(Resource):
    def get(self):
        return Response(file_service.search_by_taxid(request,ANNOTATIONS))

    def post(self):
        return Response(file_service.payload_parser(request, ANNOTATIONS))

    # def put(self, name):
    #     model_obj = file_service.model_handler(ANNOTATIONS)
    #     obj = model_obj.objects(name=name).first()
    #     ## add validating step
    #     obj.modify(**request.form)

    # def delete(self, name):
    #     model_obj = file_service.model_handler(ANNOTATIONS)
    #     obj = model_obj.objects(name=name).first()
    #     obj.delete()

class ParamApi(Resource):
    def get(self):
        return Response(file_service.search_by_taxid(request,PARAMETERS))

    # def post(self):
    #     return Response(file_service.payload_parser(request, PARAMETERS))

    # def put(self, name):
    #     model_obj = file_service.model_handler(PARAMETERS)
    #     obj = model_obj.objects(name=name).first()
    #     ## add validating step
    #     obj.modify(**request.form)

    # def delete(self, name):
    #     model_obj = file_service.model_handler(PARAMETERS)
    #     obj = model_obj.objects(name=name).first()
    #     obj.delete()