from abc import ABC, abstractclassmethod

class Persona:
    def __init__(self, nombre, edad, dni):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    # Setter para el atributo nombre
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise TypeError("El nombre debe ser una cadena de caracteres.")
    
    # Getter para el atributo nombre
    def get_nombre(self):
        return self._nombre
    
    # Setter para el atributo edad
    def set_edad(self, edad):
        if isinstance(edad, int) and edad > 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un número entero mayor que cero.")
    
    # Getter para el atributo edad
    def get_edad(self):
        return self._edad
    
    # Setter para el atributo dni
    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 8:
            self._dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de 8 caracteres.")
    
    # Getter para el atributo dni
    def get_dni(self):
        return self._dni
    
    def mostrar(self) -> str:
        return f'{self._nombre} {self._edad} {self._dni}'
    
    def es_mayor_de_edad(self):
        if self._edad < 18:
            return False
        else:
            return True
   
class Cuenta:
    def __init__(self,titular, cantidad=0.0):
        self._titular = titular
        self._cantidad = cantidad
    
    # Getter para el atributo titular
    def get_titular(self):
        return self._titular
    
    # Getter y setter para el atributo cantidad
    def get_cantidad(self):
        return self._cantidad
    
    def set_ingresar(self, cantidad):
        self._cantidad = cantidad

    def set_retirar(self, cantidad):
        self._cantidad = cantidad
    
    def mostrar(self) -> str:
        return f' \n Nombre: {persona._nombre} \n Edad: {persona._edad} \n DNI: {persona._dni} \n Saldo cuenta: $ {self._cantidad}'
    
    def es_titular_valido(self):
        if persona._edad > 18 and persona._edad < 25:
            return True
        else:
            return False

class CuentaJoven():
    def __init__(self,titular,cantidad,bonificacion="10%"):
        self._titular = titular
        self._cantidad = cantidad
        self._bonificacion = bonificacion

    def get_titular(self):
        return self._titular
    
    def set_bonificacion(self, bonificacion):            
        self._bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self._bonificacion
    
    def get_cantidad(self):
        return self._cantidad
    
    def set_ingresar(self, cantidad):
        self._cantidad = cantidad

    def set_retirar(self, cantidad):
        self._cantidad = cantidad

    def mostrar(self) -> str:
        return f' \n Cuenta Joven \n Nombre: {persona._nombre} \n Edad: {persona._edad} \n DNI: {persona._dni} \n Saldo cuenta: $ {self._cantidad} \n Bonificacion: {self._bonificacion}'

def crearCuenta():
    while True:
        cuenta = input("Desea crear una cuenta? S/N :")
        if cuenta == "S" or cuenta == "N":
            return cuenta
        else:
            print("No ingreso un opcion valida")

if crearCuenta() == 'S':
    persona = Persona('','','')
    persona.set_nombre(input('Ingrese su nombre: '))
    persona.set_edad(int(input('Ingrese su edad: ')))
    persona.set_dni(input('Ingrese su dni: '))    

    cuenta = Cuenta(persona)
    
    if cuenta.es_titular_valido() == True:
        cuentajoven = CuentaJoven(cuenta._titular.get_nombre(),cuenta._cantidad)      
        print()
        agregarDinero = float(input("Ingresar dinero, si pone 0 no se agregara: $ "))
        while agregarDinero != 0.0:
            cuentajoven.set_ingresar(cuentajoven.get_cantidad() + agregarDinero)
            agregarDinero = float(input("Ingresar dinero, si pone 0 no se agregara: $ "))

        print()
        retirarDinero = float(input("Retirar dinero, si pone 0 no se quitara: $ "))
        while retirarDinero != 0.0:
            cuentajoven.set_ingresar(cuentajoven.get_cantidad() - retirarDinero)
            retirarDinero = float(input("Retirar dinero, si pone 0 no se quitara: $ "))
        
        print(cuentajoven.mostrar())  
    else:

        print()
        agregarDinero = float(input("Ingresar dinero, si pone 0 no se agregara: $ "))
        while agregarDinero != 0.0:
            cuenta.set_ingresar(cuenta.get_cantidad() + agregarDinero)
            agregarDinero = float(input("Ingresar dinero, si pone 0 no se agregara: $ "))

        print()
        retirarDinero = float(input("Retirar dinero, si pone 0 no se quitara: $ "))
        while retirarDinero != 0.0:
            cuenta.set_ingresar(cuenta.get_cantidad() - retirarDinero)
            retirarDinero = float(input("Retirar dinero, si pone 0 no se quitara: $ "))
        
        print(cuenta.mostrar())