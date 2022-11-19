
def generate_usernames() -> list[str]:
    """
        returns a list from the usernames file
    """
    user_names:list[str] = []
    with open("./leak/usernames.txt", 'r') as leaked_usernames:
        for user_name in leaked_usernames:
            user_names.append(user_name.split('\n')[0] )
    return user_names

def generate_passwords() -> list[str]:
    """
        returns a list from the passwords file
    """
    hashed_passwords : list[str] = []
    with open("./leak/passwords.txt", 'r') as leaked_passwords:
        for line in leaked_passwords:
            hashed_passwords.append(line.split("\n")[0])
    return hashed_passwords


def get_user_hashed_pawssord(username:str, collection:dict) -> str:
    """
        takes in a username and spits out either the hased password or and empty string
    """
    return collection.get(username, "")


if __name__ == "__main__":
    user_names = generate_usernames()
    hashed_passwrods = generate_passwords()

    hashed_user_passwords = { user:password for user,password in zip( generate_usernames(), generate_passwords()) }        
    
    user_hash = get_user_hashed_pawssord("cultiris", hashed_user_passwords)
    import codecs
    password_or_challange_code = codecs.decode(user_hash, 'rot_13')
    from pprint import pprint
    pprint( password_or_challange_code )
    