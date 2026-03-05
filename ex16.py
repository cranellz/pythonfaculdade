horas = float(input("horas trabalhadas: "))
valor_hora = float(input("valor por hora: "))
percentual_desconto = float(input("percentual de desconto: "))
dependentes = float(input("Número de dependentes:"))

salario_bruto = horas * valor_hora
desconto = salario_bruto * (percentual_desconto / 100)
salario_liquido = salario_bruto - desconto + (dependentes * 100)
print(f"salario bruto: {salario_bruto:}")
print(f"desconto: {desconto:}")
print(f"bonus dependentes: {dependentes * 100}")
print(f"salário a receber:  {salario_liquido}")