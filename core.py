BOLUO_LANGUAGE=["不要慌!","妈个鸡!","狗比!","有点实力。"]

def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])


def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


def encode_by_boluo(str):
    str = encode(str)
    print(str)
    result = str.replace("11", BOLUO_LANGUAGE[0]).replace("10", BOLUO_LANGUAGE[1]).replace("0", BOLUO_LANGUAGE[2]).replace("1", BOLUO_LANGUAGE[3])
    return result

def decode_by_boluo(str):
    str = str.replace(BOLUO_LANGUAGE[3], "1").replace(BOLUO_LANGUAGE[2], "0").replace(BOLUO_LANGUAGE[1], "10").replace(BOLUO_LANGUAGE[0], "11")
    result = decode(str)
    return result

