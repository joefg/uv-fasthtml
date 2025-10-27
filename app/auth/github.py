from fasthtml.common import Button
from fasthtml.oauth import GitHubAppClient, redir_url, _AppClient

import config
from icons import github as github_icon

auth_callback = "/auth/oauth-redirect"

class GitHubOAuth():
    def __init__(self, auth_callback):
        if config.TESTING:
            self.client = TestGitHubAppClient()
        else:
            self.client = GitHubAppClient(
                client_id=config.GH_OAUTH_ID,
                client_secret=config.GH_OAUTH_SECRET
            )
        self.auth_callback = auth_callback

    def login_button(self, request):
        redirect = redir_url(request, self.auth_callback)
        login_link = self.client.login_link(redirect)
        return Button(
            github_icon() + "&nbspSign in with GitHub",
            onclick=f"document.location='{login_link}'",
            type="button",
        )


class TestGitHubAppClient(_AppClient):
    "A `WebApplicationClient` for GitHub oauth2"
    prefix = "https://oauth-mock.mock.beeceptor.com"
    base_url = f"{prefix}/oauth/authorize"
    token_url = f"{prefix}/oauth/token/github"
    info_url = f"{prefix}/userinfo/github"
    id_key = 'id'

    def __init__(self, code=None, scope=None, **kwargs):
        super().__init__('dummy-id', 'dummy-secret', code=code, scope=scope, **kwargs)

if config.TESTING:
    auth = GitHubOAuth(auth_callback=auth_callback)
else:
    if config.GH_OAUTH_ID and config.GH_OAUTH_SECRET:
        auth = GitHubOAuth(auth_callback=auth_callback)
    else:
        raise Exception("GitHub OAuth not set up.")