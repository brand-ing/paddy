import pytest
#from my_module.password_checker import check_password_complexity

def test_short_password():
    assert check_password_complexity("Pass1!") == "Password must be at least 8 characters long."

def test_no_uppercase():
    assert check_password_complexity("password1!") == "Password must contain at least one uppercase letter."

def test_no_lowercase():
    assert check_password_complexity("PASSWORD1!") == "Password must contain at least one lowercase letter."

def test_no_digit():
    assert check_password_complexity("Password!") == "Password must contain at least one digit."

def test_no_special_character():
    assert check_password_complexity("Password1") == "Password must contain at least one special character."

def test_strong_password():
    assert check_password_complexity("Password1!") == "Password is strong."
