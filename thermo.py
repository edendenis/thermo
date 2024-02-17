# PRANDIIANO - Museu da Matemática

# Curso de Computação em Python

# Data de Criação: 15 / 03 / 2018
# Data da última modificação: 15 / 03 / 2018

# REFERÊNCIA(S): -------------------------------------------------------------------------------------------------------

# [1] -.

# FUNÇÃO DO APLICATIVO: ------------------------------------------------------------------------------------------------
# Função: calcular a conversão entre as escalas de temperaturas mais utilizadas

# VARIÁVEI(S): ---------------------------------------------------------------------------------------------------------

escala_de = input("Digite a escala a ser convertida (Celsius/Fahrenheite/Kelvin): ")
escala_de = escala_de.upper() # Função para deixar todos os caracteres em MAIÚSCULO, pois, a linguagem é case sensitive.
valor_da_temperatura = input("Digite o 'Valor da Temperatura' = ")
escala_para = input("Digite a escala na qual o valor deve ser convertido (Celsius/Fahrenheite/Kelvin): ")
escala_para = escala_de.upper()

# CÁLCULO(S): ----------------------------------------------------------------------------------------------------------

if escala_de == "":
    quit()

if valor_da_temperatura == "":
    quit()

if valor_da_temperatura.isnumeric() == True:
    valor_da_temperatura = float(valor_da_temperatura)
else:
    print("Especifique apenas números para o valor da 'Temperatura' ")
    quit()

# EXERCÍCIO: Colocar verificação para os menores valores das escalas, por exemplo, NÃO existe temperatira Kelvin
# negativa e, qual seriam as temperaturas Celsius e Fahrenheit equivalente a 0 K?

if escala_para == "":
    quit()

if escala_de == "KELVIN" and escala_para == "CELSIUS":
    Tk = valor_da_temperatura
    Tc = Tk - 273.15
    print("Temperatura em Celsius (Tc) = ", Tc, " °C")
elif escala_de == "CELSIUS" and escala_para == "KELVIN":
    Tc = valor_da_temperatura
    Tk = Tc + 273.15
    print("Temperatura em Kelvin (Tk) = ", Tk , " K")
elif escala_de == "FAHRENHEIT" and escala_para == "CELSIUS":
    Tf = valor_da_temperatura
    Tc = (5 / 9) * Tf - 160 / 9
    print("Temperatura em Celsius (Tc) = ", Tc , " °C")
elif escala_de == "CELSIUS" and escala_para == "FAHRENHEIT":
    Tc = valor_da_temperatura
    Tf = (9 / 5) * Tc + 32
    print("Temperatura em Fahrenheit (Tc) = " , Tf , " °F")
elif escala_de == "KELVIN" and escala_para == "FAHRENHEIT":
    Tk = valor_da_temperatura
    Tc = Tk - 273.15
    Tf = (9 / 5) * Tc + 32
    print("Temperatura em Fahrenheit (Tc) = " , Tf , " °F")
elif escala_de == "FAHRENHEIT" and escala_para == "KELVIN":
    Tf = valor_da_temperatura
    Tc = (5 / 9) * Tf - 160 / 9
    Tk = Tc + 273.15
    print("Temperatura em Kelvin (Tk) = " , Tk , " K")
else:
    print("")

# EXERCÍCIO: Se algum número dor negativo, o 'float' NÃO irá funcionar por conta do primeiro caracter ser o símbolo  de
# negativo '-'. Como resolver isto?
 
# RESULTADO(S): --------------------------------------------------------------------------------------------------------

# Os resultados são exibidos dentro dos if's.