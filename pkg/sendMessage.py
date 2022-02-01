import datetime
import requests


def sendMessage(ip, port):
    botToken = "5130874573:AAFkkx3qkaq7dT2UoiIY3-UtQcE_IT5PaxE"
    chatId = "156050755"

    url = f"https://api.telegram.org/bot{botToken}/sendMessage"

    data = {
        'chat_id': chatId,
        'disable_web_page_preview': 'true',
        'text': f'Server {ip}:{port} down!\n{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    }

    requests.post(url, data=data)
