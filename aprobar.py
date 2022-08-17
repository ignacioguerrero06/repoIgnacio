from cmath import pi
import sys

nota=float(sys.argv[1])
nota2=float(sys.argv[2])


if nota> 7 and nota2>7:
        print("Promocionado")
elif nota>4 and nota2>4:
        print("Aprobado, debe rendir final")
elif nota<4 and nota2<4:
        print("Desaporbado ambos parciales, debe recursar")
elif nota2<4:
        print("Desaporbado, debe recuperar el segundo parcial")
elif nota<4:
        print("Desaporbado, debe recuperar el primer parcial")  
   
