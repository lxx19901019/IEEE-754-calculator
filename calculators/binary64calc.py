import os
import cffi
from softfloat import float2bits32, float2bits64
from calculators import binarycalc

c_src_dir = 'softfloat-c'


# -----------------------------------------------------------------------
# cffi import lib
# -----------------------------------------------------------------------
def get_c_sources(path):
    files = [x for x in os.listdir(path) if os.path.splitext(x)[-1] == '.c']
    files = [os.path.join(path, x) for x in files]
    return files


def validate_compilation(path):
    source_files = [x for x in os.listdir(path) if os.path.splitext(x)[-1] == '.c']
    source_files = [os.path.join(path, x) for x in source_files]
    out_files = [x for x in os.listdir(path) if os.path.splitext(x)[-1] == '.o']
    out_files = [os.path.join(path, x) for x in out_files]
    if len(source_files) != len(out_files):
        ffi.compile()


ffi = cffi.FFI()
ffi.set_source('softfloat._api', '''
    #include "platform.h"
    #include "internals.h"
    #include "specialize.h"
    #include "softfloat.h"
  ''',
               include_dirs=[c_src_dir],
               sources=get_c_sources(c_src_dir),
               )
ffi.cdef('''
typedef uint32_t float32_t;
    typedef uint64_t float64_t;
    typedef struct { uint64_t v; uint16_t x; } floatx80_t;
    typedef struct { uint64_t v[ 2 ]; } float128_t;

    int_fast8_t softfloat_exceptionFlags;
    uint_fast8_t softfloat_roundingMode;
    float32_t f32_add( float32_t a, float32_t b );
    float32_t f32_mul( float32_t a, float32_t b );
    float32_t f32_div( float32_t a, float32_t b );
    float64_t f64_add( float64_t a, float64_t b );
    float32_t f64_mul( float64_t a, float64_t b );
    float32_t f64_div( float64_t a, float64_t b );
''')

validate_compilation(c_src_dir)

from softfloat._api import ffi, lib


class Binary64Calc(binarycalc.BinaryCalc):
    def _float_calculator(self):
        lhs = float2bits64(self.first_num)
        rhs = float2bits64(self.second_num)
        res = self.__execute_operation(lhs, rhs)
        return res

    def _hex_calculator(self):
        lhs = int(self.first_num, 16)
        rhs = int(self.second_num, 16)
        res = self.__execute_operation(lhs, rhs)
        return res

    def __execute_operation(self, lhs, rhs):
        lib.softfloat_roundingMode = self.round_mode
        res = 0
        if self.operation == '+':
            res = self.__sum(lhs, rhs)
        elif self.operation == '*':
            res = self.__multiply(lhs, rhs)
        elif self.operation == '/':
            res = self.__div(lhs, rhs)
        self.exception_code = lib.softfloat_exceptionFlags
        return res

    def __sum(self, lhs, rhs):
        res = lib.f64_add(lhs, rhs)
        return res

    def __multiply(self, lhs, rhs):
        res = lib.f64_mul(lhs, rhs)
        return res

    def __div(self, lhs, rhs):
        res = lib.f64_div(lhs, rhs)
        return res
