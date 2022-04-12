from flask import Flask, request, abort
import json
from database import *

app = Flask(__name__)


@app.route("/")
def home():
    return "Search '/users/' to list all users etc..."


@app.route("/users/", methods=["GET"])
def users():
    id = request.args.get("id")
    userId = request.args.get("userId")
    if id:
        user = user_by_id(id)
        return user
    elif userId:
        user = user_by_userid(userId)
        return user
    else:
        users = all_users()
        return users


@app.route("/create/", methods=["POST"])
def add_user():
    id = request.args.get("id")
    userId = request.args.get("userId")
    firstName = request.args.get("firstName")
    lastName = request.args.get("lastName")
    if id:
        new_user = get_new_user(id, userId, firstName, lastName)
        return container.create_item(body=new_user)


@app.errorhandler(400)
def handle_400_error(e):
    return json.dumps({"error": f"{e}"}, indent=True)


@app.errorhandler(401)
def handle_401_error(e):
    return json.dumps({"error": f"{e}"}, indent=True)


@app.errorhandler(404)
def handle_404_error(e):
    return json.dumps({"error": f"{e}"}, indent=True)


@app.errorhandler(500)
def handle_500_error(e):
    return json.dumps({"error": f"{e}"}, indent=True)


if __name__ == "__main__":
    app.run(debug=True)
