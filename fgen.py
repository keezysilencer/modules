import argparse
import os
import secrets
import string

__author__ = "Keezy Silencer"

# this creates dir of the specified number in n with each dir 5 characters.
def create(n):
    fname = []
    for i in range(int(n)):
        words = string.ascii_letters + string.digits
        text = ''.join(secrets.choice(words) for _ in range(5))
        fname.append(text)
    for k in range(len(fname)):
        os.mkdir(fname[k])
    print("+++++++++++++ Done ++++++++++!\n" + str(n) + ' FILES CREATED SUCCESSFULLY!')


# this passes the number of files to be created from the terminal to create function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="Type in the number of files to create", type=int)
    args = parser.parse_args()
    create(args.num)


if __name__ == '__main__':
    main()
