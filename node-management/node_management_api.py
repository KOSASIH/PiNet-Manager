# node_management_api.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///node_management.db"
db = SQLAlchemy(app)

class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip_address = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(20), nullable=False)

@app.route("/nodes", methods=["GET"])
def get_nodes():
    nodes = Node.query.all()
    return jsonify([{"id": node.id, "name": node.name, "ip_address": node.ip_address, "status": node.status} for node in nodes])

@app.route("/nodes", methods=["POST"])
def create_node():
    data = request.get_json()
    node = Node(name=data["name"], ip_address=data["ip_address"], status=data["status"])
    db.session.add(node)
    db.session.commit()
    return jsonify({"message": "Node created successfully"})

@app.route("/nodes/<int:node_id>", methods=["GET"])
def get_node(node_id):
    node = Node.query.get(node_id)
    if node is None:
        return jsonify({"message": "Node not found"}), 404
    return jsonify({"id": node.id, "name": node.name, "ip_address": node.ip_address, "status": node.status})

@app.route("/nodes/<int:node_id>", methods=["PUT"])
def update_node(node_id):
    node = Node.query.get(node_id)
    if node is None:
        return jsonify({"message": "Node not found"}), 404
    data = request.get_json()
    node.name = data["name"]
    node.ip_address = data["ip_address"]
    node.status = data["status"]
    db.session.commit()
    return jsonify({"message": "Node updated successfully"})

@app.route("/nodes/<int:node_id>", methods=["DELETE"])
def delete_node(node_id):
    node = Node.query.get(node_id)
    if node is None:
        return jsonify({"message": "Node not found"}), 404
    db.session.delete(node)
    db.session.commit()
    return jsonify({"message": "Node deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
