import app.models.users as users_model

"""
Note: The test user is id 459 from BeeCeptor.
"""

def mock_auth(client):
   client.get("/auth/oauth-redirect?code=mock-code-123")
   return client

def set_test_user_admin(state: bool):
    users_model.set_user_admin(459, state)

def set_test_user_active(state: bool):
    users_model.set_user_active(459, state)
