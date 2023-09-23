RSA and ECC public keys can be recovered from messages and/or signatures.
This is a demo.

See:
- https://crypto.stackexchange.com/questions/26188/rsa-public-key-recovery-from-signatures
- https://crypto.stackexchange.com/questions/18105/how-does-recovering-the-public-key-from-an-ecdsa-signature-work

# Requirments

```
pip3 install pyprimes
pip3 install ecdsa
```

# Examples

```
./recover_rsa_public.py examples/rsa_3/m1 examples/rsa_3/s1 examples/rsa_3/m2 examples/rsa_3/s2
3, c1e55f9b9e167dcc8262afd43e20639e5c60e8dffb912b595b05d1e0c7cafb62092bf78751cb698a82d19398ad499c0a9ed5f3025cc35d64a8c6932a1810fe620e895e3312a4b1de1eecc97490575306b5b8aeedb9baa10361c0079e207ea8261c1219c412c7c53194c4eba34b74e53472636b2fd3f43b658566998ed6cf1537

./recover_ecc_public.py examples/ecc/dgst examples/ecc/sig 
Candidate 0:
-----BEGIN PUBLIC KEY-----
MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEqwNtyrxhIvZsSsfgCVojJ8XQ0amqWkwt
U39jySmTN8HldfSXY/SzWw/eH6gPabLvxqtIC/Ge0LUG0Haa3curZQ==
-----END PUBLIC KEY-----

Candidate 1:
-----BEGIN PUBLIC KEY-----
MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEDtIclVaxmim5PudM5S/GAXeNL3Mr9+MK
hJd2RqdEfGv/N0QjfdLfw37Irxyhbeh09yT4DLTJFkxUuUYPw5JRDg==
-----END PUBLIC KEY-----
```

# Benchmark

- Hardware: Intel Core i7-10700 CPU @ 2.90GHz × 16
- Sofeware:
	- Os: Ubuntu 20.04.6 LTS
	- Python: 3.8.10
	- pyprimes: 0.1
	- ecdsa: 0.18.0

| Alg | Parameters    | Time        |
|-----|---------------|-------------|
| RSA | 1024bit, e=3  | 0m0.158s    |
| RSA | 2048bit, e=f4 | 273m53.345s |
| ECC | SECP256k1     | 0m0.046s    |
