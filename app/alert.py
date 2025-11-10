import httpx

import logging

import config


def telegram(msg: str) -> None:
    bot_token = config.TG_TOKEN
    chat_id = config.TG_ALERT_CHAT
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    if bot_token and chat_id and not config.TESTING:
        httpx.post(url, params={"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"})
    else:
        logging.warning("Telegram alert not sent. Consider setting it up.")


def slack(msg: str) -> None:
    url = config.SLACK_WEBHOOK_URL

    if url and not config.TESTING:
        httpx.post(url, params={"text": msg})
    else:
        logging.warning("Slack alert not sent. Consider setting it up.")


def discord(msg: str) -> None:
    webhook_id = config.DISCORD_WEBHOOK_ID
    webhook_token = config.DISCORD_WEBHOOK_TOKEN
    url = f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}"

    if webhook_id and webhook_token and not config.TESTING:
        httpx.post(url, params={"content" : msg})
    else:
        logging.warning("Discord alert not sent. Consider setting it up.")
