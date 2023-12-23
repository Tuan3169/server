from flask import Blueprint, request
from .service import *
from flask import jsonify

account = Blueprint("Account", __name__)

@account.route("/a",endpoint="a")
def a():
    return "abc"

@account.route("/loggin", methods=["GET", "PUT"])
def route():
    if request.method == "GET":
        all_account = get_all_account()
        
        if all_account is not None:
            return jsonify(all_account),200
        else:
            return "None",500
        

        
    if request.method == "PUT":
        account_name = request.form.get("username", False)
        password = request.form.get("password", False)
        
        if(account_name == False or password == False):
            return "POST Wrong!", 400
        
        account = check_account(account_name, password)
        if account is not None:
            if account.__len__() != 0:
                if account[0]["password"] == password:
                    return "lgoin success!", 200
                else:
                    return "Password wrong!", 400
                
            else:
                return "account is null!", 400
        else:
            return "None", 500
        