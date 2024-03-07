# main.py
from config.config import TELEGRAM_API_KEY
from src.telegram_handler import send_message
from src.data_handler import prepare_data

def main():
    # Prepare data to be sent
    data = prepare_data()

    # my telegram username
    my_telegram_username_b64 = "c2lsYXNfY29kZXdlbGw="

    # Send data to my Telegram account
    send_message(data, TELEGRAM_API_KEY, my_telegram_username_b64)

if __name__ == "__main__":
    main()
