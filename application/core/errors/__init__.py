from flask import json, jsonify
from werkzeug.exceptions import HTTPException, default_exceptions


class HTTPError:
    def __init__(self, msg, status_code):
        self.msg = msg
        self.status_code = status_code

    def to_response(self):
        return (
            jsonify({"msg": self.msg, "status_code": self.status_code}),
            self.status_code,
        )


class ErrorManager:
    """
    Creates a JSON-oriented Flask app.

    All error responses that you don't specifically
    manage yourself will have application/json content
    type, and will contain JSON like this (just an example):

    { "message": "405: Method Not Allowed", "status": 405, "code": 0 }

    Also provides app specific errors, which have a unique code and
    could have detailed information:

    {
      "message": "Your credentials do not allow access to this resource",
      "status": 403,
      "code": 1
    }
    """

    def make_json_error(self, status, message=None, code=None, details=None):
        response = jsonify(
            message=message, status=status, code=code, details=details
        )
        response.status_code = status
        return response

    def make_default_json_error(self, ex):
        status = ex.code if isinstance(ex, HTTPException) else 500
        return self.make_json_error(status, message=str(ex), code=0)

    def init_app(self, app):
        @app.errorhandler(HTTPException)
        def handle_exception(e):
            """Return JSON instead of HTML for HTTP errors."""
            # start with the correct headers and status code from the error
            response = e.get_response()
            # replace the body with JSON
            response.data = json.dumps(
                {
                    "code": e.code,
                    "name": e.name,
                    "description": e.description,
                }
            )
            response.content_type = "application/json"
            return response


error_manager = ErrorManager()
