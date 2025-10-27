from fasthtml.common import Button
from fasthtml.oauth import DiscordAppClient, redir_url

import config
from icons import discord as discord_icon


class DiscordOAuth():
    def __init__(self, auth_callback):
        self.client = DiscordAppClient(
            client_id=config.DISCORD_OAUTH_ID,
            client_secret=config.DISCORD_OAUTH_SECRET
        )
        self.auth_callback = auth_callback

    def login_button(self, request):
        redirect = redir_url(request, self.auth_callback)
        login_link = self.client.login_link(redirect)
        return Button(
            discord_icon() + "&nbspSign in with Discord",
            onclick=f"document.location='{login_link}'",
            type="button",
        )


if config.DISCORD_OAUTH_ID and config.DISCORD_OAUTH_SECRET:
    auth = DiscordOAuth("/auth/oauth-redirect")
else:
    raise Exception("Discord OAuth not configured.")
