from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory sample data
users = [
    {"id": 1, "name": "Shreya", "email": "shreya@example.com"}
]

def validate_user(data):
    if not isinstance(data, dict):
        return "Request body must be JSON."
    if not data.get("name") or not isinstance(data.get("name"), str):
        return "Name is required."
    if not data.get("email") or not isinstance(data.get("email"), str):
        return "Email is required."
    if "@" not in data["email"]:
        return "Enter a valid email address."
    return None

@app.get("/")
def home():
    return jsonify({
        "message": "DecodeLabs Project 2 - Backend API is running",
        "endpoints": ["/api/users", "GET /api/users/<id>", "POST /api/users"]
    })

@app.get("/api/users")
def get_users():
    return jsonify(users), 200

@app.get("/api/users/<int:user_id>")
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.post("/api/users")
def create_user():
    data = request.get_json(silent=True)
    error = validate_user(data)

    if error:
        return jsonify({"error": error}), 400

    new_user = {
        "id": max([u["id"] for u in users], default=0) + 1,
        "name": data["name"].strip(),
        "email": data["email"].strip()
    }

    users.append(new_user)
    return jsonify({
        "message": "User created successfully",
        "user": new_user
    }), 201

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
