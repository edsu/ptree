import os
import re


def id2ptree(id, shorty_length=2, sep="/"):
    """Pass in a identifier and get back a PairTree path. Optionally
    you can pass in the "shorty length" (default is 2) and the
    path separator (default is /).
    """
    if sep == "": sep = "/"
    return sep + sep.join(_split_id(id, shorty_length)) + sep


def ptree2id(path, shorty_length=2, sep="/"):
    """Pass in a PairTree path and get back the identifier that it maps to.
    """
    # TODO: should this be smarter?
    return _decode("".join(path.split(sep)))


def _split_id(id, shorty_length):
    encoded_id = _encode(id)
    parts = []
    while encoded_id:
        parts.append(encoded_id[:shorty_length])
        encoded_id = encoded_id[shorty_length:]
    return parts


def _encode(s):
    if isinstance(id, unicode):
        s = s.encode('utf-8')

    s = _encode_regex.sub(_char2hex, s)
    parts = []
    for char in s:
        parts.append(_encode_map.get(char, char))
    return "".join(parts)


def _decode(id):
    parts = []
    for char in id:
        parts.append(_decode_map.get(char, char))
    dec_id = "".join(parts)
    return _decode_regex.sub(_hex2char, dec_id).decode("utf-8")


def _char2hex(m):
    return "^%02x"%ord(m.group(0))


def _hex2char(m):
    return chr(int(m.group(1), 16))


_encode_regex = re.compile(r"[\"*+,<=>?\\^|]|[^\x21-\x7e]", re.U)
_decode_regex = re.compile(r"\^(..)", re.U)
_encode_map = { '/' : '=',  ':' : '+',  '.' : ','  } # not easy on the eyes 
_decode_map = dict([(v, k) for k, v in _encode_map.items()]) # reversed 

