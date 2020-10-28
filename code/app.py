import trend_app_protect.start
import os
import logging
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'SECRET'
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
ENABLE_DEBUGGING = os.environ.get('ENABLE_DEBUGGING')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    if uploaded_file.filename != "":
        output_file_path = f"/tmp/{uploaded_file.filename}"
        uploaded_file.save(output_file_path)

        # display output via web browser & container logs
        if ENABLE_DEBUGGING:
            http_method = f'Method:\n{request.method}'
            flash(http_method)
            app.logger.info(http_method)

            flash('Headers:')
            app.logger.info('Headers:')

            for header in request.headers:
                flash(header)
                app.logger.info(header)

    return render_template("index.html")
