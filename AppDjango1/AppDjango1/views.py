from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

###

import random
from gestor.models import Articulos, Clientes
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .formularios import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


'''
para obtimizar el loader se puede escribir
de la siguiente forma la importacion...

from django.template.loader import get_template

en el codigo : doc_ext = get_template(nombre.html) 
'''

#clase de persona
class Persona(object):
        def __init__(self, nombre, apellido):
            self.nombre = nombre
            self.apellido = apellido


#cada funcion es una vista o por decirlo asi una pagina...
#hay que actualizar las urls

def index(request):
    doc_externo = loader.get_template("index.html")
    documento = doc_externo.render()
    return HttpResponse(documento)


def games(request):
    agno = datetime.datetime.now().year
    dia = datetime.datetime.now().day
    mes = datetime.datetime.now().month
    hora = datetime.datetime.now().strftime("%X")
    fecha = "%s/%s/%s a las %s" %(dia, mes, agno, hora)

    doc_externo = loader.get_template("games.html")
    documento = doc_externo.render(
        {
            "fecha":fecha
        }
    )
    return HttpResponse(documento)


def musica(request):
    agno = datetime.datetime.now().year
    dia = datetime.datetime.now().day
    mes = datetime.datetime.now().month
    hora = datetime.datetime.now().strftime("%X")
    fecha = "%s/%s/%s a las %s" %(dia, mes, agno, hora)

    doc_externo = loader.get_template("musica.html")
    documento = doc_externo.render(
        {
            "fecha":fecha
        }
    )
    return HttpResponse(documento)


def tecnologia(request):
    agno = datetime.datetime.now().year
    dia = datetime.datetime.now().day
    mes = datetime.datetime.now().month
    hora = datetime.datetime.now().strftime("%X")
    fecha = "%s/%s/%s a las %s" %(dia, mes, agno, hora)

    doc_externo = loader.get_template("tecnologia.html")
    documento = doc_externo.render(
        {
            "fecha":fecha
        }
    )
    return HttpResponse(documento)


#vista de saludar 

def saludar(request):
    return HttpResponse("hola Gamer Esta es la primera vista")

#vista de la fecha actual

def mostrar_fecha(request):
    fecha_actual=datetime.datetime.now()
    pagina ="""
<html>
<head>   
    <title>Mostrar fecha</title>
</head>
<body>
    <h2>Ejercicio Mostrar la fecha con Django </h2>

        <p>Usted ingreso o actualizo esta vista en la fecha:
    %s
        </p>
</body>
</html>
    """ %fecha_actual
    return HttpResponse(pagina)

#vista de Edad futura 

def calculo(request, fechaNacimiento, fechaFutura):
    año_actual = datetime.datetime.now().year
    edad_actual = año_actual - fechaNacimiento
    edad_futura = fechaFutura - fechaNacimiento
    documento = """
    <HTML>
        <head>
        <tittle>Estructura basica de un documento html</tittle>
        </head>
        <body>
            <h1>
            El individuo nacido en el año %s actualmente tien la edad de %s años 
            y en el año %s tendra %s años de edad
            </h1>
        <body>
    </HTML>
    """ % (fechaNacimiento, edad_actual, fechaFutura, edad_futura)
    return HttpResponse(documento)


#uso de templates 

def plantilla1(request):
    documento_externo = open("C:/Users/Familia/Desktop/Proyectos Django/Mi_primer_proyecto/Mi_primer_proyecto/templates/primer_plantilla.html")
    plantilla = Template(documento_externo.read())
    documento_externo.close()
    cont = Context()
    documento = plantilla.render(cont)
    return HttpResponse(documento)


#mostrar la vista de calculo con un plantilla

def calculo2(request, fechaNacimiento, fechaFutura):
    año_actual = datetime.now().year
    edad_actual = año_actual - fechaNacimiento
    edad_futura = fechaFutura - fechaNacimiento

    documento_externo = open("C:/Users/Familia/Desktop/Proyectos Django/Mi_primer_proyecto/Mi_primer_proyecto/templates/calculo_plantilla.html")
    plantilla = Template(documento_externo.read())
    documento_externo.close()
    cont = Context({
        "fecha_a":año_actual,
        "edad_a":edad_actual,
        "edad_f":edad_futura,
        "f_na":fechaNacimiento,
        "f_f":fechaFutura
    })
    documento = plantilla.render(cont)

    return HttpResponse(documento)


#vista de tareas enlistadas:

def tareasEnlistadas(request):

    Tareas = ["Aprender sobre internet","Aprender html","Aprender css", "Aprender python","Aprender Django","Construir mi propia web"]

    documento_externo = open("C:/Users/Familia/Desktop/Proyectos Django/Mi_primer_proyecto/Mi_primer_proyecto/templates/tareas_enlistadas.html")
    plantilla = Template(documento_externo.read())
    documento_externo.close()
    cont = Context({
        "listado":Tareas
    })
    documento = plantilla.render(cont)
    return HttpResponse(documento)

