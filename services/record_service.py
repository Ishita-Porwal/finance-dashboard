from utils.db import records_collection
from models.record_model import record_schema

def create_record(data):
    required = ["amount", "type", "category", "date"]

    if not all(field in data for field in required):
        return {"error": "Missing fields"}, 400

    records_collection.insert_one(data)
    return {"message": "Record created"}, 201


def get_records(filters):
    query = {}

    if "type" in filters:
        query["type"] = filters["type"]

    if "category" in filters:
        query["category"] = filters["category"]

    records = records_collection.find(query)
    return [record_schema(r) for r in records]


def delete_record(record_id):
    from bson import ObjectId

    records_collection.delete_one({"_id": ObjectId(record_id)})
    return {"message": "Deleted"}


def get_summary():
    records = list(records_collection.find())

    income = sum(r["amount"] for r in records if r["type"] == "income")
    expense = sum(r["amount"] for r in records if r["type"] == "expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }