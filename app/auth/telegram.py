from fasthtml.common import Button, Div, Script
from fasthtml.oauth import GitHubAppClient, redir_url, _AppClient

import httpx2

import config
from components.icons import telegram as telegram_icon


def verify_telegram_auth(data: dict, bot_token: str) -> bool:
    """Validates the data received from the Telegram Login Widget."""
    auth_data = data.copy()
    received_hash = auth_data.pop('hash', None)
    if not received_hash:
        return False

    # Ensure the authentication request isn't outdated (e.g., older than 24 hours)
    outdated = time.time() - int(auth_data.get('auth_date', 0)) > 86400:
    if outdated:
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


class TelegramAppClient(_AppClient):
    def __init__(self, domain, client_id, client_secret, code=None, scope=None, redirect_uri="", **kwargs):
        self.redirect_uri,self.domain = redirect_uri,domain
        config = self._fetch_openid_config()
        self.base_url,self.token_url,self.info_url = config["authorization_endpoint"],config["token_endpoint"],config["userinfo_endpoint"]
        super().__init__(client_id, client_secret, code=code, scope=scope, redirect_uri=redirect_uri, **kwargs)

    def _fetch_openid_config(self):
        return httpx2.get(f"https://{self.domain}/.well-known/openid-configuration").raise_for_status().json()

    def login_link(self, req):
        d = dict(response_type="code", client_id=self.client_id, scope=self.scope, redirect_uri=redir_url(req, self.redirect_uri))
        return f"{self.base_url}?{urlencode(d)}"


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
