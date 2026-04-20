import time

print("Welcome to AI Health Reminder Assistant")

medicine_time = input("Enter your medicine time (HH:MM format): ")
water_interval = int(input("Enter water reminder interval (in minutes): "))

print("Assistant is running...")

while True:
    current_time = time.strftime("%H:%M")

    if current_time == medicine_time:
        print("🔔 Time to take your medicine!")

    print("💧 Drink water reminder!")

    time.sleep(water_interval * 60)
