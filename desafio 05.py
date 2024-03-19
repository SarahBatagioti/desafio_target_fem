# Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser 
# previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

p = 'palavra'

l = []
for let in p:
    l.append(let)

li = []
for i in range(len(l) - 1, -1, -1):
    li.append(l[i])

pi = ''
for let in li:
    pi += let

print(pi)
