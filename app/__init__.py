import os
from flask import Flask, request, jsonify
from linebot import LineBotApi
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from dotenv import load_dotenv

load_dotenv()

LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')


app = Flask(__name__)

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


@app.route('/book-confirm', methods=['POST'])
def send_booking_confirmation():
    payload = request.json
    if payload['lineId']:
        line_bot_api.push_message(payload['lineId'], TextSendMessage(text=payload['message']))
        return jsonify(['message', 'success'])
    else:
        return jsonify(['message', 'failure'])
