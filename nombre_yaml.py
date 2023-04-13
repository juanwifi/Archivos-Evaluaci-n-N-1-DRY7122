import yaml

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

info = {"nombre": nombre, "apellido": apellido}

yaml_info = yaml.dump(info)

print(yaml_info)
