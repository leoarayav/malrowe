from text import Text
from design import Design
from encryption import Encryption

class Core:
    def __init__(self) -> str:
        self.__text = Text
        self.__design = Design
        self.__encrypt = Encryption

    def show_menu(self, __name: str, __options: dict) -> str:
        '''
            This function show our content menu.

            Args:
                name (str): Menu or section name.
                options (dict): Available options.

            Returns:
                str: Our printed menu. 
        '''
        self.__text(f'<blue>py@malrowe ~ <blue>{__name}')
        for clave in sorted(__options):
            self.__text(f'<cyan>({clave}) <lwhite>| {__options[clave][0]}\n - - - - - - -')


    def read_option(self, options: dict) -> any:
        '''
            This function read options in our menu.

            Args:
                options (dict): Available options.
            
            Returns:
                Any: Option readed.
        '''
        while (a := input('@malrowe/option > ')) not in options:
            self.__text('<red>ERROR | Problem ocurred while reading option.')
        return a


    def execute_option(self, option: int, options: dict) -> any:
        '''
        This function execute an option in our menu.

        Args:
            option (int): Option in menu.
            options (dict): Options availables.

        Returns:
            any: Option executing.
        '''
        options[option][1]()

    def generate_menu(self, name: str, options: dict, outputOption: str) -> str:
        '''
        This function generate our menu.

        Args:
            name (str): Name of our menu.
            options (dict): Options available.
            outputOption (str): Our option output.
        
        Returns:
            str: Our menu.
        '''
        option = None
        while option != outputOption:
            self.show_menu(name, options)
            option = self.read_option(options)
            self.execute_option(option, options)

    def main_menu(self):
        '''This function you will find the main menu'''
        __main_menu__ = {
            '1': ('Encrypt your text.', self.malrowe_encryption),
            '2': ('Decrypt your text.', self.malrowe_decryption),
            '3': ('About.', self.malrowe_about),
            '4': ('Exit.', self.malrowe_exit)
        }

        self.generate_menu('Main Menu', __main_menu__, '4')

    def malrowe_encryption(self):
        '''This function contains encryption menu with availables encryptions'''
        __encryption_menu__ = {
            'a': ('Encryption with SHA224', self.malrowe_sha224),
            'b': ('Encryption with SHA256', self.malrowe_sha256),
            'c': ('Back to main menu.', self.main_menu)
        }

        self.generate_menu('@malrowe - Encryptions', __encryption_menu__, 'c')

    '''Main menu logic section will goes here'''
    def malrowe_decryption(self) -> None: TODO: ...

    def malrowe_about(self) -> any: TODO: ...

    def malrowe_exit(self) -> None:
        '''This function just close malrowe program'''
        return exit(1)

    '''Encryption menu logic section will be founded here'''
    def malrowe_sha224(self) -> bytes:
        text = input("pymalrowe/encryption: Write your secret text here > ")
        self.__encrypt.sha224(text)
    
    def malrowe_sha256(self) -> bytes:
        text = input("pymalrowe/encryption: Write your secret text here > ")
        self.__encrypt.sha256(text)
    
    def initialize(self) -> None:
        '''This function initialize malwore core application'''
        try:
            self.__text(f'<blue>{self.__design.LOGO}')
            self.__text(f'<cyan>{self.__design.BANNER}')
            self.main_menu()
        except Exception as err:
            self.__text(f'<red>ERROR | An problem was ocurred when initialize - {err}')