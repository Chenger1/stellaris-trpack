from dataclasses import dataclass
from typing import Union, Dict

import re


@dataclass
class Parsed:
    """Class only stores keys:values in format:
        Original line: 'trait_additrait_ephemeral:0 "Ephemeral"'
        Dict:
        {'trait_additrait_ephemeral': 'Ephemeral'}
    Not a part of the public API
    """
    keys: Dict[str, str]


class Parser:
    """
        Not a part of the public API
    """
    temp = re.compile(': |:0|:1|:"')  # regular exp. template

    @classmethod
    def parsing(cls, file_path: str):
        """
        :param file_path:
        :return: object 'Parsed' that includes keys:values store
        """
        keys: Dict[str, str] = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            for index, line in enumerate(file):
                if cls.search(line) == 1:
                    if (line[0] and line[1]) != '#':
                        split = cls.temp.split(line)
                        a = line.find('"')
                        lt = line[a + 1:-2]
                        keys[split[0]] = lt+'\n'
                    else:
                        keys[f'n-{index}'] = '\n'  # Storing '\n' symbols to match with original parse algorithm
                else:
                    keys[f'n-{index}'] = '\n'
        return Parsed(keys)

    @classmethod
    def search(cls, line):
        match = cls.temp.search(line)
        if match is not None:
            return 1
        else:
            return 0


class Comparator:
    """
    Part of the public API
    """
    def __init__(self, new, old):
        self.new = Parser.parsing(new)
        self.old = Parser.parsing(old)

    def comparing(self) -> Union[list, bool]:
        """
         Returns 'False' if both len are equal, means that new file doesn`t contain new lines
         Otherwise returns 'list' with old-translated lines and new one
        :return: False, list
        """
        if len(self.new.keys.values()) != len(self.old.keys.values()):
            for key, value in self.new.keys.items():
                try:
                    if value == '\n':
                        continue
                    if value != self.old.keys[key]:
                        self.new.keys[key] = self.old.keys[key]
                except KeyError:  # if new file contains new line, dict with old lines won`t have special keys for them
                    continue
            return list(self.new.keys.values())
        else:
            return False


def run():
    """
    Test function
    """
    temp = Comparator('file1', 'file2')  # TODO rewrite using descriptors
    result = temp.comparing()
    print(result)


if __name__ == '__main__':
    run()
