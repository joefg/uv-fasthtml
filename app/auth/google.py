from fasthtml.common import Button
from fasthtml.oauth import GoogleAppClient, redir_url

import config
from icons import google as google_icon


class GoogleOAuth():
    def __init__(self, auth_callback):
        self.client = GoogleAppClient(
            client_id=config.GH_OAUTH_ID,
            client_secret=config.GH_OAUTH_SECRET
        )
        self.auth_callback = auth_callback

    def login_button(self, request):
        redirect = redir_url(request, self.auth_callback)
        login_link = self.client.login_link(redirect)
        return Button(
            google_icon() + "&nbspSign in with Google",
            onclick=f"document.location='{login_link}'",
            type="button",
        )


if config.GH_OAUTH_ID and config.GH_OAUTH_SECRET:
    auth = GoogleOAuth("/auth/oauth-redirect")
else:
    raise Exception("Discord OAuth not configured.")
