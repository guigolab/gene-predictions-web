from flask import Response, request
from flask import current_app as app
from db.models import Species
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from errors import InternalServerError, SchemaValidationError, UserNotFoundError, EmailAlreadyExistError


class SpeciesApi(Resource):
	def get(self):
		species = Species.objects().to_json()
		return Response(species, mimetype="application/json", status=200)

	def delete(self):
		species = Species.objects.delete()
		return '', 200

	def post(self):
		try:
			app.logger.error(request.get_json())
			body = request.get_json()
			species = Species(**body).save()
			id = species.id
			return {'id': str(id)}, 201
		except NotUniqueError:
			raise EmailAlreadyExistError
		except ValidationError:
			raise SchemaValidationError
		except Exception as e:
			app.logger.error(e)
			raise InternalServerError

# class SpeciesApi(Resource):
# 	def put(self, id):
# 		body = request.get_json()
# 		Species.objects.get(id=id).update(**body)
# 		return '', 200

# 	def get(self, id):
# 		try:
# 			species = Species.objects.get(id=id).to_json()
# 			return Response(species, mimetype="application/json", status=200)
# 		except DoesNotExist:
# 			raise UserNotFoundError

# 	def delete(self, id):
# 		species = Species.objects.get(id=id).delete()
# 		return '', 200