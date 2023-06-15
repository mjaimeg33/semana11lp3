from django.shortcuts import render, HttpResponse, redirect

layout = """
<h1> Proyecto Web (LP3) | Jaime Matheus </h1>
<hr/>
<ul>
<li>
<a href="/inicio"> Inicio</a>
</li>
<li>
<a href="/saludo"> Mensaje de Saludo</a>
</li>
<li>
<a href="/rango"> Mostrar Números [a,b]</a>
    </li>
    <li>
<a href="/rango2/10/15"> Mostrar Números [10,15]</a>
    </li>
    <li>
</ul>
<hr/>
"""
def index(request):
    estudiantes = ['Isabella Caballero',
    'Alejandro Hermitaño',
    'Joan Palomino',
    'Pierre Bernaola']
    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje': 'Proyecto Web con Django',
        'estudiantes': estudiantes
})


def saludo(request):
    return render(request,'saludo.html',{
        'titulo':'Saludo',
        'autor_saludo':'Jaime Matheus'
    })

def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request,'rango.html',{
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
})

def rango2(request,a,b):
    resultado = f"""
    <h2> Números de [{a},{b}] </h2>
    Resultado: <br>
    <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
        resultado += "</ul"
    return HttpResponse(layout + resultado)

def rango2(request,a=0,b=100):
    resultado = f"""
    <h2> Números de [{a},{b}] </h2>
    Resultado: <br>
    <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
        resultado += "</ul"
    return HttpResponse(layout + resultado)