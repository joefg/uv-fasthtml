


from fasthtml.common import Button, Div, Script
from fasthtml.oauth import GitHubAppClient, redir_url, _AppClient

import config
from components.icons import telegram as telegram_icon


def verify_telegram_auth(data: dict, bot_token: str) -> bool:
    """Validates the data received from the Telegram Login Widget."""
    auth_data = data.copy()
    received_hash = auth_data.pop('hash', None)
    if not received_hash:
        return False

    # Ensure the authentication request isn't outdated (e.g., older than 24 hours)
    if time.time() - int(auth_data.get('auth_date', 0)) > 86400:
        return False

    # Sort data alphabetically and format as key=value separated by newlines
    data_check_list = [f"{k}={v}" for k, v in sorted(auth_data.items())]
    data_check_string = "\n".join(data_check_list)

    # Compute the secret key using the SHA256 of the bot token
    secret_key = hashlib.sha256(bot_token.encode()).digest()

    # Generate the validation hash
    computed_hash = hmac.new(
        secret_key,
        data_check_string.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(computed_hash, received_hash)

def login_button(bot_username: str) -> Div:
    return Div(
        Script(
            src="https://oauth.telegram.org/js/telegram-login.js?6",
            data_client_id="",
            data_onauth="console.log(data)",
            data_request_access="write"
        ),
        Button("Sign in with Telegram", cls="tg-auth-button")
    )
