from re import compile as re_compile

binary_template = '''
template<typename T, isize N>
constexpr auto operator$Op(Array<T, N> const& a, Array<T, N> const& b){
    Array<$Type, N> c;
    for(isize i = 0; i < N; i++){
        c[i] = a $Op b;
    }
    return c;
}
'''
unary_template = '''
template<typename T, isize N>
constexpr auto operator$Op(Array<T, N> const& a){
    Array<$Type, N> c;
    for(isize i = 0; i < N; i++){
        c[i] = $Op a;
    }
    return c;
}
'''

whitespace = re_compile(r'\s+')

def binary(t, op):
    return whitespace.sub(' ', binary_template.replace('$Type', t).replace('$Op', op))

def unary(t, op):
    return whitespace.sub(' ', unary_template.replace('$Type', t).replace('$Op', op))

bin_arith_ops = [
    '+', '-', '*', '/', '%',
    '&', '|', '^', '<<', '>>',
]

bin_logic_ops = [
    '&&', '||', '==', '!=',
    '>', '>=', '<', '<=',
]

un_arith_ops = [
    '+', '-', '~',
]

un_logic_ops = [
    
    '!',
]

lines = []
lines += [binary('T', op)    for op in bin_arith_ops]
lines += [binary('bool', op) for op in bin_logic_ops]
lines += [unary('T', op)    for op in un_arith_ops]
lines += [unary('bool', op) for op in un_logic_ops]

print('\n'.join(lines))
