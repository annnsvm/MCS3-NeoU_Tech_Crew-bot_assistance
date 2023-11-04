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
        except PhoneValueError as error:
            return error.message
        except NameValueError as error:
            return error.message
        except ContactValueError as error:
            return error.message
        except DateValueError as error:
            return error.message
        except BirthdayValueError as error:
            return error.message
        except IncorrectAddress as error:
            return error.message
        except Exception:
            return "Please enter right command"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
