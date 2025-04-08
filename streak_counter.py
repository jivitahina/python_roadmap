import json
import os
from datetime import datetime, timedelta

STREAK_FILE = "streak_log.json"

def load_data():
    if not os.path.exists(STREAK_FILE):
        return {"streak": 0, "last_date": None}
    with open(STREAK_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(STREAK_FILE, "w") as f:
        json.dump(data, f)

def update_streak():
    data = load_data()
    today = datetime.now().date()
    last_date = (
        datetime.strptime(data["last_date"], "%Y-%m-%d").date()
        if data["last_date"]
        else None
    )

    if last_date == today:
        print("✅ You've already logged today. Keep it up!")
    elif last_date == today - timedelta(days=1):
        data["streak"] += 1
        data["last_date"] = today.isoformat()
        print(f"🔥 {data['streak']}-day streak! You're on fire!")
    else:
        data["streak"] = 1
        data["last_date"] = today.isoformat()
        print("🌱 Streak reset. Today is Day 1 of your new journey!")

    save_data(data)

if __name__ == "__main__":
    update_streak()