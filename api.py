from flask_classy import FlaskView, route
from flask import request, jsonify

from api_methods.get_compare import info_comparison
from api_methods.get_geo_info import info
from api_methods.get_hint import hint
from api_methods.get_page import page


class ApiView(FlaskView):
    @route('/getid', methods=["POST"])
    def get_id(self):
        geonameid = request.data.decode("utf-8")
        return info(geonameid)

    @route('/getpage', methods=["POST"])
    def get_page(self):
        json_request = request.get_json()
        if "Page" and "Items_value" in json_request:
            return jsonify(page(json_request["Page"], json_request["Items_value"]))
        else:
            return "Incorrect request!"

    @route('/getlocation', methods=["POST"])
    def get_location(self):
        json_request = request.get_json()
        if "Geo_1" and "Geo_2" in json_request:
            return jsonify(info_comparison(json_request["Geo_1"], json_request["Geo_2"]))
        else:
            return "Incorrect request!"

    @route('/hintname', methods=["POST"])
    def hint_name(self):
        json_request = request.data.decode("utf-8")
        return jsonify(hint(json_request))

