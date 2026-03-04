from datetime import datetime

import pytest

from app.database import engine
from app.models.models import User, UserNote
from sqlmodel import Session


@pytest.fixture(autouse=True)
def setup_database():
    with engine.begin() as conn:
        User.__table__.create(conn, checkfirst=True)
        UserNote.__table__.create(conn, checkfirst=True)

    with Session(engine) as session:
        existing_user = session.get(User, 459)
        if not existing_user:
            test_user = User(
                id=459,
                is_active=True,
                is_admin=False,
                gh_login="testuser",
                gh_node_id="mock_node_id",
                gh_avatar_url="https://example.com/avatar.png",
                gh_type="User",
                gh_created_at=datetime(2024, 1, 15, 10, 30, 0),
            )
            session.add(test_user)
            session.commit()

    yield
