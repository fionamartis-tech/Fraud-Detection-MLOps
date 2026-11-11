from datetime import datetime
import math

REQUIRED_FIELDS=["transaction_id",
                 "customer_id",
                 "amount",
                 "merchant",
                 "city",
                 "device",
                 "timestamp"]
def validate_transaction(transaction):
    errors=[]
    if not isinstance(transaction,dict):
        return False,["Transaction must be a dictionary"]
    # Check required field
    for field in REQUIRED_FIELDS:
        value=transaction.get(field)
        if value is None or value =="":
            errors.append(f"{field} is required")
        elif isinstance(value, str) and not value.strip():
            errors.append(f"{field} cannot be empty or whitespace")

            # Validate id and description fields
        for field in ["transaction_id", "customer_id","merchant","city","device"]:
            value=transaction.get(field)
            if value is not None and not isinstance(value, str):
                errors.append(f"{field} must be a string")

        # Validate amount field
        amount=transaction.get("amount")
        if(isinstance(amount,bool) or not isinstance(amount,(int, float))
           or not math.isfinite(amount) and amount<0):
            errors.append("amount must be in finite number")

        # Validate timestamp field
        timestamp=transaction.get("timestamp")
        if not isinstance(timestamp,str):
            errors.append("Timestamp must be aa ISO datetime text")
        else:
            try:
                parsed = datetime.fromisoformat(timestamp)
                if parsed.tzinfo is None:
                    errors.append("Timestamp must be ISO timestamp")
            except ValueError:
                errors.append("Timestamp has invalid format")
        return len(errors) == 0, errors
