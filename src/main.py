#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

from hunspell import Hunspell


def main():
    h = Hunspell('ko', hunspell_data_dir='dictionaries', system_encoding='UTF-8')
    text = input('Input Text : ').split()
    print(h.bulk_suggest(text))


if __name__ == "__main__":
    main()
