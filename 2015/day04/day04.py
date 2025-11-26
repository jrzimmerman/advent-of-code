import hashlib


def generate_hash(secret_key, i):
    key_int = secret_key + str(i)
    encoded = key_int.encode()

    return hashlib.md5(encoded).hexdigest()


with open("./input.txt", "r") as file:
    secret_key = file.read().strip()


def calc_part1(secret_key):
    found_hash = False
    i = 1
    while not found_hash:
        md5_hash = hashlib.md5((secret_key + str(i)).encode()).hexdigest()
        # md5_hash = generate_hash(secret_key, i)
        if md5_hash[:6] == "000000":
            print(i)
            found_hash = True

            return i

        i += 1


# assert calc_part1("abcdef") == generate_hash(
#     "abcdef", 609043
# )  # 000001dbbfa3a5c83a2d506429c7b00e
# assert calc_part1("pqrstuv") == generate_hash(
#     "pqrstuv", 1048970
# )  # 000006136ef2ff3b291c85725f17325c

part1 = calc_part1(secret_key)
print(f"part1: {part1}")
