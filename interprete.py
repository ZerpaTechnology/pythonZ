#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import zu
def zlambda(**__f__):
	__p__=""
	__v__=""
	for elem in __f__:
		__p__+=elem+","
		
		__v__+='"""'+__f__[elem]+'""",'

	
	___mcodigo___=__f__["__codigo__"].replace("return","__return__=")
	___mcodigo2___=""
	for elem in ___mcodigo___.split("\n"):
		___mcodigo2___+=elem.lstrip()+"\n"
	___mcodigo___=___mcodigo2___
	___codigo___=__p__[:-1]+"="+__v__[:-1]+"\n"+___mcodigo___
	exec(___codigo___)
	return __return__
	
class PyZer:
	def __init__(self,idioma="español"):
		self.version="0.1"
		self.autor="jesús Zerpa"
		self.idioma=idioma
		self.codificado="# -*- coding: utf-8 -*-"
		self.expresiones={}
		self.variables={}
		self.codigo=[]
		
	def reexpresar(self,antigua,nueva):
		self.expresiones[antigua]=nueva
		
	def correr(self,codigo,archivo=False):
		if archivo==False:
			for expresion in self.expresiones:
				codigo=zu.remplazarFueraString(codigo,expresion,self.expresiones[expresion])
			self.codigo.append(codigo)
		else:
			f=open(codigo,"r")
			codigo=f.read()
			f.close()
			self.correr(codigo)

	def compilar(self):
		c=""
		for elem in self.codigo:
			c+=elem
		
		exec(zu.compilarLambda(c.split("\n")))

					
interprete=PyZer()	
interprete.reexpresar("para cada ","for ")
interprete.reexpresar("mientras que ","while ")
interprete.reexpresar("Falso","False")
interprete.reexpresar("Verdadero","True")
interprete.reexpresar("imprime ","print ")
interprete.reexpresar("de lo contrario:","else:")
interprete.reexpresar("si ","if ")
interprete.reexpresar("si no ","elif ")
interprete.reexpresar(" en "," in ")
interprete.reexpresar("clase ","class ")
interprete.reexpresar("importa ","import ")
interprete.reexpresar("desde ","from ")
interprete.reexpresar("como ","as ")
interprete.reexpresar("se incrementa","+=")
interprete.reexpresar(" es ","=")

interprete.reexpresar("es igual a","==")
interprete.reexpresar("es diferente de","!=")
interprete.reexpresar("es menor que",">")
interprete.reexpresar("es mayor que","<")
interprete.reexpresar("es menor o igual que",">=")
interprete.reexpresar("es mayor o igual que","<=")

interprete.reexpresar("es igual a","==")
interprete.reexpresar("sea diferente de","!=")
interprete.reexpresar("sea menor que",">")
interprete.reexpresar("sea mayor que","<")
interprete.reexpresar("sea menor o igual que",">=")
interprete.reexpresar("sea mayor o igual que","<=")

interprete.reexpresar(" con "," with ")
interprete.reexpresar("prueba","try")
interprete.reexpresar("excepto","except")
interprete.reexpresar("como ","as ")
interprete.reexpresar("ó","__o0_")
interprete.reexpresar("Ó","__O0_")
interprete.reexpresar("á","__a0_")
interprete.reexpresar("Á","__A0_")
interprete.reexpresar("é","__e0_")
interprete.reexpresar("É","__E0_")
interprete.reexpresar("í","__i0_")
interprete.reexpresar("Í","__I0_")
interprete.reexpresar("ú","__u0_")
interprete.reexpresar("Ú","__U0_")
interprete.reexpresar("ü","__u1_")
interprete.reexpresar("Ü","__U1_")
interprete.reexpresar(" entonces",":")


interprete.correr("codigo.py",True)
#interprete.correr("imprime 'oración'")
interprete.compilar()

