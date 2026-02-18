from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

DB = "users.json"

# ===== DATABASE =====
def load():
    if not os.path.exists(DB):
        return {}
    with open(DB,"r",encoding="utf8") as f:
        return json.load(f)

def save(data):
    with open(DB,"w",encoding="utf8") as f:
        json.dump(data,f,indent=2)

# ===== REGISTER =====
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    users = load()

    u = data["user"]
    p = data["pass"]

    if u in users:
        return jsonify({"error":"User tồn tại"}),400

    users[u] = {
        "pass": p,
        "money": 0
    }

    save(users)
    return jsonify({"ok":True})

# ===== LOGIN =====
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    users = load()

    u = data["user"]
    p = data["pass"]

    if u not in users or users[u]["pass"] != p:
        return jsonify({"error":"Sai tài khoản"}),401

    return jsonify({
        "user":u,
        "money":users[u]["money"]
    })

# ===== TASK =====
@app.route("/task", methods=["POST"])
def task():
    u = request.json["user"]
    users = load()

    users[u]["money"] += 200
    save(users)

    return jsonify({"money":users[u]["money"]})

# ===== ADMIN GET USERS =====
@app.route("/admin/users")
def admin_users():
    return jsonify(load())

# ===== ADMIN UPDATE MONEY =====
@app.route("/admin/update", methods=["POST"])
def update_money():
    data = request.json
    users = load()

    u = data["user"]
    money = int(data["money"])

    users[u]["money"] = money
    save(users)

    return jsonify({"ok":True})

app.run(host="0.0.0.0", port=5000)
