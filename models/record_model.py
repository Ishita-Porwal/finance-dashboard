def record_schema(record):
    return {
        "id": str(record["_id"]),
        "amount": record["amount"],
        "type": record["type"],
        "category": record["category"],
        "date": record["date"],
        "note": record.get("note", "")
    }