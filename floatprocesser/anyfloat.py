"""Conversion module between floating point representations.
This module offers a class "anyfloat" which is a named tuple with 3 fields: sign, exponent, significand,
but without restrictions on the size of the exponent and the significand.
An instance of anyfloat represents the real value
    val = +/- 0.significand x 2^(1 + exponent)
    * The sign field has value 1 for a negative value and 0 otherwise.
    * The exponent is the logarithm of |val| in base 2 (except for special values)
    * The significand is >= 0 except for special values:
        + significand = -1 is used to represent +/- infinity. In this case, exponent = 0
        + significand = -2 is used to represent NaN value. In this case, exponent = 0

Methods are provided to convert ieee numbers or python floats to/from anyfloat:
    AnyFloat.to_ieee(size) converts to an integer which binary representation is the ieee754
        representation of this anyfloat with given size = (w, p).

    AnyFloat.from_ieee(n, size) creates an anyfloat from an integer containing the ieee754
        representation of a value.

    AnyFloat.__float__() converts to a python float.

    AnyFloat.from_float(val) creates an anyfloat from a python floating point number.
"""

from collections import namedtuple
import struct

DEFAULT_SIZE = (11, 52)


def trunc_round(n, k):
    rshift = n.bit_length() - 1 - k
    if rshift >= 0:
        n >>= (rshift)
    else:
        n <<= (-rshift)
    return (n + 1) >> 1


def more_bin_digits(n, k):
    return bool(n >> k)


def unset_high_bit(n):
    assert n > 0
    return n ^ (1 << (n.bit_length() - 1))


def fbin(n, nbits):
    assert (0 <= n)
    assert not (n >> nbits)
    return "{val:0>{width}}".format(val=bin(n)[2:], width=nbits)


_anyfloat = namedtuple("floatprocesser", "sign exponent significand")


class AnyFloat(_anyfloat):
    __slots__ = ()
    _b32 = 1 << 32
    _b64 = 1 << 64

    def __new__(cls, sign, exponent, significand):
        assert sign in (0, 1)
        if significand:
            significand = significand // (significand & -significand)
        return _anyfloat.__new__(cls, sign, exponent, significand)

    @staticmethod
    def _encode(log2, mantissa, a, b):
        A = ~(~0 << a)
        AA = A >> 1
        if mantissa <= 0:
            return ((A, 0) if (mantissa == -1) else (A, 1 << (b - 1))) if mantissa else (0, 0)
        elif log2 <= - AA:
            nbits = b + log2 + AA
            rounded = trunc_round(mantissa, nbits) if (nbits >= 0) else 0
            return (1, 0) if more_bin_digits(rounded, b) else (0, rounded)
        elif log2 <= AA:
            rounded = trunc_round(mantissa, b + 1)
            return (((log2 + 1 + AA, 0) if (log2 < AA) else (A, 0))
                    if more_bin_digits(rounded, b + 1) else (log2 + AA, unset_high_bit(rounded)))
        else:
            return (A, 0)

    @staticmethod
    def _decode(exponent, significand, a, b):
        A = ~(~0 << a)
        AA = A >> 1
        assert 0 <= exponent <= A
        assert 0 <= significand < (1 << b)
        if exponent == A:
            return (0, -2 if significand else -1)
        elif exponent:  # normal case
            return (exponent - AA, significand | (1 << b))
        else:  # subnormal case
            if significand:
                return (significand.bit_length() - AA - b, significand)
            else:
                return (0, 0)

    def __float__(self):
        return self.int64_to_float(self.to_ieee())

    @classmethod
    def from_float(cls, x):
        """Create an floatprocesser instance from a python float (64 bits double precision number)."""
        return cls.from_ieee(cls.float_to_int64(x))

    @classmethod
    def from_ieee(cls, n, size=DEFAULT_SIZE):
        """Create an floatprocesser from an ieee754 integer.

        Create an floatprocesser from an integer which binary representation is the ieee754
        format of a floating point number. The argument 'size' is a tuple (w, p)
        containing the width of the exponent part and the significand part in
        this ieee754 format."""
        w, p = size
        r = n >> p
        significand = (r << p) ^ n
        sign = int(r >> w)
        if not sign in (0, 1):
            raise ValueError(("Integer value out of range for ieee754 format", n, size))
        exponent = (sign << w) ^ r
        e, s = cls._decode(exponent, significand, w, p)
        if e == -2:
            sign = 0
        return cls(sign, e, s)

    def ieee_parts(self, size=DEFAULT_SIZE):
        w, p = size
        e, s = self._encode(self.exponent, self.significand, w, p)
        sign = 0 if (e + 1) >> w else self.sign
        return sign, e, s

    def to_ieee(self, size=DEFAULT_SIZE):
        """Convert to an ieee754 integer.

        Convert self to an integer which binary representation is the ieee754 format corresponding
        to the 'size' argument (read the documentation of from_ieee() for the meaning of the size
        argument.
        """
        sign, e, s = self.ieee_parts(size)
        return (((sign << size[0]) | e) << size[1]) | s

    @classmethod
    def int64_to_float(cls, n):
        """Convert a 64 bits integer to a python float.

        This class method converts an integer representing a 64 bits floating point
        number in the ieee754 double precision format to this floating point number."""

        if not (0 <= n < cls._b64):
            raise ValueError(("Integer value out of range for 64 bits ieee754 format", n))
        u, v = divmod(n, cls._b32)
        return struct.unpack(">d", struct.pack(">LL", u, v))[0]

    @classmethod
    def float_to_int64(cls, x):
        """Convert a python float to a 64 bits integer.

        This class method converts a float to an integer representing this
        float in the 64 bits ieee754 double precision format."""

        u, v = struct.unpack(">LL", struct.pack(">d", x))
        return (u << 32) | v

    def bin(self, size=DEFAULT_SIZE, sep=' '):
        """Return a binary representation of self.

        The returned string contains only the characters '0' and '1' and shows the
        ieee754 representation of the real number corresponding to self whith the given
        size = (w, p).
        """
        if sep:
            sign, e, s = self.ieee_parts(size)
            return sep.join((fbin(sign, 1), fbin(e, size[0]), fbin(s, size[1])))
        else:
            return fbin(self.to_ieee(size), sum(size) + 1)


def main():
    from math import exp
    val = exp(2)
    print("exp(2) =", val)
    af = AnyFloat.from_float(val)
    print(af)
    print(af.bin(), "(64 bits float)")
    print(" " * 2, af.bin(size=(8, 23)), "(32 bits)")
    print(" " * 7, af.bin(size=(3, 4)), "(8 bits)")
    print("conversion to float works:", float(af) == val)

    n = int("00000010100000000000000000010000", 2)  # a single precision ieee number.
    af = AnyFloat.from_ieee(n, (8, 23))
    print(float(af))


if __name__ == "__main__":
    main()

""" my output -->
exp(2) = 7.38905609893
floatprocesser(sign=0, exponent=2, significand=4159668786720471)
0 10000000001 1101100011100110010010111000110101001101110110101110 (64 bits float)
   0 10000001 11011000111001100100110 (32 bits)
        0 101 1110 (8 bits)
conversion to float works: True
Notice that during the conversion to shorter formats, for example 64 bits to 32 bits,
the significand is not only truncated to 23 bits, it is also rounded to the nearest value
depending on the value of the next bit.
"""
