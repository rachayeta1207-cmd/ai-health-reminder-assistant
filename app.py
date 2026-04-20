import time
from datetime import datetime

# ---------------- USER PROFILE ----------------
def get_user_profile():
    print("🧑 Welcome to AI Health Reminder Assistant\n")
    name = input("Enter your name: ")
    medicine_time = input("Enter medicine time (HH:MM): ")
    water_interval = int(input("Water reminder interval (minutes): "))
    exercise_time = input("Enter exercise time (HH:MM): ")

    return {
        "name": name,
        "medicine_time": medicine_time,
        "water_interval": water_interval,
        "exercise_time": exercise_time
    }

# ---------------- LOGGING SYSTEM ----------------
def log_event(message):
    with open("health_log.txt", "a") as file:
        file.write(f"{datetime.now()} - {message}\n")

# ---------------- SMART REMINDERS ----------------
def medicine_reminder(profile):
    print(f"\n🔔 {profile['name']}, it's time to take your medicine!")
    response = input("Did you take it? (yes/no): ")

    if response.lower() == "no":
        print("⚠️ Reminder: Please take your medicine now!")
        log_event("Medicine missed")
        return False
    else:
        print("✅ Great! Stay healthy.")
        log_event("Medicine taken")
        return True

def exercise_reminder(profile):
    print(f"\n🏃 {profile['name']}, time to exercise!")
    log_event("Exercise reminder sent")

def water_reminder():
    print("💧 Drink water!")
    log_event("Water reminder sent")

# ---------------- MAIN ENGINE ----------------
def run_assistant(profile):
    missed_medicine = False
    last_water_time = time.time()

    print("\n🚀 Assistant is running...\n")

    while True:
        current_time = datetime.now().strftime("%H:%M")

        # Medicine logic
        if current_time == profile["medicine_time"]:
            missed_medicine = not medicine_reminder(profile)

        # Smart repeated alert if missed
        if missed_medicine:
            print("⚠️ You still haven't taken your medicine!")

        # Exercise reminder
        if current_time == profile["exercise_time"]:
            exercise_reminder(profile)

        # Water reminder based on interval
        if time.time() - last_water_time >= profile["water_interval"] * 60:
            water_reminder()
            last_water_time = time.time()

        time.sleep(30)

# ---------------- RUN ----------------
if __name__ == "__main__":
    user_profile = get_user_profile()
    run_assistant(user_profile)
