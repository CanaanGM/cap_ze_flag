from typing import List

def decode_talker(trimmed_coded, cypher_alpha) -> List:
    """
    decodes the message
    can be done more elegantly but i wanna go eat :3
    """
    decoded_items = []
    for character in trimmed_coded:
        char_code = int(character)
        
        if char_code in range(26):
            decoded_items.append(cypher_alpha[char_code])
        elif char_code in range(26, 36):
            decoded_items.append(cypher_alpha[char_code])
        elif char_code == 36:
            decoded_items.append("_")
    return decoded_items


if __name__ == "__main__":
    to_be_decoded =\
    "202 137 390 235 114 369 198 110 350 396 390 383 225 258 38 291 75 324 401 142 288 397".split(" ")

    trimmed_coded = [ f"{int(code) % 37}" for code in to_be_decoded]
    
    alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' # this should be with the digits according to https://www.dcode.fr/base-36-cipher
    cypher_alpha = {i:x for i,x in zip (range(36), alphas)}

    decoded_text = ""
    for i in decode_talker(trimmed_coded,cypher_alpha):
        decoded_text+= str(i)
        
    print("picoCTF{"+ decoded_text+"}")