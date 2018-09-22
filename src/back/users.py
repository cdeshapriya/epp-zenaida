
from back.models.account import Account


def is_exist(email):
    """
    Return `True` if domain exists, doing query in Domain table.
    """
    return bool(Account.users.filter(email=email).first())


def find_account(email):
    """
    Return `Account` object created for that email address.
    """
    return Account.users.filter(email=email).first()

