# coding=utf-8
from base_error import BaseError
from backend_common.services.medical import MedicalAPIError


def uncaught_error_handler(e):
    import sys
    import backend_common.constants.http_code as http_code
    from flask import jsonify, current_app
    current_app.log_exception(sys.exc_info())
    return jsonify({'errcode': http_code.INTERNAL_SERVER_ERROR, 'errmsg': e.__class__.__name__})


def init_app(server):
    exceptions = [BaseError, MedicalAPIError]
    for e in exceptions:
        server.register_error_handler(e, e.handle)
    server.register_error_handler(Exception, uncaught_error_handler)
