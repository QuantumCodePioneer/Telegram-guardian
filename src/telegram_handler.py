# src/telegram_handler.py
import requests
import base64

def send_message(data, api_key, b64_recipient_username):
    url = f"https://api.telegram.org/bot{api_key}/sendMessage"
    account_url = f"https://t.me/{base64.b64decode(b64_recipient_username)}"
    # Replace 'chat_id' with the actual method you use to get the chat ID
    chat_id = get_chat_id(api_key, b64_recipient_username)

    if chat_id is not None:
        message = f"New data:\n{data}"

        params = {
            'chat_id': chat_id,
            'text': message
        }

        response = requests.post(url, params=params)

        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print("Failed to send message.")
    else:
        print(f"Unable to get chat ID for {b64_recipient_username}")

def get_chat_id(api_key, username):
    # Replace this with the actual method to get the chat ID
    # You might use the Telegram Bot API to get the chat ID using the username
    # Example: https://api.telegram.org/bot<API_KEY>/getChat?username=<USERNAME>
    # Ensure proper error handling in your actual implementation
    chat_id_url = f"https://api.telegram.org/bot{api_key}/getChat?username={username}"
    response = requests.get(chat_id_url)

    if response.status_code == 200:
        chat_info = response.json()
        chat_id = chat_info.get('result', {}).get('id')
        return chat_id
    else:
        return None