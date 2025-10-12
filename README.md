# RSA Demo (Educational)

Minimal RSA implementation in Python that generates keys, encrypts a short ASCII message as a big integer, then decrypts it.

> ⚠️ For learning only (no padding, not production-safe).

## Requirements

* Python 3.9+
* sympy

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install sympy
```

## Run

```bash
python main.py
```

## What the script does

* `generate_prime(n)`: picks two ~n-bit primes `p`, `q` with `sympy.randprime`
* `calculate_phi(p, q)`: φ = (p−1)(q−1)
* `generate_e_d(p, q)`: chooses public `e` (coprime with φ) and computes private `d = e⁻¹ mod φ`
* `encrypt(m, e, N)`: ASCII → int → `c = m^e mod N`
* `decrypt(c, d, N)`: `m = c^d mod N` → int → ASCII
* `test_RSA()`: demo using `"hi user"` and 2048-bit primes

## Configure

* Key size: in `test_RSA()`, change

```python
p, q = generate_prime(2048)   # primes of 2048 bits → ~4096-bit modulus
```

## Notes / Limitations

* No OAEP padding; raw RSA is insecure for real data.
* Python’s `random` isn’t a CSPRNG; fine for demos only.
* Make sure bit-range math is correct in prime generation.
