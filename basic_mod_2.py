def decode_talker(trimmed_coded, cypher_alpha) -> list:
    """
    decodes the message
    can be done more elegantly but i wanna go eat x2 :3
    """
    decoded_items = []
    for character in trimmed_coded:
        char_code = int(character)

        if char_code in range(27):
            decoded_items.append(cypher_alpha[char_code])
        elif char_code in range(27, 37):
            decoded_items.append(cypher_alpha[char_code])
        elif char_code == 37:
            decoded_items.append("_")
    return decoded_items


def get_decoded_message(decoded_items: list) -> str:
    """returns the decoded message"""
    decoded_text = ""
    for i in decoded_items:
        decoded_text += str(i)

    return decoded_text


if __name__ == "__main__":
    basic_mod_2_message = "104 290 356 313 262 337 354 229 146 297 118 373 221 359 338 321 288 79 214 277 131 190 377".split(
        " "
    )

    # in python to get the inverse nonsense u do this: pow(the number, -1, what u wanna devide by)

    coded_message_2 = [f"{pow( int(code) , -1, 41 )}" for code in basic_mod_2_message]

    alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    cypher_alpha = {i: x for i, x in zip(range(1, 37), alphas)}

    print(f"picoCTF{{{get_decoded_message(decode_talker(coded_message_2, cypher_alpha))}}}")