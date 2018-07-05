import base64
from io import BytesIO

import struct


def encode_hashes(version: int, starting_class: int, ascendency: int, fullscreen: int, hashes: list) -> str:
    """
    Creates a valid poe skilltree url payload
    :param version:
    :param starting_class:
    :param ascendency:
    :param fullscreen:
    :param hashes:
    :return:
    """
    # [ver,charclass,asc,[4byte ints]]
    bytes = bytearray(struct.pack('>ibbb', version, starting_class, ascendency, fullscreen))
    for tmpHash in hashes:
        for byte in struct.pack('>H', tmpHash):
            bytes.append(byte)
    return base64.urlsafe_b64encode(bytes).decode("utf-8")


def decode_url(payload: str) -> tuple:
    """
    Decodes a poe skilltree url to a tuple
    :param payload: string after the last slash
    :return: tuple that contains version, char, ascendency, fullscreen, nodes[]
    """
    bytes = base64.urlsafe_b64decode(payload)
    # bytes 0-3 contain the version
    ver = struct.unpack(">i", bytes[0:4])[0]
    # bytes4-6 contain the class, ascendency and fullscreen status
    char, ascendency, fullscreen = struct.unpack("bbb", bytes[4:7])
    start = 7
    offset = 2
    # rest of the bytes contain the hashes
    nodes = []
    for count in range(start, len(bytes), 2):
        nodes.append(struct.unpack(">H", bytes[count:count + offset])[0])
    return ver, char, ascendency, fullscreen, nodes



