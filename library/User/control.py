from flask import Blueprint, request, jsonify
from .service import *


user_blueprint = Blueprint("User", __name__)

@user_blueprint.route("/all-user", methods= ["GET"], endpoint = 'route_all_user')
def route_all_user():
    if request.method == "GET":
        users = get_all_user()
        return jsonify(users),200

@user_blueprint.route("/user-account-id/<int:account_id>", methods=["PUT"], endpoint = 'route_account_id')
def route_get_account_id(account_id):
    if request.method == "PUT":
         
        user = get_user_account_id(account_id)
        if user.__len__() != 0:
            return jsonify(user), 200
        else:
         return "user is null!", 400

@user_blueprint.route("/user_id/<int:id>", methods=["PUT"], endpoint = 'route_user_id')
def route_user_id(id):
    if request.method == "PUT":

        user = get_user_id(id)

        if user.__len__() != 0:
            return jsonify(user), 200
        else:
            return "user is null!", 200        


@user_blueprint.route("/user_update_avatar", methods=["PUT"], endpoint = 'route_update_avatar')
def route_update_avatar():
    if request.method == "PUT":
        avatar = request.form.get("user_avatar", False)
        user_id = request.form.get("id", False)
        if (avatar != False and user_id != False):
            user = update_avatar(user_id, avatar)
            if len(user) == 0:
                return "user is null!", 200
            else:
                return jsonify(user), 200
        elif avatar == False:
            return "avatar is null!", 400
        elif id == False:
            return "id is null!", 400
