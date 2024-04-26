#!/usr/bin/env python3
""" End-to-end integration test """
import requests


BASE_URL = "http://0.0.0.0:5000"


def register_user(email: str, password: str) -> None:
    """ registers a user """
    url = f"{BASE_URL}/users"
    body = {
        "email": email,
        "password": password,
    }
    response = requests.post(url, data=body)
    assert response.status == 200
    assert response.json() == {"email": email, "message": "user created"}

    response = requests.post(url, data=body)
    assert response.status == 400
    assert response.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """ logging in with a wrong password """
    url = f"{BASE_URL}/sessions"
    body = {
        "email": email,
        "password": password,
    }

    response = requests.post(url, data=body)
    assert response.status == 401


def log_in(email: str, password: str) -> str:
    """ log in """
    url = f"{BASE_URL}/sessions"
    body = {
        "email": email,
        "password": password,
    }

    response = requests.post(url, data=body)
    assert response.status == 200
    assert response.json() == {"email": email, "message": "logged in"}
    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """ tests requesting a profile while not logged in """
    url = f"{BASE_URL}/profile"
    response = requests.get(url)
    assert response.status == 403


def profile_logged(session_id: str) -> None:
    """ Tests retrieving profile information whilst logged in. """
    url = f"{BASE_URL}/profile"
    request_cookies = {
        "session_id": session_id,
    }
    response = requests.get(url, cookies=request_cookies)
    assert response.status == 200
    assert "email" in response.json()


def log_out(session_id: str) -> None:
    """ tests logging out """
    url = f"{BASE_URL}/profile"
    request_cookies = {
        "session_id": session_id,
    }
    response = requests.delete(url, cookies=req_cookies)
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """ tests resetting passwords """
    url = f"{BASE_URL}/reset_password"
    response = requests.post(url, body={"email": email})

    assert response.status == 200
    assert "email" in response.json()
    assert response.json()["email"] == email
    assert "reset_token" in response.json()
    return response.json().get("reset_token")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ tests updating password """
    url = f"{BASE_URL}/reset_password"
    body = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password,
    }
    response = requests.put(url, data=body)

    assert response.status == 200
    assert response.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
