from flask import Response, request
from flask import current_app as app
from db.models import Newick
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from errors import InternalServerError, SchemaValidationError, UserNotFoundError, EmailAlreadyExistError


class NewickApi(Resource):
	def get(self):
		newick = Newick.objects().to_json()
		return Response(newick, mimetype="application/json", status=200)

	def delete(self):
		newick = Newick.objects.delete()
		return '', 200

	def post(self):
		try:
			body = request.get_json()
			newick = Newick(**body).save()
			id = newick.id
			return {'id': str(id)}, 201
		except NotUniqueError:
			raise EmailAlreadyExistError
		except ValidationError:
			raise SchemaValidationError
		except Exception as e:
			app.logger.error(e)
			raise InternalServerError

