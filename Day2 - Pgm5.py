# to create all possible strings by using 'a', 'e', 'i', 'o', 'u'.

import random


def get_perms(chars):
    res = [''.join(chars)]
    while len(res) != 120:
        random.shuffle(chars)
        s = ''.join(chars)
        if s in res:
            continue
        else:
            res.append(s)
    return res


if __name__ == "__main__":
    perms = get_perms(['a', 'e', 'i', 'o', 'u'])
    print("The possible strings are:")
    print(*perms, sep=", ")
