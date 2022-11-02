'''This module handles every text methods like console alerts, messages and more'''
import colorama

class Text:
    '''Class Text of @Malrowe'''

    __colors__ = {
        '<red>': colorama.Fore.RED,
        '<blue>': colorama.Fore.BLUE,
        '<green>': colorama.Fore.GREEN,
        '<white>': colorama.Fore.WHITE
    }

    def __init__(self, output: str, parse: str = True) -> None:
        if parse:
            output = self.__parse(output)
        self.message(output)
    
    @staticmethod
    def init() -> None:
        colorama.init()
    
    def __parse(self, text: str) -> str:
        for k, v in self.__colors__.items():
            text = text.replace(k, v)
        return text
    
    def message(self, text: str) -> None:
        print(colorama.Style.RESET_ALL + text)