from utils import is_valid_email

import models.users as users_model

def validate_registration(email: str, password: str) -> bool:
    if not email: raise ValueError("Email not provided.")
    if not is_valid_email(email): raise ValueError("Email not valid.")
    if not password: raise ValueError("Password not provided.")

    if len(password) < 8:
        raise ValueError("Password is too short: it needs to be 8 characters or longer.")

    if email and password:
        return True

def register_user(email: str, password: str):
    is_user = users_model.get_user(email)
    if is_user: raise ValueError("User already exists.")
    validate_registration(email, password)
    new_user = users_model.register_user(email, password)
    return new_user

def authenticate_user(email: str, password: str):
    is_user = users_model.get_user(email)
    if not is_user:
        raise ValueError("User does not exist")
    else:
        user = users_model.authenticate_user(email, password)
        if not user: raise ValueError("Incorrect password.")
        else: users_model.update_last_login(user.id)
        return user