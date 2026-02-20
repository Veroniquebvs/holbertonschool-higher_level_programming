from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token, jwt_required,
                                get_jwt_identity, get_jwt)
from datetime import timedelta


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "mon_mot_de_passe"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)
auth = HTTPBasicAuth()
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# AUTHENTIFICATION
@auth.verify_password
def verify_password(username, password):
    if username in users:
        stored_hash = users[username]["password"]
        if check_password_hash(stored_hash, password):
            return username
    return None


@auth.error_handler
def auth_error(status):
    return jsonify({"error": "Unauthorized"}), 401


# Protected Route
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


# JWT Authentication
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Unauthorized"}), 401
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )
    return jsonify({"access_token": access_token}), 200


# JWT Protected Route
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted"}), 200


# Role-based Protected Route
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    get_jwt_identity()
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


# Error Handlers
@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(err):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run(debug=True)
