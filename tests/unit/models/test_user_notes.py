from datetime import datetime

import pytest
from sqlmodel import Session

from app.models import user_notes as user_notes_model
from app.models.models import User


def make_session_factory(test_engine):
    def _factory():
        return Session(test_engine)

    return _factory


@pytest.fixture
def user_with_id(test_session):
    user = User(
        id=11111,
        is_active=True,
        is_admin=False,
        gh_login="noteuser",
        gh_node_id="node111",
        gh_avatar_url="https://example.com/u.png",
        gh_type="User",
        gh_created_at=datetime(2024, 1, 1, 0, 0, 0),
    )
    test_session.add(user)
    test_session.commit()
    test_session.refresh(user)
    return user


def test_get_user_notes_empty(user_with_id, test_engine):
    factory = make_session_factory(test_engine)
    results = user_notes_model.get_user_notes(11111, session_factory=factory)
    assert results == []


def test_add_and_get_user_note(user_with_id, test_engine):
    factory = make_session_factory(test_engine)
    user_notes_model.add_user_note(
        user_id=11111,
        added_by_id=11111,
        note="Test note",
        session_factory=factory,
    )
    results = user_notes_model.get_user_notes(11111, session_factory=factory)
    assert len(results) == 1
    assert results[0].note == "Test note"
    assert results[0].user_id == 11111


def test_get_user_notes_multiple(user_with_id, test_engine):
    factory = make_session_factory(test_engine)
    user_notes_model.add_user_note(11111, 11111, "First note", session_factory=factory)
    user_notes_model.add_user_note(11111, 11111, "Second note", session_factory=factory)
    user_notes_model.add_user_note(11111, 11111, "Third note", session_factory=factory)
    results = user_notes_model.get_user_notes(11111, session_factory=factory)
    assert len(results) == 3


def test_notes_ordered_by_created_at_desc(user_with_id, test_engine):
    factory = make_session_factory(test_engine)
    user_notes_model.add_user_note(11111, 11111, "First", session_factory=factory)
    user_notes_model.add_user_note(11111, 11111, "Second", session_factory=factory)
    user_notes_model.add_user_note(11111, 11111, "Third", session_factory=factory)
    results = user_notes_model.get_user_notes(11111, session_factory=factory)
    assert len(results) == 3
    notes_text = [r.note for r in results]
    assert set(notes_text) == {"First", "Second", "Third"}


def test_get_notes_for_different_users(user_with_id, test_session):
    other_user = User(
        id=22222,
        is_active=True,
        is_admin=False,
        gh_login="otheruser",
        gh_node_id="node222",
        gh_avatar_url="https://example.com/o.png",
        gh_type="User",
        gh_created_at=datetime(2024, 1, 1, 0, 0, 0),
    )
    test_session.add(other_user)
    test_session.commit()
    factory = make_session_factory(test_session.get_bind())
    user_notes_model.add_user_note(
        11111, 11111, "User 11111 note", session_factory=factory
    )
    user_notes_model.add_user_note(
        22222, 22222, "User 22222 note", session_factory=factory
    )
    results_11111 = user_notes_model.get_user_notes(11111, session_factory=factory)
    results_22222 = user_notes_model.get_user_notes(22222, session_factory=factory)
    assert len(results_11111) == 1
    assert len(results_22222) == 1
    assert results_11111[0].note == "User 11111 note"
    assert results_22222[0].note == "User 22222 note"
