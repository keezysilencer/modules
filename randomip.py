"""
This will generate random Ip addresses.
"""
from random import randrange

__author__ = "Keezy Silencer"


class RandomIP(object):
    """
    Class to generate random valid IP's
    """

    def _generateip(self):
        invalid = [10, 127, 169, 172, 192]
        first = randrange(1, 256)

        while first is invalid:
            first = randrange(1, 256)

        _ip = ".".join([str(first), str(randrange(1, 256)),
                        str(randrange(1, 256)), str(randrange(1, 256))])
        return _ip


if __name__ == "__main__":
    randomip = RandomIP()
    print(randomip._generateip())
