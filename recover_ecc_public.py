#!/usr/bin/env python3

"""Recover ECC public key from signature.
"""

import sys
from ecdsa import VerifyingKey
from ecdsa import curves
from ecdsa.util import sigdecode_der


def recover(dat, sig):
    """Recover ECC public key."""
    keys = VerifyingKey.from_public_key_recovery_with_digest(
        sig, dat, curves.SECP256k1, sigdecode=sigdecode_der)
    return (key.to_pem() for key in keys)


def read_file(filename):
    """Read a file."""
    with open(filename, "rb") as ifile:
        return ifile.read()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} dgst_file sig_file")
        print(f"    NOTE: sig_file must be SECP256k1 signature, DER encoded.")
        sys.exit(1)

    dgst = read_file(sys.argv[1])
    signature = read_file(sys.argv[2])
    keys = recover(dgst, signature)
    for i, key in enumerate(keys):
        print(f"Candidate {i}:")
        print(key.decode())