#cargar un documento con loader
def tareasEnlistadas2(request):

    Tareas = ["Aprender sobre internet","Aprender html","Aprender css", "Aprender python","Aprender Django","Construir mi propia web"]

    """documento_externo = open("C:/Users/Familia/Desktop/Proyectos Django/Mi_primer_proyecto/Mi_primer_proyecto/templates/tareas_enlistadas.html")
    plantilla = Template(documento_externo.read())
    documento_externo.close()"""

    doc = loader.get_template("tareas_enlistadas2.html")
    documento = doc.render({
        "listado":Tareas
    })
    return HttpResponse(documento)


#------------------------------------------------------------------------

#EJERCICIOS DE LA CLASE

#------------------------------------------------------------------------

    

def saludo_ej(request):

    name = "Juan "
    apellido = "Perez "
    p1 = Persona("Profesor Luis","Ch")
    haora = datetime.datetime.now()
    lista = ["Plantillas","Modelos","Formularios","Vistas","despliegue"]
    #doc_externo = open("C:/Users/Familia/Desktop/Proyecto Django/Mi_primer_proyecto/Mi_primer_proyecto/templates/saludar_ejercicio.html")
    #plantilla = Template(doc_externo.read())
    #doc_externo.close()
    '''
    contexto = Context(
        {
            "nombre":name,
            "apellido":apellido,
            "haora":haora,
            "temas":lista,
            "profesor":p1.nombre
        }
    )
    '''
    #documento = plantilla.render(contexto)
    #return HttpResponse(documento)

    return render(request, "saludar_ejercicio.html",{
            "nombre":name,
            "apellido":apellido,
            "haora":haora,
            "temas":lista,
            "profesor":p1.nombre
        })

'''

DE ESTA FORMA, SE UTILIZA UN SHORTCUT Y REDUZE EL CODIGO

from django.shortcuts import render

def view():
    //code

    return render(request,"nombre_plantilla",{Contexto})

'''

###


def formulario(request):
    return render(request, "formulario.html")

def home(request):
    return render(request, "home.html")

def respuesta(request):
    agno=datetime.datetime.now().year
    mes=datetime.datetime.now().month
    dia=datetime.datetime.now().day
    hora = datetime.datetime.now().strftime("%X")
    fecha = "%s/%s/%s a las %s" %(dia, mes, agno, hora)
    videos = {
        "menores":["https://www.youtube.com/embed/BIBHU-73YoQ","https://www.youtube.com/embed/mB267cU64bo","https://www.youtube.com/embed/Ggau_mRMTK4","https://www.youtube.com/embed/6Z4jj3Pcw3I"],
        "jovenes":["https://www.youtube.com/embed/aFwLmCNmnl4","https://www.youtube.com/embed/c6jlNDs9CWE","https://www.youtube.com/embed/8gKIM5aMJWs","https://www.youtube.com/embed/vgO2ou7JqCE","https://www.youtube.com/embed/fxavwHPJ36o","https://www.youtube.com/embed/z-99see1eKw"],
        "adultos":["https://www.youtube.com/embed/Bt8kAkX5uwM","https://www.youtube.com/embed/RK_pv8gqx6M","https://www.youtube.com/embed/KtXofyhNs3s","https://www.youtube.com/embed/kna0jm-vFSI","https://www.youtube.com/embed/1w8TLOuqUDc"]
    }
    video_n=random.choice(videos["menores"]);
    video_j=random.choice(videos["jovenes"]);
    video_a=random.choice(videos["adultos"]);
    agno_nacimiento =int(request.GET["nacimiento"].split('-')[0])
    mes_nacimiento =int(request.GET["nacimiento"].split('-')[1])
    dia_nacimiento =int(request.GET["nacimiento"].split('-')[2])
    edad =agno - agno_nacimiento
    if mes_nacimiento > mes:
        edad -= 1
    elif mes == mes_nacimiento:
        if dia < dia_nacimiento:
            edad -= 1
    nombre = request.GET["nombre"]
    genero = request.GET["genero"]
    return render(request, "respuesta.html",{
        "nombre":nombre,
        "genero":genero,
        "edad":edad,
        "fecha":fecha,
        "vid_j":video_j,
        "vid_n":video_n,
        "vid_a":video_a,
    })




def form_bus(request):
    arti =[]
    ar =Articulos.objects.all()
    for i in ar:
        arti.append(i.seccion)
    arti = sorted(list(set(arti)))
    return render(request,"./Form/form.html",{
        "articulos":arti,
    })

