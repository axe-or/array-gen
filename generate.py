ARR_TYPE = 'array'

bin_templ = '''
template<typename T, int N> constexpr $ARR<$OUT, N> operator$OP($ARR<T,N> a, $ARR<T,N> b){
\t$ARR<$OUT, N> r{};
\tfor(int i = 0; i < N; i += 1){
\t\tr[i] = a[i] $OP b[i];
\t}
\treturn r;
}
'''
bin_scalar_templ_a = '''
template<typename T, int N> constexpr $ARR<$OUT, N> operator$OP($ARR<T,N> a, T s){
\t$ARR<$OUT, N> r{};
\tfor(int i = 0; i < N; i += 1){
\t\tr[i] = a[i] $OP s;
\t}
\treturn r;
}
'''
bin_scalar_templ_b = '''
template<typename T, int N> constexpr $ARR<$OUT, N> operator$OP(T s, $ARR<T,N> a){
\t$ARR<$OUT, N> r{};
\tfor(int i = 0; i < N; i += 1){
\t\tr[i] = s $OP a[i];
\t}
\treturn r;
}
'''
unary_templ = '''
template<typename T, int N> constexpr $ARR<$OUT, N> operator$OP($ARR<T,N> a){
\t$ARR<$OUT, N> r{};
\tfor(int i = 0; i < N; i += 1){
\t\tr[i] = $OP a[i];
\t}
\treturn r;
}
'''
def arith_bin(op):
    return '\n'.join([bin_templ, bin_scalar_templ_a, bin_scalar_templ_b]).replace('$OP', op).replace('$OUT', 'T')

def arith_unary(op):
    return unary_templ.replace('$OP', op).replace('$OUT', 'T')

def logic_bin(op):
    return bin_templ.replace('$OP', op).replace('$OUT', 'bool')

def logic_unary(op):
    return unary_templ.replace('$OP', op).replace('$OUT', 'bool')

ab = [ arith_bin(op) for op in ['+', '-', '*', '/', '%',  '&', '|', '^'] ]
au = [ arith_unary(op) for op in ['+', '-', '~'] ]
lb = [ logic_bin(op) for op in ['&&', '||', '==', '!=', '>=', '<=', '>', '<'] ]
lu = [ logic_unary(op) for op in ['!'] ]

decls = ab + au + lb + lu

decls.insert(0, '''template<typename T, int N>
struct $ARR {
\tT data[N];
\tconstexpr T& operator[](int i){ return data[i]; }
\tconstexpr T const& operator[](int i) const { return data[i]; }
};\n
''')
decls = '\n'.join(decls).replace('$ARR', ARR_TYPE).replace('\n\n', '\n').replace('\n\n', '\n')
print(decls)
