dias = int(input())
horas = int(input())
minutos = int(input())
segundos = int(input())
milisegundos = 0

horas += dias*24
minutos += horas*60
segundos += minutos*60
milisegundos += segundos*1000

print(milisegundos)