import pywhatkit as kit
import schedule
import random
import time

# List of sweet messages
messages = [
    "Good morning, my love! ❤️ Hope you have a beautiful day!",
    "Just thinking about you 😘 Hope your day is as amazing as you are!",
    "You're my sunshine ☀️ Have a fantastic day, baby!",
    "I love you so much! 💖 Stay happy and take care!",
    "You make my world brighter 🌍✨ Can't wait to talk to you later!"
]

# Your boyfriend's WhatsApp number (replace with actual number)
recipient_number = "+254797341497"

# Function to send a message
def send_message():
    message = random.choice(messages)
    try:
        kit.sendwhatmsg_instantly(recipient_number, message, wait_time=0, tab_close=True)
        print(f"Sent: '{message}'")
    except Exception as e:
        print(f"Error sending message: {e}")

# Schedule 3 messages per hour
for _ in range(3):
    minute = random.randint(10, 50)
    schedule.every().hour.at(f":{minute:02d}").do(send_message)

# Run the scheduler
print("Automated WhatsApp message sender is running...")
while True:
    schedule.run_pending()
    time.sleep(00)  # Check every minute
