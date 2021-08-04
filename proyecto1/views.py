from django.http import HttpResponse
import datetime
from django.template import Context, Template
from django.template.loader import get_template
class Persona():

	def __init__(self,nombre,apellido):
		self.nombre=nombre
		self.apellido=apellido


def saludo(request):

	p1=Persona("Dardo","Gusmeroli")
	temas_del_curso=["plantillas","modelos","fomularios","vistas","despliegue"]
	#nombre="Juan"
	#apellido="Gusmeroli"
	ahora=datetime.datetime.now

	#doc_externo=open("C:/pildorasinf/Proyecto/proyecto1/proyecto1/plantillas/miplantilla.html")

	#plt=Template(doc_externo.read())
		
	
	#doc_externo.close()

	doc_externo=get_template('mi_plantilla.html')

	documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas_del_curso})

	#ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas_del_curso})

	#documento=plt.render(ctx)

	return HttpResponse(documento)

def despedida(request):

	return HttpResponse("Esta es la despedida, hasta luego")

def dame_fecha(request):
	fecha_actual=datetime.datetime.now()

	documento="""<html>
	<body>
	<h1>
	La fecha y hora actual es %s 
	</h1>
	</body>
	</htlm>""" %(fecha_actual)

	return HttpResponse(documento)

def calcula_edad(request,edad,agno):

	
	periodo=agno-2019
	edad_futura=edad+periodo

	documento="""<html>
	<body>
	<h1>
	En el año %s tendras %s años
	</h1>
	</body>
	</htlm>"""%(agno,edad_futura)

	return HttpResponse(documento)



