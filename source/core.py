from text import Text as text
from design import Design as design

class Core:
    def __init__(self) -> str:
        text.init()

    '''Logic handling of malrowe goes here, encryption and more can be founded here.'''
    def encrypt_menu(self) -> str: ...

    '''Menu handling section goes here, manipulation of options will be founded here.'''
    def show_menu(self, options: dict) -> str:
        for opt in sorted(options):
            text(f'<green>({opt}) <white>| {options[opt][0]}')
    
    def show_banner(self) -> str:
        return text(f'<blue>{design.BANNER}')
    
    def show_info(self) -> str:
        return text('<blue>[!] <white>This application actually is in development, see: https://www.github.com/leoarayav/malrowe')
    
    def read_option(self, options: dict) -> any:
        while (opt := input('@pymalrowe > ')) not in options:
            text("<red>This option is invalid or doesnt exists")
        return opt
    
    def execute_options(self, option: any, options: dict) -> any:
        return options[option][1]()
    
    def generate_menu(self, options: any, output: any) -> str:
        option = 0
        try:
            while options != output:
                self.show_menu(options)
                option = self.read_option(options)
                self.execute_options(option, options)
        except Exception as err:
            return text(f"<red>Problem ocurred while generating menu from @malwore/core - {err}")
    
    def exit_menu(self) -> any:
        return exit(1)

    def main_menu(self) -> str:
        __menu_options__ = {
            '1': ('Encrypt your text with availables encryptions.', self.encrypt_menu),
            '2': ('Exit malrowe application.', self.exit_menu)
        }

        self.generate_menu(__menu_options__, '2')

    def initialize(self) -> any:
        try:
            self.show_banner()
            self.show_info()
        except Exception as err:
            return text(f"<red>Problem ocurred while initializing from @malwore/core - {err}")