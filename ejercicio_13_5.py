#!/usr/bin/python3

fich = open("/etc/passwd","r")
usuarios = fich.readlines()
dicc = {}

for usuario in usuarios:
    lista = usuario.split(':')
    login = lista[0]
    shell = lista[-1][:-1]
    dicc[login] = shell
try:
  print ("El usuario root es: " + dicc['root'])
  print ("El usuario imaginario es: " + dicc['imaginario'])

except KeyError:
  print("Key no encontrada")

fich.close()
