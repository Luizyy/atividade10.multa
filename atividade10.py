# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
km = float(input("Insira a velocidade em Km/h percorrida:"))
multa= (km-60)*7
if km > 60:
    print(f"Voce recebera uma multa de:{multa} reais")
else:
    print('voce nao recebera multa') 
 
