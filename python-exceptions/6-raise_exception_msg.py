#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise Exception
    except Exception:
        print(message)