def resultado(request):
    '''
     busqueda = request.GET["producto"]
    resultado = Articulos.objects.filter(nombre=busqueda)
    mensaje = ""
    for i in resultado:
        mensaje ='%s Nombre: %s, Seccion: %s, Precio: %s \n\n' %(mensaje, i.nombre, i.seccion, i.precio) 
    '''
    if len(request.GET["producto"]) >=20:
        arti =[]
        ar =Articulos.objects.all()
        for i in ar:
            arti.append(i.seccion)
        arti = sorted(list(set(arti)))
        return render(request,"./Form/form.html",{
        "articulos":arti,
        "error":True,
    })

    encontrado = True
    if not(request.GET["producto"]=="") and not(request.GET["seccion"] == "todos"):
        nombre = request.GET["producto"]
        seccion = request.GET["seccion"]
        resultado = Articulos.objects.filter(nombre__icontains=nombre, seccion=seccion)

    elif not(request.GET["producto"]=="") and request.GET["seccion"]=="todos":
        nombre =request.GET["producto"]
        resultado = Articulos.objects.filter(nombre__icontains=nombre)

    elif request.GET["producto"]=="" and not(request.GET["seccion"]=="todos"):
        seccion = request.GET["seccion"]
        resultado = Articulos.objects.filter(seccion = seccion)

    elif request.GET["producto"]=="" and request.GET["seccion"]=="todos":
        resultado = Articulos.objects.all()

    if not resultado:
        encontrado = False

    return render(request,"./Form/respuesta.html",{
        "registro":resultado,
        "status":encontrado,
    })



def verificacion(nombre,direccion,telefono,email,password,pass2):
    dicError={}
    if len(nombre)>=40 or len(nombre)<3:
        dicError.setdefault("ErrorNombre","el nombre debe contener mas de 3 letras y menor de 40")

    if not len(telefono)==10:
        dicError.setdefault("ErrorTelefono","El numero del telefono debe tener 10 digitos")
    for i in telefono:
        if ord(i)<40 or ord(i)>58:
            if "ErrorTelefono" in dicError:
                dicError["ErrorTelefono"]="El campo solo puede tener numeros"
                break
            else:
                dicError.setdefault("ErrorTelefono","El numero telefonico no puede tener letras")

    if  len(direccion)<=5 or len(direccion)>=81 :
        dicError.setdefault("ErrorDireccion","La direccion debe ser mayor a 5 carateres y menor a 80 caracteres")

    if len(password)==0:
        dicError.setdefault("ErrorPassword","Debe ingresar una contraseña")
    if len(password)>=21 or len(password)<=7:
        if "ErrorPassword" in dicError:
            dicError["ErrorPassword"]="La contraseña debe tener almenos 8 caracteres y no ser mayor a 20 caracteres"
        else:
            dicError.setdefault("ErrorPassword","La contraseña debe tener almenos 8 caracteres y no ser mayor a 20 caracteres")
    if not(password==pass2):
        if "ErroPassword" in dicError:
            dicError["ErrorPassword"]="La contraseña no coincide con la verificacion de la misma "
        else:
            dicError.setdefault("ErrorPassword","La contraseña no coincide con la verificacion de la misma ")

    if len(email)==0:
        dicError.setdefault("ErrorEmail","DEbe ingresar un correo electronico")
    email_consulta=Clientes.objects.filter(email=email)
    if not len( email_consulta)==0:
        if "ErrorEmail" in dicError:
            dicError["ErrorEmail"]="El correo electronico no esta disponible"
        else:
            dicError.setdefault("ErrorEmail","El correo electronico no esta disponible")

    return dicError 


def validacion(request):
    nombre=request.POST["nombre"]
    direccion=request.POST["direccion"]
    email=request.POST["email"]
    telefono=request.POST["telefono"]
    password=request.POST["password"]
    pass2=request.POST["pass2"]
    status=verificacion(nombre,direccion,telefono,email,password,pass2)
    if len(list(status.keys()))>0:
        return render(request,"./Form/registro.html",{"status":status})
    else:
        Clientes.objects.create(nombre=nombre,direccion=direccion,email=email,telefono=telefono,password=password)
        return render(request,"./Form/RegistroExitoso.html",{"nombre":nombre})


def registro(request): return render(request,"./Form/registro.html",)


def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            messages.success(request,"usuario %s CREADO CORRECTAMENTE!!"%username)
    else:
        form=UserCreationForm(request.POST)
    contexto ={"form":form}
    return render(request,'./Form/register.html',contexto)        

def register2(request):
    if request.method=="POST":
        form1= UserRegisterForm(request.POST)
        if form1.is_valid():
            username=form1.cleaned_data['username']
            form1.save()
            messages.success(request,"usuario %s CREADO CORRECTAMENTE!!"%username)
    else:
        form1= UserRegisterForm(request.POST)
    contexto ={"form":form1}
    return render(request,'./Form/register2.html',contexto)       




def ingresar(request):
    if request.method=='POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get('username')
            contraseña=form.cleaned_data.get('password')
    else:
        form = AuthenticationForm()
    contexto = {'formulario':form}

    return render(request,'./Form/login.html',contexto)




