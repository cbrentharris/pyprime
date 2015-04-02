import random

class Prime:
    u""" 

    A python class to perform relatively quick generation of large primes and 
    primality test with a good percentage of correctness.

    """

    @classmethod
    def is_prime(cls, n):
        u""" is prime can be changed to use desired check function """
        return cls.probabilistic_primality_test(n)

    @classmethod
    def probabilistic_primality_test(cls, n):
        u""" Rabin's probabalistic primality test """
        bases = cls.generate_random_bases(n)
        return all([cls.passes_miller_test(base, n) for base in bases])

    @staticmethod
    def generate_random_bases(n):
        u""" If Riemann hypothesis is true, only need 1/4 * n random bases """
        number_of_bases = 50 if n > 50 * 4 else n / 4
        bases = set()
        while len(bases) < number_of_bases:
            random_base = random.randint(2, n - 1)
            if random_base not in bases:
                bases.add(random_base)
        return bases

    @staticmethod
    def passes_miller_test(base, n):
        u""" Implemenation of miller test """
        n_minus_one = n - 1
        #Initial check when (n - 1) = 2^k * t
        while n_minus_one % 2 == 0:
            if pow(base, n_minus_one, n) not in [1, n - 1]:
                return False
            n_minus_one /= 2

        #Last check when (n - 1) = t
        return pow(base, n_minus_one, n) in [1, n - 1]

    @classmethod
    def generate_large_prime(cls, upper_bound):
        lower_bound = 2**200
        while True:
            x = random.randint(lower_bound, upper_bound)
            is_prime = cls.probabilistic_primality_test(x)
            if is_prime:
                return x


def main():
    first_answer = raw_input("Would you like to run a probabilistic primality test? (Y/N) ")
    if first_answer.lower() == "y":
        try:
            number_to_test = int(raw_input("Please enter a large integer to test primality: "))
            is_prime = Prime.probabilistic_primality_test(number_to_test)
            print "{} is {}".format(number_to_test, "prime" if is_prime else "composite")
        except ValueError as e:
            print "You didn't enter a valid number."

    second_answer = raw_input("Would you like to generate a large prime number? (Y/N) ")
    if second_answer.lower() == "y":
        try:
            upper_bound = int(raw_input("Please enter the upper bound for the prime number: "))
            print "{} is a really large prime number!".format(Prime.generate_large_prime(upper_bound))
        except ValueError as e:
            print "You didn't enter a valid number."
    print "Exiting."

if __name__ == "__main__":
    main()
