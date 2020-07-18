#!/usr/bin/env python3

def validate_user(username, minlen):
    # assert checks if the condition is true and raises AssertionError
    # if it is False with the description provided
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        # signaling that our program is in trouble
        # raise introduces a type of error is something wrong happened
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
