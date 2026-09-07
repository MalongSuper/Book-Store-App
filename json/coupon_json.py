import json
import os
from datetime import datetime

COUPON_JSON_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates", "coupon.json")

def load_coupons():
    with open(COUPON_JSON_PATH, "r") as f:
        return json.load(f)

def save_coupons(coupons):
    with open(COUPON_JSON_PATH, "w") as f:
        json.dump(coupons, f, indent=2)

def get_user_coupon(email, code):
    for coupon in load_coupons():
        if coupon["user_email"] == email and coupon["code"] == code:
            return coupon
    return None
