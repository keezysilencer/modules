import random
import string
import secrets


class Key:
    def __init__(self):
        self.key = ''
        self.generate_key()

    def verify(self):
        score = 0
        check_digit = self.key[0]
        check_digit_count = 0
        __chunks = self.key.split('-')
        for chunk in __chunks:
            if len(chunk) != 4:
                print('chunk okay')
            for char in chunk:
                if char == check_digit:
                    check_digit_count += 1
                    print('counting the number of characters present')
                score += ord(char)
        if score == 1772 and check_digit_count == 3:
            print('valid')
        else:
            self.generate_key()

    def generate_key(self):
        __letters = string.ascii_lowercase + string.digits
        __chunk = ''
        while len(self.key) < 25:
            char = random.choice(__letters)
            self.key += char
            __chunk += char
            if len(__chunk) == 4:
                self.key += '-'
                __chunk = ''

        self.key = self.key[:-1]
        return self.key

    def __str__(self):
        return self.generate_key()
k = Key()
print(k.verify())
