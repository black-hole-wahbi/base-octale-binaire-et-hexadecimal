# base-octale-binaire-et-hexadecimal
application grafic de conversion de base
fonction de conversion de base :
'''
ch=str()
while n!=0:
   if n%b<=9 :
      ch=chr(n%b+48)+ch
   else:
      ch=chr(n%b+55)+ch
   n=n//b
return ch
'''
