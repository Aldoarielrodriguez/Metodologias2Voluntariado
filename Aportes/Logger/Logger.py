import time
import os
h=time.strftime("%H:%M:%S")
f=time.strftime("%d/%m/%y")

class Logerror:
	def __init__(self,c):
		self.__nombre=c
	def setname(self,n):
		os.rename(self.__nombre,n)
		self.__nombre=n
	def loggearerror(self,s):
		l=open(self.__nombre,"a+")
		l.write(s+". "+f+". "+h+"\n")
		l.close
	def getnombre(self):
		return self.__nombre
	def leerlog(self):
		l=open(self.__nombre,"r")
		return l.read()
		l.close

class Logcommon:
	def __init__(self,c):
		self.__nombre=c

	def setname(self,n):
		os.rename(self.__nombre,n)
		self.__nombre=n
	def loggearcommon(self,s):
		l=open(self.__nombre,"a+")
		l.write(s+". "+f+". "+h+"\n")
		l.close
	def getnombre(self):
		return self.__nombre
	def leerlog(self):
		l=open(self.__nombre,"r")
		return l.read()
		l.close

le= Logerror("Error.log")
le.loggearerror("Soy otra prueba")
le.loggearerror("asd")
le.loggearerror("asdasd3")
le.setname("error2.log")
le.loggearerror("Prueba rename")

lc= Logcommon("Common.log")

lc.loggearcommon("Soy prueba 1")
lc.loggearcommon("Soy num 2")
lc.loggearcommon("Yo soy el 3")		

lc.setname("common2.log")
lc.loggearcommon("Prueba rename")
lc.loggearcommon("Prueba rename 2")
