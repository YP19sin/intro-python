m= int(input('Veuillez entrer le coefficient directeur de votre fonction affine:  a='))
p= int(input('Veuillez entrer lordonnée à lorigine de votre fonction affine:  b=' ))
x= (0,10)
print('Les résultats de la fonction affine pour x=[0;9[ dans f=ax+b sont:')
for x in range (0,10):
  f=m*x+p
  print (f)
