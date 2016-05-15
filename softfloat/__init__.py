import struct


def bits32tofloat(bits):
    raw_data = struct.pack("I", bits)
    conv_data = struct.unpack("f", raw_data)
    return conv_data[0]


def float2bits32(flt):
    raw_data = struct.pack("f", flt)
    conv_data = struct.unpack("I", raw_data)
    return conv_data[0]


def bits64tofloat(bits):
    raw_data = struct.pack("L", bits)
    conv_data = struct.unpack("<d", raw_data)
    return conv_data[0]


def float2bits64(flt):
    raw_data = struct.pack("d", flt)
    conv_data = struct.unpack("q", raw_data)
    return conv_data[0]


def bits64tohex(bits):
    raw_data = struct.pack('<d', bits)
    conv_data = struct.unpack('<Q', raw_data)
    return conv_data[0]