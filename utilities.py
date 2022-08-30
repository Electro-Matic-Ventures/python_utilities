from re import sub
from datetime import datetime

class Strings:

    def __init__(self):
        return
        
    def remove_all(self, haystacks, needles, new_needle):
        new_haystacks = []
        if new_needle in needles:
            return haystacks
        for haystack in haystacks:
            for needle in needles:
                while haystack.find(needle) >= 0:
                    haystack = haystack.replace(needle, new_needle)
            new_haystacks.append(haystack)
        return new_haystacks

    def capitalize_first_letter_of_each_word(self, value):
        strings = value.split(' ')
        _return = ''
        for _string in strings:
            _string = _string.lower()
            _return += _string[:1].upper() + _string[1:] + ' '
        return _return[:-1]

    def just_alpha_numeric(self, string):
        return sub('[^a-zA-Z0-9]','', string).strip()

    def split_multiple_delimeters(self, value, delimeters):
        if len(delimeters) == 0:
            return value
        delimeter = delimeters.pop()
        out = []
        for x in value:
            out.extend(x.split(delimeter))
        return self.split_multiple_delimeters(out, delimeters)

        
class Log:

    def __init__(self, path):
        if path == '': path = '.'
        self.__path = f'{path}/process_log.csv'
        return

    def create(self):
        with open(self.__path, 'w') as f:
            f.write(f'{datetime.now()}; log created\n')
        return

    def add_event(self, text):
        with open(self.__path, 'a') as f:
            f.write(f'{datetime.now()}; {text}\n')
        return