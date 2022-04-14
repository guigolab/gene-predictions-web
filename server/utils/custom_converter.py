# from flask import Flask
# from enum import Enum, unique
# from werkzeug.routing import BaseConverter, ValidationError

# @unique
# class RequestType(str, Enum):
#     TYPE1 = 'abc'
#     TYPE2 = 'def'

# class RequestTypeConverter(BaseConverter):

#     def to_python(self, value):
#         try:
#             request_type = RequestType(value)
#             return request_type
#         except ValueError as err:
#             raise ValidationError()

#     def to_url(self, obj):
#         return obj.value


# app = Flask(__name__)
# app.url_map.converters.update(request_type=RequestTypeConverter)
