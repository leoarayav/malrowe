'''This module contains all encryptions availables on malrowe'''

import hashlib

class Encryption:
    '''Class Encryption of @malrowe'''
    
    @staticmethod
    def md5(text: str) -> bytes:
        '''
        This method encrypt any text to message-diggest algorithm md5 in bytes.

        Args:
            text (str) - Message text.
        
        Returns:
            bytes - MD5 Encrypted Text.
        '''
        try:
            xyz = hashlib.md5(text.encode())
            print(f"@malrowe/MD5: Your secret text has been encrypted > {xyz.digest()[:10]}")
        except Exception as err:
            print(err)
    
    @staticmethod
    def md5_sd(text: str) -> hex:
        '''
        This method encrypt any text to message-diggest algorithm md5 in string to hexadecimal.

        Args:
            text (str) - Message text.
        
        Returns:
            hex - Our text encrypted in hexadecimal.
        '''
        try:
            xyz = hashlib.md5(text.encode())
            print(f"@malrowe/MD5SD: Your secret text has been encrypted > {xyz.digest()[:10]}")
        except Exception as err:
            print(err)
    
    @staticmethod
    def sha256(text: str) -> hex:
        '''
        This method encrypt any text to secure-hash algorithm sha256 in string to hexadecimal.

        Args:
            text (str) - Message text.
        
        Returns:
            hex - Our text encrypted in hexadecimal.
        '''
        try:
            xyz = hashlib.sha256(text.encode())
            print(f"@malrowe/SHA256: Your secret text has been encrypted > {xyz.digest()[:10]}")
        except Exception as err:
            print(err)
    
    @staticmethod
    def sha512(text: str) -> bytes:
        '''
        This method encrypt any text to secure hash algorithm sha512 in string to bytes.

        Args:
            text (str) - Message text.
        
        Returns:
            bytes - This text encrypted.
        '''
        try:
            xyz = hashlib.sha512(text.encode())
            print(f"@malrowe/SHA512: Your secret text has been encrypted > {xyz.digest()[:10]}")
        except Exception as err:
            print(err)
    
    @staticmethod
    def sha1(text: str) -> bytes:
        '''
        This method encrypt any text to secure hash algorithm sha1 in string to bytes.

        Args:
            text (str) - Message text.
        
        Returns:
            bytes - This text encrypted.
        '''
        try:
            xyz = hashlib.sha1(text.encode())
            print(f"@malrowe/SHA1: Your secret text has been encrypted > {xyz.digest()[:10]}")
        except Exception as err:
            print(err)
    
    @staticmethod
    def sha224(text: str) -> bytes:
        '''
        This method encrypt any text to secure hash algorithm 224 in string to bytes.

        Args:
            text (str) - Message text.
        
        Returns:
            bytes - This text encrypted.
        '''
        try:
            xyz = hashlib.sha224(text.encode())
            print(f"@malrowe/SHA224: Your secret text has been encrypted > {xyz.digest()[:10]}")
        except Exception as err:
            print(err)