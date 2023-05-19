#!/usr/bin/env python3



parser = __import__("regex_parser").parser


def main():
    while True:
       log = input()
       parser(log)


if __name__ == "__main__":
    main()
