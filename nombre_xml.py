from xml.etree.ElementTree import Element, SubElement, tostring

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

info = Element("info")
nombre_element = SubElement(info, "nombre")
nombre_element.text = nombre
apellido_element = SubElement(info, "apellido")
apellido_element.text = apellido

xml_info = tostring(info)

print(xml_info.decode())
