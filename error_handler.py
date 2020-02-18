from config import app
from flask import Response


@app.errorhandler(404)
def not_found_error(error):
    return Response("Error 404\nNot Found", status=404, mimetype='text/plain')


@app.errorhandler(400)
def not_found_error(error):
    return Response("Error 400!\nBad Request", status=400, mimetype='text/plain')


@app.errorhandler(500)
def internal_error(error):
    return Response("Error 500\nInternal Server Error", status=500, mimetype='text/plain')
