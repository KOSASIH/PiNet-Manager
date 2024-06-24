from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from api.models import Node, User
from api.schemas import NodeSchema, UserSchema

app = Flask(__name__)
app.config.from_file("config.json", silent=True)

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route("/nodes", methods=["GET"])
def get_nodes():
    nodes = Node.query.all()
    return jsonify(NodeSchema(many=True).dump(nodes))

@app.route("/nodes/<int:node_id>", methods=["GET"])
def get_node(node_id):
    node = Node.query.get(node_id)
    if node is None:
        return jsonify({"error": "Node not found"}), 404
    return jsonify(NodeSchema().dump(node))

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify(UserSchema(many=True).dump(users))

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(UserSchema().dump(user))

if __name__ == "__main__":
    app.run()
