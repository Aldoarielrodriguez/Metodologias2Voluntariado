class Decodificador:
	def __init__(self,string):
		self.__st=string
	
	def analizar(self):
		modulos=open(self.__st,'r').readlines()
		for x in modulos:
			x=x[:x.find('\n')] 
			if x!='fin':
				ran= x.find('(')
				if x == 'inicio programa()':		#si el programa se inicio correctamente , inicio
					#iniciar()
					print 'iniciando programa'						
					
				elif x[:ran] == 'avanzar' :		#si el usuario quiere que el colectivo avance, 
					av=x[ran+1:x.find(')')]
					if av>0 and av<20:			#avanzar en un rango menor a 20 cuadras
						#Colectivo.avanzar(d)
						print 'el colectivo avanza:',av,'espacios'	
				
				elif x[:ran] == 'girar':
					g=x[ran+1:x.find(')')]
					if g == 'izquierda':
						#Colectivo.girar('izquierda')
						print 'el colectivo gira a la izquierda'
					elif g == 'derecha':
						#Colectivo.girar('derecha')#tres veces izquierda	
						print 'el colectivo gira a la derecha'
				else:
					print 'debes iniciar el programa'
		print 'programa terminado'
		
			
dec= Decodificador('texto.txt')
dec.analizar()



