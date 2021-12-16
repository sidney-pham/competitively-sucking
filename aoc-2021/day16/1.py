from itertools import islice
import copy

hex_to_binary = lambda x: bin(int(x, 16))[2:].zfill(len(x) * 4)
binary_to_decimal = lambda x: int(x, 2)
take = lambda xs, n: "".join(islice(xs, n))

hexa = open("input.txt").read().strip()
# Using iterators was a bad idea...
binary = iter(hex_to_binary(hexa))


def solve(binary):
    version = binary_to_decimal(take(binary, 3))
    type_id = binary_to_decimal(take(binary, 3))

    if type_id == 4:
        literal = ""
        next_5 = take(binary, 5)
        while next_5:
            if next_5[0] == "1":
                literal += next_5[1:]
                next_5 = take(binary, 5)
            else:
                literal += next_5[1:]
                next_5 = None
        return version
    else:
        total = version
        length_type_id = take(binary, 1)
        if length_type_id == "0":
            total_length = binary_to_decimal(take(binary, 15))
            new_binary = iter(take(binary, total_length))
            # Read as many packets from total_length digits.
            while list(copy.copy(new_binary)):  # Yikes.
                total += solve(new_binary)
        else:
            num_sub_packets = binary_to_decimal(take(binary, 11))
            # Read num_sub_packets from binary.
            for _ in range(num_sub_packets):
                total += solve(binary)
        return total


print(solve(binary))
