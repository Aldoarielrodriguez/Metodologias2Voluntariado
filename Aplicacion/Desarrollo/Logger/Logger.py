import time

class Logger():
    class __Logger:
        def __init__(self):
        	print("Mierdaaa")
        	self.__logDir = "logs"
        	self.__errorLogName = "error.log"
        	self.__commonLogName = "common.log"
        	self.__consoleOut=False
        	         
         
        def __str__(self):
            return "Singleton Logger:[Directorio de logs: "+self.__logDir +"] [Log de error:"+ self.__errorLogName +"] [Log de ejecucion: "+self.__commonLogName+"]"
        def loggearError(self, obj):
        	self.__escribirEnFile(self.__errorLogName, str(obj))

        def loggearCommon(self, obj):
        	self.__escribirEnFile(self.__commonLogName, str(obj))
        def __escribirEnFile(self, logName, string):
        	f=open("./"+self.__logDir+"/"+logName,"a")        	
        	strfinal = "[Fecha: "+self.__getFecha()+"]-[Hora: "+self.__getHora()+"]"+string+"\n"
        	if(self.__consoleOut):
        	    print(strfinal)
        	f.write(strfinal)
        	f.close
        def __getFecha(self):
        	return time.strftime("%d/%m/%y")
        def __getHora(self):
        	return time.strftime("%H:%M:%S")

    instance = None
    def __new__(cls): 
        if not Logger.instance:
            Logger.instance = Logger.__Logger()
        return Logger.instance

