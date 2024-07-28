from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola_mundo(response):
    return HttpResponse('''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Texto Mundo</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Altura completa de la ventana */
            margin: 0; /* Elimina el margen por defecto */
            background-color: blue; /* Fondo claro (opcional) */
        }
        h1 {
            color: yellow ; /* Color del texto */
            font-family: 'Pacifico', cursive; 
            font-size: 200px;
            opacity: 0; /* Comienza invisible */
            animation: fadeIn 1s forwards; /* Llama a la animación */
        }

        /* Definición de la animación */
        @keyframes fadeIn {
            from {
                
                opacity: -3; /* Comienza completamente transparente */
                transform: translateY(-200px); /* Desplazamiento hacia arriba */
            }
            to {
                
                opacity: 1; /* Termina completamente visible */
                transform: translateY(0); /* Regresa a su posición original */
            }
        }
    </style>
</head>
<body>
    <div>
        <h1>Hola Mima : )</h1>
    </div>
</body>
</html>
''')
    
def Home(response):
    
    plantilla = open('hola/templates/home.html')
    plt=Template(plantilla.read())
    plantilla.close()
    ctc= Context()
    documento = plt.render(ctc)
    return  HttpResponse(documento)

def ofertas(response):
    plantilla = open('hola/templates/ofertas.html')
    plt=Template(plantilla.read())
    plantilla.close()
    ctc= Context()
    documento = plt.render(ctc)
    return  HttpResponse(documento)   
    
def a_nombre(response):
    plantilla = open('hola/templates/a_nombre.html')
    plt=Template(plantilla.read())
    plantilla.close()
    ctc= Context()
    documento = plt.render(ctc)
    return  HttpResponse(documento)   

def exito(request):
    return render(request, 'exito.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')
