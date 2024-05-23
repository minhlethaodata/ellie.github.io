# from flask import Flask, jsonify, request, send_from_directory

# app = Flask(__name__, static_folder='static')

# # Dummy data endpoint
# @app.route('/data', methods=['GET'])
# def get_data():
#     return jsonify({"message": "Hello, world!"})

# # Route for serving the index.html file
# @app.route('/')
# def index():
#     return send_from_directory(app.static_folder, 'index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('templates/index.html').read())


if __name__ == '__main__':
    app.run(debug=True)
