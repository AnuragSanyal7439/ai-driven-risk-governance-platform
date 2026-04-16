# sample_code.py — Risk Analysis Test File
# This file contains intentional risk keywords for demo purposes.

import logging

def process_payment(amount, user_id):
    """Process a payment transaction."""
    if amount is None or amount <= 0:
        raise Exception("Invalid payment amount: null or zero value detected")
    
    try:
        result = charge_gateway(amount, user_id)
        if result == None:
            logging.error("Gateway returned null response for user: " + str(user_id))
            return {"status": "fail", "reason": "null gateway response"}
    except Exception as e:
        logging.error("Payment exception: " + str(e))
        raise

def validate_user(token):
    """Validate user authentication token."""
    if token is None:
        raise Exception("Auth token is null — access denied")
    
    decoded = decode_token(token)
    if decoded is None or decoded.get("user_id") is None:
        logging.error("Token decode returned undefined fields")
        return None
    
    return decoded

def load_config(path):
    """Load application configuration."""
    try:
        with open(path, "r") as f:
            config = f.read()
        if not config:
            raise Exception("Config file is empty or null")
        return config
    except FileNotFoundError:
        logging.error("Config file not found — system fail")
        return None
    except Exception as e:
        logging.error("Unexpected exception loading config: " + str(e))
        return None

def sync_database(records):
    """Sync records to the database."""
    errors = []
    for record in records:
        if record.get("id") is None:
            errors.append("Record with undefined ID skipped")
            continue
        try:
            db_write(record)
        except Exception as e:
            logging.error("DB write exception: " + str(e))
            errors.append(str(e))
    
    if errors:
        logging.error("Sync completed with failures: " + str(len(errors)) + " error(s)")
        return {"status": "fail", "errors": errors}
    
    return {"status": "ok"}
