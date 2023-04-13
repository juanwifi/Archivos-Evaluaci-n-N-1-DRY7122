import json

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

info = {"nombre": nombre, "apellido": apellido}

json_info = json.dumps(info)

print(json_info)
