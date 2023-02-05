#!/usr/bin/env python
import json
import sys


class BigCharacters:
    def __init__(self, filename):
        with open(filename) as file:
            self._raw_data = json.load(file)
        self._validate_json()
        self._block_size = self._raw_data['block_size']
        self._characters = self._raw_data['characters']
        self._validate_characters()

    def _validate_json(self):
        for field in ['block_size', 'characters']:
            if field not in self._raw_data.keys():
                print('ERROR: Missing data field:', field)
                sys.exit(1)

    def _validate_characters(self):
        for ch in self._characters.keys():
            lines = self._characters[ch]
            if len(lines) != self._block_size:
                print('ERROR: Inconsistent line count for character:', ch)
                sys.exit(1)
            for line in lines:
                if len(line) != self._block_size:
                    print('ERROR: Inconsistent line length for character:', ch)
                    sys.exit(1)

    def _translate_characters(self, s):
        characters = []
        for ch in s:
            if ch not in self._characters.keys():
                print('ERROR: String contains unknown character(s):', s)
                sys.exit(1)
            characters.append(self._characters[ch])
        return characters

    def translate(self, s):
        result = ''
        characters = self._translate_characters(s)
        n = len(characters)
        for r in range(self._block_size):
            for i in range(n):
                result += characters[i][r]
            result += '\n'
        return result


def main():
    big_characters = BigCharacters('characters.json')
    args = sys.argv[1:]
    if len(args) == 0:
        args = ['TEST']
    for arg in args:
        print(big_characters.translate(arg))


if __name__ == '__main__':
    main()
