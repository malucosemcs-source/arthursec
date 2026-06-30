s=float(input('qual e a media salarial:'))
d=float(input('quatos porcento aumentou no salario:'))
r=s+(s*d/100)
print('se o seu salario era de R${:.2f} com o aumento de %{} no final vc fica com R${:.2f} por mes'.format(s,d,r))