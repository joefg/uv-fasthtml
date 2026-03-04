from datetime import datetime

import pytest
from sqlmodel import Session, SQLModel, create_engine

from app.models.models import User, UserNote


@pytest.fixture
def test_engine():
    engine = create_engine("sqlite:///:memory:", echo=False)
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture
def test_session(test_engine):
    with Session(test_engine) as session:
        yield session


@pytest.fixture
def sample_user_data():
    return {
        "id": 12345,
        "login": "testuser",
        "node_id": "abc123",
        "avatar_url": "https://example.com/avatar.png",
        "type": "User",
        "created_at": datetime(2024, 1, 15, 10, 30, 0),
    }


@pytest.fixture
def sample_user(sample_user_data, test_session):
    user = User(
        id=sample_user_data["id"],
        is_active=True,
        is_admin=False,
        gh_login=sample_user_data["login"],
        gh_node_id=sample_user_data["node_id"],
        gh_avatar_url=sample_user_data["avatar_url"],
        gh_type=sample_user_data["type"],
        gh_created_at=sample_user_data["created_at"],
    )
    test_session.add(user)
    test_session.commit()
    test_session.refresh(user)
    return user
