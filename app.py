from flask import Flask, request, jsonify
from api.imei_parse import imei_data
import json


app = Flask(__name__)

@app.route('/api/imei_process', methods=['POST'])
def process_data_route():
    try:
        input_data = request.get_json()
        processed_data = imei_data(json.dumps(input_data))
        return jsonify(processed_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run("0.0.0.0",debug=False)
