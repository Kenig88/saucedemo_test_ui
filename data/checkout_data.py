import os


class CheckoutInfoData:
    FIRST_NAME = os.getenv("FIRST_NAME")
    LAST_NAME = os.getenv("LAST_NAME")
    POSTAL_CODE = os.getenv("POSTAL_CODE")


class ErrorMessagesCheckoutInfo:
    EMPTY_FIRST_NAME = "Error: First Name is required"
    EMPTY_LAST_NAME = "Error: Last Name is required"
    EMPTY_POSTAL_CODE = "Error: Postal Code is required"


class CheckoutCompleteMessages:
    HEADER = "Thank you for your order!"
    TEXT = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
