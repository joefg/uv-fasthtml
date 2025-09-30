import httpx

import logging

import config


def telegram(msg: str) -> None:
    bot_token = config.TG_TOKEN
    chat_id = config.TG_ALERT_CHAT
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    if bot_token and chat_id:
        httpx.post(url, params={"chat_id": chat_id, "text": msg})
    else:
        logging.warning("Telegram alert not sent. Consider setting it up.")
