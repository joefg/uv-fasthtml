from fasthtml.common import RedirectResponse
from fasthtml.oauth import Beforeware, GitHubAppClient

import config

if config.GH_OAUTH_ID and config.GH_OAUTH_SECRET:
    client = GitHubAppClient(
        client_id=config.GH_OAUTH_ID,
        client_secret=config.GH_OAUTH_SECRET
    )

    auth_callback = "/auth/oauth-redirect"

    def before(request, session):
        auth = request.scope['auth'] = session.get('user_id', None)
        if not auth: return RedirectResponse("/auth/login", status_code=303)

    beforeware = Beforeware(before, skip=['/auth/login', '/auth/oauth-redirect'])
else:
    raise Exception("GitHub OAuth not configured.")
