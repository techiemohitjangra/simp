from router import app
from flask import jsonify, request
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from models.contruction_project import ConstructionProject


@app.route("/project", methods=['GET'])
def getProject():
    project_id = request.args.get("id")
    project_name = request.args.get("name")

    utc_time = datetime.now(ZoneInfo("UTC"))
    india_timezone = ZoneInfo("Asia/Kolkata")
    india_time = utc_time.astimezone(india_timezone)

    project = ConstructionProject(id=1, name="test", start_date=india_time,
                                  end_date=india_time + timedelta(hours=1))

    if project_id:
        return jsonify(project.json())
    elif project_name:
        pass

    return jsonify({"error": "Provide either 'id' or 'name' as query"})


@app.route("/project/<data>", methods=['GET'])
def getProjectData(data: str):
    project_id = request.args.get("id")
    project_name = request.args.get("name")

    if not project_id and not project_name:
        return jsonify({"error": "Provide either 'id' or 'name' as query"})

    if data == "feedback":
        # fetch and return feedback for the project with given id or name
        pass
    elif data == "":
        pass
    else:
        pass
