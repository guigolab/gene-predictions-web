from flask import Response, request
from flask import current_app as app
from flask_restful import Resource
from utils import common_functions
from services import file_service


GENOMES='genomes'
ANNOTATIONS='annotations'
PARAMETERS='parameters'

class GenomesApi(Resource):
    def get(self):
        return Response(file_service.search_by_taxid(request,GENOMES))
        
    def post(self):
        return Response(file_service.payload_parser(request, GENOMES))

    def put(self, name):
        args = request.args
        if 'API_KEY' in args.keys() and common_functions.auth_request(args['API_KEY']):
            model_obj = file_service.model_handler(GENOMES)
            obj = model_obj.objects(name=name).first()
            ## add validating step
            obj.modify(**request.form)
            return Response(obj.to_json())
        return 405

    def delete(self, name):
        args = request.args
        if 'API_KEY' in args.keys() and common_functions.auth_request(args['API_KEY']):
            model_obj = file_service.model_handler(GENOMES)
            obj = model_obj.objects(name=name).first()
            obj.delete()
            return 201
        return 405

class AnnotationApi(Resource):
    def get(self):
        return Response(file_service.search_by_taxid(request,ANNOTATIONS))

    def post(self):
        return Response(file_service.payload_parser(request, ANNOTATIONS))

    def put(self, name):
        args = request.args
        if 'API_KEY' in args.keys() and common_functions.auth_request(args['API_KEY']):
            model_obj = file_service.model_handler(ANNOTATIONS)
            obj = model_obj.objects(name=name).first()
            ## add validating step
            obj.modify(**request.form)
            return Response(obj.to_json())
        return 405

    def delete(self, name):
        args = request.args
        if 'API_KEY' in args.keys() and common_functions.auth_request(args['API_KEY']):
            model_obj = file_service.model_handler(ANNOTATIONS)
            obj = model_obj.objects(name=name).first()
            obj.delete()
            return 201
        return 405

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