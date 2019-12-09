def get_formatted_name(first, last,middle=''):
    if middle:
        fullname = '{} {} {}'.format(first, middle, last)
    else:
        fullname = '{} {}'.format(first, last)
    return fullname.title()