import os


class CheckoutDataCheckoutYourInformationPage:
    FIRST_NAME = os.getenv("FIRST_NAME")
    LAST_NAME = os.getenv("LAST_NAME")
    POSTAL_CODE = os.getenv("POSTAL_CODE")


class ErrorMessagesCheckoutYourInfoPage:
    EMPTY_FIRST_NAME = "Error: First Name is required"
    EMPTY_LAST_NAME = "Error: Last Name is required"
    EMPTY_POSTAL_CODE = "Error: Postal Code is required"
