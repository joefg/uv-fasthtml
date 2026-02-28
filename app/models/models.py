from datetime import datetime

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    is_active: bool
    is_admin: bool
    gh_login: str
    gh_node_id: str
    gh_avatar_url: str
    gh_type: str
    gh_created_at: datetime
    creation_date: datetime | None = Field(default=datetime.now())
    last_login: datetime | None = Field(default=datetime.now())


class UserNote(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    note_added_by: int
    note: str
    created_at: datetime | None = Field(default=datetime.now())
