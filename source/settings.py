'''This module contains all settings of this program'''

# Methods availables of encryption.
__MALROWE_ENCRYPTION_METHODS = {
    ('md5', True),
    ('md5_sd', True),
    ('sha256', True),
    ('sha512', True),
    ('sha1', True),
    ('sha224', True)
}

# Initial configuration of @Malrowe
MALROWE = {
    "name": "Malrowe",
    "description": "A encryptor/decryptor tool called Malrowe",
    "version": "0.1.0",
    "private": False,
    "author": {
        "name": "leoarayav",
        "github": "https://www.github.com/leoarayav"
    },
    "tags": [
        'python-script',
        'pytools',
        'encrypt',
        'rsa',
        'coding',
        'schedule'
    ],
    "license": "MIT"
}