from fasthtml.common import RedirectResponse
from fasthtml.oauth import Beforeware, GitHubAppClient, _AppClient

import config

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
    client = TestGitHubAppClient()
else:
    if config.GH_OAUTH_ID and config.GH_OAUTH_SECRET:
        client = GitHubAppClient(
            client_id=config.GH_OAUTH_ID,
            client_secret=config.GH_OAUTH_SECRET
        )
    else:
        raise Exception("GitHub OAuth not set up.")

auth_callback = "/auth/oauth-redirect"

def before(request, session):
    auth = request.scope['auth'] = session.get('user_id', None)
    if not auth: return RedirectResponse("/auth/login", status_code=303)

beforeware = Beforeware(before, skip=['/auth/login', '/auth/oauth-redirect'])
