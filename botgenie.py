import telebot
import requests

# Telegram bot token
TOKEN = ''

# GenieACS API URL and credentials
GENIEACS_URL = 'http://id-24.hostddns.us:10609'
GENIEACS_USERNAME = ''
GENIEACS_PASSWORD = ''

# Initialize the Telegram bot
bot = telebot.TeleBot(TOKEN)

# Define a command handler for /status command
@bot.message_handler(commands=['status'])
def send_status(message):
    # Query GenieACS for device status
    device_id = message.chat.id  # Assuming device ID is the same as chat ID
    status = get_device_status(device_id)
    
    # Send status message to the user
    bot.reply_to(message, f"Device status: {status}")

# Function to query device status from GenieACS
def get_device_status(device_id):
    url = f"{GENIEACS_URL}/devices/{device_id}/status"
    response = requests.get(url, auth=(GENIEACS_USERNAME, GENIEACS_PASSWORD))
    if response.status_code == 200:
        device_status = response.json()
        return device_status['status']
    else:
        return "Failed to retrieve device status"

# Start the bot
bot.polling()
