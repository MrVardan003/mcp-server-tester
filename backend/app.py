from flask import Flask, request, jsonify
from flask_cors import CORS  # 👈 Add this
from mcp_tester import run_tests

app = Flask(__name__)
CORS(app)  # 👈 Enable CORS

@app.route("/api/test", methods=["POST"])
def test_mcp():
    data = request.json
    installation_code = data.get("installation_code")
    api_key = data.get("api_key")
    config = data.get("config")
    valid_json_input = data.get("valid_json_input")

    result = run_tests(installation_code, api_key, config, valid_json_input)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
