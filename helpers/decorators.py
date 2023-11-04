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
        except NoteInputError as error:
            return error.message
        except Exception:
            return "Please enter right command"
    return inner

@input_error
def parse_input(user_input):
    cmd = (ParserCommands.cmd_and_string_reader(user_input))[0]
    prep_str = (ParserCommands.cmd_and_string_reader(user_input))[1]
    if cmd == "add-note" or cmd == "replace-note-text" or cmd == "add-text-to-note":
        *args , = ParserCommands.string_reader(prep_str)
        return cmd, *args
    elif cmd == "add-tags" or cmd == "remove-tag":
        *args , = ParserCommands.tag_reader(prep_str)
        return cmd, *args
    elif cmd == "show-note" or cmd == "remove-note" or cmd == "find-tagged-notes" or cmd == "about-note":
        return cmd, prep_str
    else:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
    return cmd, *args


class ParserCommands:

    @input_error
    def cmd_and_string_reader(user_input):
        separator = user_input.find(" ")
        cmd = user_input[:separator].strip().lower()
        prep_str = user_input[separator:].strip()
        return cmd, prep_str
    

    @input_error
    def string_reader(prep_str):
        tags = []
        text = ""
        if prep_str.find('"') != -1 and prep_str.find('"') != len(prep_str) - prep_str[::-1].find('"')-1:
            text_string = prep_str[(prep_str.find('"')) : (len(prep_str) - prep_str[::-1].find('"'))]
            part_list = list(prep_str.partition(text_string))
            text = part_list[1].strip()
            part_list[2] = part_list[2].split(',')
            name = part_list[0].strip()
            if len(name) == 0:
                raise NoteInputError('Note must have name')
            for tag in part_list[2]:
                if len(tag.strip()) > 0:
                    tags.append(tag.strip())
        elif prep_str.find('"') != -1:
            raise NoteInputError('Note must have name without ""')
        else:
            name = prep_str
        *args , = name, text, tags
        return *args ,

    @input_error
    def tag_reader(prep_str):
            prep_list = prep_str.split(':')
            args = []
            tags = []
            if len(prep_list ) == 2:
                args.append(prep_list [0].strip())
                for tag in prep_list [1].split(','):
                    tags.append(tag.strip())
                args.append(tags)
            else:
                raise NoteInputError(': must be before the tags')
            return args
