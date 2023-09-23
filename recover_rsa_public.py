#!/usr/bin/env python3

"""Recovery RSA public key from two pairs of message and cipher.
"""

import math
import sys
import pyprimes


def recover_rsa_public(exps, msg1, sig1, msg2, sig2, mode=None):
    """Recover rsa public key."""
    if mode == "enc":
        msg1, sig1 = sig1, msg1
        msg2, sig2 = sig2, msg2

    for exp in exps:
        diff1 = pow(sig1, exp) - msg1
        diff2 = pow(sig2, exp) - msg2
        candidate = math.gcd(diff1, diff2)
        for prime in pyprimes.primes_below(1000000):
            while candidate % prime == 0:
                candidate //= prime
        if pow(sig1, exp, candidate) == msg1:
            if pow(sig2, exp, candidate) == msg2:
                return exp, candidate
    return 0, 0


def read_int_from_file(filename):
    """Read int value from file."""
    with open(filename, "rb") as ifile:
        return int.from_bytes(ifile.read(), "big")


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(f"usage: {sys.argv[0]} msg1 sig1 msg2 sig2 [enc]")
        sys.exit(1)

    msg1 = read_int_from_file(sys.argv[1])
    sig1 = read_int_from_file(sys.argv[2])
    msg2 = read_int_from_file(sys.argv[3])
    sig2 = read_int_from_file(sys.argv[4])

    mode = None
    if len(sys.argv) > 5 and sys.argv[5] == "enc":
        mode = sys.argv[5]

    pub = recover_rsa_public([3, 65537], msg1, sig1, msg2, sig2, mode)
    print("{:x}, {:x}".format(pub[0], pub[1]))
