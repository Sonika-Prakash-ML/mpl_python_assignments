# to create all possible strings by using 'a', 'e', 'i', 'o', 'u'.


def get_perms(chars, l, r):
    if l == r:
        print(''.join(chars), end=' ')
    else:
        for i in range(l, r + 1):
            chars[i], chars[l] = chars[l], chars[i]
            get_perms(chars, l + 1, r)
            chars[i], chars[l] = chars[l], chars[i]


if __name__ == "__main__":
    get_perms(['a', 'e', 'i', 'o', 'u'], 0, 4)
