from flask import Blueprint, request, jsonify
from .service import *

diemdanh_blueprint = Blueprint("DiemDanh", __name__)

@diemdanh_blueprint.route("/all-diemdanh", methods=["GET"], endpoint="route_all_diemdanh")
def route_get_all_diemdanh():
    if request.method == "GET":
        diemdanhs = get_all_diemdanh()

        if diemdanhs is not None:
            return jsonify(diemdanhs), 200
        else:
            return "None", 500
        
@diemdanh_blueprint.route("/diemdanh-user-id/<int:user_id>", methods=["GET", "POST"], endpoint="route_get_diemdanh_id")
def route_get_diemdanh_id(user_id):
    if request.method == "GET":
        diemdanhs = get_diemdanh_user_id(user_id)
        return jsonify(diemdanhs), 200
    
    if request.method == "POST":
        img = request.form.get("img", False)
        date = request.form.get("date", False)
        # user_id = request.form.get("user_id", False)

        if(img and date and user_id):
            diemdanh = {
                "img": img,
                "date": date,
                "user_id": user_id
            }

            diemdanhs = insert_diemdanh(diemdanh)

            return jsonify(diemdanhs), 200
        else:
            return "POST wrong!", 400