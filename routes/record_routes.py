from flask import Blueprint, request
from services.record_service import create_record, get_records, delete_record, get_summary
from middleware.auth_middleware import role_required

record_bp = Blueprint("records", __name__)

@record_bp.route("/records", methods=["POST"])
@role_required(["Admin"])
def add_record():
    return create_record(request.json)


@record_bp.route("/records", methods=["GET"])
@role_required(["Admin", "Analyst", "Viewer"])
def fetch_records():
    return get_records(request.args)


@record_bp.route("/records/<id>", methods=["DELETE"])
@role_required(["Admin"])
def remove_record(id):
    return delete_record(id)


@record_bp.route("/summary", methods=["GET"])
@role_required(["Admin", "Analyst"])
def summary():
    return get_summary()