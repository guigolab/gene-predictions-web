from flask import Response, request
from flask import current_app as app
from flask_restful import Resource
# import services.taxon_service as service
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from errors import InternalServerError, NotFound, SchemaValidationError, Unauthorized, EmailAlreadyExistError
import os
from services import organism_service
from services import file_service
import json

API_KEY = os.getenv('SECRET_KEY')

GENERAL_PARAMS = ['name, locations','taxid']

FILES_ENUM = ['genomes', 'annotations', 'parameters']

## class to dynamically CRUD file model
class FilesModelApi(Resource):
#TODO add decorator to handle model not in FILES_ENUM
    def get(self, model):
        if not model in FILES_ENUM:
            raise NotFound
        model = file_service.model_handler(model)
        model_objects = model.objects().to_json()
        return Response(model_objects)
     
    def post(self, model):
        params = request.json
        #expected params: {taxi}
        app.logger.info(params)
        error_keys = file_service.validate_params(params, GENERAL_PARAMS)
        if not error_keys:
            error_keys = file_service.validate_params(params['locations'], file_service.location_handler(model))
        if error_keys:
            return error_keys, model
        organism = organism_service.get_or_create_organism(params['taxid'])
        model_obj = file_service.model_handler(model)
        saved_file_obj = file_service.create_file_model(params, organism, model_obj)
        organism = file_service.organism_handler(model, saved_file_obj, organism)
        if organism:
            return 201, model

    def put(self, model, name):
        model_obj = file_service.model_handler(model)
        obj = model_obj.objects(name=name).first()
        ## add validating step
        obj.modify(**request.form)

    def delete(self, model, name):
        model_obj = file_service.model_handler(model)
        obj = model_obj.objects(name=name).first()
        obj.delete()


       