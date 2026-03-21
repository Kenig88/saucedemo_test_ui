import os


class Username:
    STANDARD_USER = os.getenv("STANDARD_USER")
    LOCKED_OUT_USER = os.getenv("LOCKED_OUT_USER") # заблокированный пользователь, сообщение "BLOCKED_USER"
    PROBLEM_USER = os.getenv("PROBLEM_USER")
    PERFORMANCE_GLITCH_USER = os.getenv("PERFORMANCE_GLITCH_USER")
    ERROR_USER = os.getenv("ERROR_USER")
    VISUAL_USER = os.getenv("VISUAL_USER")
    INVALID_LOGIN = os.getenv("INVALID_LOGIN")
    EMPTY = os.getenv("EMPTY")


class Password:
    SECRET_SAUCE = os.getenv("SECRET_SAUCE")
    INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")
    EMPTY = os.getenv("EMPTY")


class ErrorMessages:
    EMPTY_USERNAME = "Epic sadface: Username is required"
    EMPTY_PASSWORD = "Epic sadface: Password is required"
    INCORRECT_DATA = "Epic sadface: Username and password do not match any user in this service"
    BLOCKED_USER = "Epic sadface: Sorry, this user has been locked out."
