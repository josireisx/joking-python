n = float(input())

if 0 <= n and n <= 25:
   print('Intervalo [0,25]')
else:
   if 25 < n and n <=50:
     print('Intervalo (25,50]')
   else:
     if 50 < n and n <=75:
       print('Intervalo (50,75]')
     else:
       if 75 < n and n <=100:
         print('Intervalo de (75,100]')
       else:
         print('Fora do intervalo')
  