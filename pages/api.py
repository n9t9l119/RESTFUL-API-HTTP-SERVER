from flask_classy import FlaskView, route
from flask import request, jsonify, Response

from api_methods.get_compare import info_comparison
from api_methods.get_geo_info import info
from api_methods.get_hint import hint
from api_methods.get_page import page


class ApiView(FlaskView):
    @route('/getinfo', methods=["POST"])
    def get_geo_info(self):
        geonameid = request.data.decode("utf-8")
        return info(geonameid)

    @route('/getpage', methods=["POST"])
    def get_page(self):
        json_request = request.get_json()
        if "Page" in json_request and "Items_value" in json_request:
            return page(json_request["Page"], json_request["Items_value"])
        return Response("Incorrect request!\nIt must be json with keys 'Page' and 'Items_value'!",
                        status=500, mimetype='text/plain')

    @route('/getcomparison', methods=["POST"])
    def get_comparison(self):
        json_request = request.get_json()
        if "Geo_1" in json_request and "Geo_2" in json_request:
            return info_comparison(json_request["Geo_1"], json_request["Geo_2"])
        return Response("Incorrect request!\nIt must be json with keys 'Geo_1' and 'Geo_2'!",
                        status=500, mimetype='text/plain')

    @route('/hintname', methods=["POST"])
    def hint_name(self):
        json_request = request.data.decode("utf-8")
        return hint(json_request)
