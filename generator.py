import secrets
import string

"""
Generates random password of 6 chars long
"""


class Generator:
    # returns a string of 6 chars of random letters and digits
    def generate(self):
        words = string.ascii_letters + string.digits
        text = ''.join(secrets.choice(words) for _ in range(6))  # number of char can be changed here
        return text
        # harvest number of passwords

    def collect(self, number):
        collection = []
        for _ in range(number):  # number = number of passwords needed
            word = self.generate()
            collection.append(word)
        collection = set(collection)
        collection = list(collection)
        return collection


Create = Generator()
passwords = Create.collect(20)
print(passwords)
