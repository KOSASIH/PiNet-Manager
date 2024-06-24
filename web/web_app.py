from flask import Flask, render_template, request, redirect, url_for
from web.templates import index, node_list, node_detail, user_list, user_detail

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nodes")
def node_list():
    nodes = Node.query.all()
    return render_template("node_list.html", nodes=nodes)

@app.route("/nodes/<int:node_id>")
def node_detail(node_id):
    node = Node.query.get(node_id)
    if node is None:
        return redirect(url_for("node_list"))
    return render_template("node_detail.html", node=node)

@app.route("/users")
def user_list():
    users = User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/users/<int:user_id>")
def user_detail(user_id):
    user = User.query.get(user_id)
    if user is None:
        return redirect(url_for("user_list"))
    return render_template("user_detail.html", user=user)

if __name__ == "__main__":
    app.run()
