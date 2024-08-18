def lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return abs(a * b) // gcd(a, b)
