from flask import Flask, jsonify, request
from flasgger import Swagger ,swag_from 


app = Flask(__name__)

swagger = Swagger(app, template = {
    "swagger": "2.0",
    "info": {
        "title": "Swagger Demo Docs",
        "description": "Auto-generated Swagger docs, baby",
        "version": "1.0.0"
    }
})

@app.route('/greet', methods=['GET'])
@swag_from('docs/greet.yaml')
def greet():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Name is required"}), 400
    try:
        return jsonify({"greeting": f"Hello, {name}!"}), 200
    except Exception:
        return jsonify({"error": "Something went terribly wrong"}), 500

if(__name__) == "__main__":
    app.run(host="0.0.0.0", debug=True,threaded=True, port=8000)


