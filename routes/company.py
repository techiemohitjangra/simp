from router import app
from flask import request, jsonify


@app.route("/company", methods=['GET'])
def getCompany():
    company_id = request.args.get("id")
    company_name = request.args.get("name")

    if company_id:
        pass
    elif company_name:
        pass

    return jsonify({"error": "Provide either 'id' or 'name' as query"})
