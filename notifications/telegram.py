import requests

def tg_send_message(api_key, chat_id, change_log_url, exchange):
    api_url = f'https://api.telegram.org/bot{api_key}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': f'🔴New update on {exchange}🔴 \n {change_log_url}'
    }
    response = requests.post(api_url, data=data)
    if response.status_code != 200:
        print("Error sending message to telegram!")
