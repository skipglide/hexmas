from sympy import symbols, mod_inverse
from sympy.polys.polyfuncs import interpolate
from sympy.abc import x

def construct_secret(secret, modulus):
    

def reconstruct_secret(shares, modulus):
    n = len(shares)

    # Constructing the Lagrange basis polynomials modulo the modulus
    L = []
    for i in range(n):
        numerator = 1
        denominator = 1
        for j in range(n):
            if i != j:
                numerator *= x - shares[j][0]
                denominator *= shares[i][0] - shares[j][0]
        L.append(numerator / denominator)

    # Interpolating to find the polynomial
    polynomial = 0
    for i in range(n):
        polynomial += shares[i][1] * L[i]

    # Getting the constant term (which is the secret) modulo the modulus
    print(polynomial.subs(x, 0))
    secret = polynomial.subs(x, 0) % modulus
    return secret

def make_random_shares(secret, minimum, shares, prime=_PRIME):
    """
    Generates a random shamir pool for a given secret, returns share points.
    """
    if minimum > shares:
        raise ValueError("Pool secret would be irrecoverable.")
    poly = [secret] + [_RINT(prime - 1) for i in range(minimum - 1)]
    points = [(i, _eval_at(poly, i, prime))
              for i in range(1, shares + 1)]
    return points

shares = [(1, 2097890403),(2, 371732494),(3, 1170428974),(4, 1871058789),(5, 1485848919),(6, 885301891)]
modulus = 2147483647
secret = reconstruct_secret(shares, modulus)
print(secret)
secret = mod_inverse(secret, modulus)
print(secret)

