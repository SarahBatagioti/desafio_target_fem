# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de 
# representação que cada estado teve dentro do valor total mensal da distribuidora.

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

td = sp + rj + mg + es + outros

p_sp = sp / td * 100 
p_rj = rj / td * 100 
p_mg = mg / td * 100 
p_es = es / td * 100 
p_outros = (outros / td) * 100 

print(f'SP: {p_sp:.0f}%, RJ: {p_rj:.0f}%, MG: {p_mg:.0f}%, ES: {p_es:.0f}% e outros: {p_outros:.0f}%')
