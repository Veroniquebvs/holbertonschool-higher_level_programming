#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_users():
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def get_status():
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_username(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def create_user():
    new_user = request.get_json()
    if new_user is None:
        return jsonify({"error": "Invalid JSON"}), 400
    if "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400
    if new_user["username"] in users:
        return jsonify({"error": "Username already exists"}), 409
    else:
        username = new_user["username"]
        users[username] = new_user
        return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
