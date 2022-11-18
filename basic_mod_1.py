
def decode_talker(trimmed_coded, cypher_alpha) -> list:
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

def get_decoded_message(decoded_items: list) -> str:
    """returns the decoded message"""
    decoded_text = ""
    for i in decoded_items:
        decoded_text+= str(i)

    return decoded_text

if __name__ == "__main__":
    basic_mod_1_message =\
    "202 137 390 235 114 369 198 110 350 396 390 383 225 258 38 291 75 324 401 142 288 397".split(" ")
    basic_mod_2_message=\
        "104 290 356 313 262 337 354 229 146 297 118 373 221 359 338 321 288 79 214 277 131 190 377".split(" ")

    coded_message_1 = [ f"{int(code) % 37}" for code in basic_mod_1_message]
    coded_message_2 = [ f"{pow( int(code), -1 , 41)}" for code in basic_mod_2_message]
    
    alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' # this should be with the digits according to https://www.dcode.fr/base-36-cipher
    cypher_alpha = {i:x for i,x in zip (range(36), alphas)}


    print("picoCTF{"+ get_decoded_message(decode_talker(coded_message_1,cypher_alpha))+"}")