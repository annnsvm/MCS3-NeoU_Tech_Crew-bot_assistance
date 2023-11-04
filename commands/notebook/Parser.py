from helpers.error import *

def cmd_and_string_reader(user_input):
    separator = user_input.find(" ")
    cmd = user_input[:separator].strip().lower()
    prep_str = user_input[separator:].strip()
    return cmd, prep_str


def string_reader(prep_str):
    tags = []
    text = ""
    if prep_str.find('"') != -1 and prep_str.find('"') != len(prep_str) - prep_str[::-1].find('"')-1:
        text_string = prep_str[(prep_str.find('"')) : (len(prep_str) - prep_str[::-1].find('"'))]
        part_list = list(prep_str.partition(text_string))
        text = part_list[1].strip()
        part_list[2] = part_list[2].split(',')
        name = part_list[0].strip()
        for tag in part_list[2]:
            if len(tag.strip()) > 0:
                tags.append(tag.strip())
#   elif prep_str.find('"') != -1:
#       raise InputException('Note must have name without ""')
    else:
        name = prep_str
    *args , = name, text, tags
    return *args ,


def tag_reader(prep_str):
        prep_list = prep_str.split(':')
        args = []
        tags = []
        if len(prep_list ) == 2:
            args.append(prep_list [0].strip())
            for tag in prep_list [1].split(','):
                tags.append(tag.strip())
            args.append(tags)
#       else:
#           raise InputException(': must be before the tags')
        return args
    


