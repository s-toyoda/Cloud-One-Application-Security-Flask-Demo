import trend_app_protect.start
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    if uploaded_file.filename != "":
        output_file_path = f"/tmp/{uploaded_file.filename}"
        uploaded_file.save(output_file_path)

    return redirect(url_for("index"))

