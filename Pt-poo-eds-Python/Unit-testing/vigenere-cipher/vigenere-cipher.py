"""
Our program will need an encode method that takes a keyword and plaintext and 
returns the ciphertext, and a decode method that accepts a keyword and ciphertext 
and returns the original message.

"""

class VigenerCipher:
    def __init__( self, keyword ):
        self.keyword = keyword
        
    def encode(self, plaintext ):
        # return "XECWQXUIVCRKHWA"
        plaintext = plaintext.replace(" ", "").upper()

        cipher = []
        keyword = self.extend_keyword( len(plaintext) )
        for p, k in zip( plaintext, keyword ):
            cipher.append(combine_character(p, k))
        return "".join(cipher)
    
        
    def combine_character( plain, keyword ):
        plain = plain.upper( )
        keyword = keyword.upper()
        plain_num = ord(plain) - ord('A')
        keyword_num = ord( keyword ) - ord('A')
        return chr ( ord('A') + (plain_num + keyword_num) % 26 )

    def extend_keyword( self, number ):
        repeats = number // len( self.keyword )+ 1
        return (self.keyword + repeats)[:number]

    def separate_character( cypher, keyword ):
        cypher = cypher.upper()
        keyword = keyword.upper()
        cypher_num = ord(cypher) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A')+ (cypher_num - keyword_num) % 26 )

        
    def decode(self, ciphertext ):
        plain = []
        keyword = self.extend_keyword(len(ciphertext))
        for p, k in zip(ciphertext, keyword):
            plain.append( separate_character(p,k) )
        return "".join(plain)

    
def _code(self, text, combine_func):
    text = text.replace(" ", "").upper()
    combined = []
    keyword = self.extend_keyword(len(text))
    for p,k in zip(text, keyword):
        combined.append(combine_func(p,k))
    return "".join(combined)

def encode(self, plaintext):
    return self._code(plaintext, combine_character)

def decode(self, ciphertext):
    return self._code(ciphertext, separate_character)
