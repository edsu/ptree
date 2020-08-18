import sys
if sys.version_info > (3,):
    from builtins import chr
import re


def id2ptree(id, sep="/", relpath=False):
    """Pass in a identifier and get back a PairTree path. Optionally
    you can pass in the path separator (default is /). Set relpath=True to
    omit the leading separator.
    """
    if sep == "": sep = "/"
    return (not relpath and sep or "") + sep.join(_split_id(id)) + sep


def ptree2id(path, sep="/"):
    """Pass in a PairTree path and get back the identifier that it maps to.
    """
    parts = path.strip().split(sep)
    id_parts = []
    for part in parts:
        if len(part) == 2:
            id_parts.append(part)
        elif len(part) == 1:
            if id_parts:
                id_parts.append(part)
                break
        elif len(part) > 2:
            if id_parts:
                break
    return _decode("".join(id_parts))


def _split_id(id):
    encoded_id = _encode(id)
    parts = []
    while encoded_id:
        parts.append(encoded_id[:2])
        encoded_id = encoded_id[2:]
    return parts


def _encode(s):
    if sys.version_info > (3,):
        test_type = str
    else:
        test_type = unicode
    if isinstance(s, test_type):
        s = s.encode('utf-8')

    regex_chars = r"[\"*+,<=>?\\^|]|[^\x21-\x7e]"
    if sys.version_info > (3,) and isinstance(s, bytes):
        s = re.compile(regex_chars.encode('utf-8')).sub(_char2hex, s)
        s = s.decode('utf-8')
    else:
        s = re.compile(regex_chars, re.U).sub(_char2hex, s)

    parts = []
    for char in s:
        parts.append(_encode_map.get(char, char))
    return "".join(parts)


def _decode(id):
    parts = []
    for char in id:
        parts.append(_decode_map.get(char, char))
    dec_id = "".join(parts)
    try:
        return _decode_regex.sub(_hex2char, dec_id).decode("utf-8")
    except AttributeError:
        return _decode_regex.sub(_hex2char, dec_id)


def _char2hex(m):
    if sys.version_info > (3,) and isinstance(m.group(0), bytes):
        return b"^%02x"%ord(m.group(0))
    else:
        return "^%02x" % ord(m.group(0))


def _hex2char(m):
    return chr(int(m.group(1), 16))


_decode_regex = re.compile(r"\^(..)", re.U)
_encode_map = { '/' : '=',  ':' : '+',  '.' : ','  } # not easy on the eyes
_decode_map = dict([(v, k) for k, v in list(_encode_map.items())]) # reversed 

