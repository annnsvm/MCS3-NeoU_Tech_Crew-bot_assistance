from helpers.error import *
from commands.notebook.Parser import cmd_and_string_reader, string_reader, tag_reader


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
        except Exception:
            return "Please enter right command"

    return inner


@input_error
def parse_input(user_input):
    cmd = (cmd_and_string_reader(user_input))[0]
    prep_str = (cmd_and_string_reader(user_input))[1]
    if cmd == "add-note" or cmd == "replace-note-text" or cmd == "add-text-to-note":
        *args , = string_reader(prep_str)
        return cmd, *args
    elif cmd == "add-tags" or cmd == "remove-tag":
        *args , = tag_reader(prep_str)
        return cmd, *args
    elif cmd == "show-note" or cmd == "remove-note" or cmd == "find-tagged-notes" or cmd == "about-note":
        return cmd, prep_str
    else:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
    return cmd, *args
