from settings import MALROWE
from text import Text

class Design:

    Text.init()

    LOGO = f'''

    ███    ███      █████      ██          ██████       ██████      ██     ██     ███████ 
    ████  ████     ██   ██     ██          ██   ██     ██    ██     ██     ██     ██      
    ██ ████ ██     ███████     ██          ██████      ██    ██     ██  █  ██     █████   
    ██  ██  ██     ██   ██     ██          ██   ██     ██    ██     ██ ███ ██     ██      
    ██      ██     ██   ██     ███████     ██   ██      ██████       ███ ███      ███████

                                    Version {MALROWE["version"]} 
    '''

    BANNER = f'''
    {LOGO}
        Developed by @{MALROWE["author"]["name"]} ensuring your privacity and securing your keys.
    '''