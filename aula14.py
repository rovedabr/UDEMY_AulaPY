a = "A"
b = "B"
c = 1.1
formato = 'a={} b={} c={}'.format(a, b, c)
print(formato)

## MESMA SAÍDA PARA 

string = 'a={} b={} c={}'
string2 = 'c={:.2f}'
formato2 = string.format(a, b, c)
formato3 = string2.format(c)
print(formato2)
print(formato3)

# NOMEANDO AS SAÍDAS

string3 = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato4 = string3.format(nome1=a, nome2=b, nome3=c)
print(formato4)