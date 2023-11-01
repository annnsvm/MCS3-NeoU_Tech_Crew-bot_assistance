from helpers.error import *


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me correct command please."
        except KeyError:
            return "User not found. Enter user name please."
        except IndexError:
            return "Give me name please."
        except IncorrectEmail as error:
            return error.message
        except Exception:
            return "Please enter right command"

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
