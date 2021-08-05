from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    return render(request, 'index.html')

def calcular(request):
    opc = request.POST['opcion']

    if opc == "granja":
        numini = 10
        numfin = 20

    if opc == "cueva":
        numini = 5
        numfin = 10

    if opc == "casa":        
        numini = 2
        numfin = 5

    if opc == "casino":
        numini = -50
        numfin = 50

    n = random.randint(numini, numfin)
    print(f"Opcion : {opc} - Oros : {n}")    

    if 'contador' in request.session:
        request.session['contador'] += n
    else:
        request.session['contador'] = 1

    if not ('logs' in request.session):
        request.session['logs'] = []
    
    if n >= 0:
        textolog = (f"Ganaste {n} Oros desde {opc} ({datetime.now()})")
        textocol = "text-success"
    else:
        textolog = (f"Ingresaste a {opc} y perdiste {n} Oros ... Ouch ... ({datetime.now()})")
        textocol = "text-danger"

    print(f"Log : {textolog} Color : {textocol}")

    request.session['logs'].append({
        'texto':textolog,
        'color':textocol
    })
    request.session.save()       

    return redirect ('/')    

def resetear(request):
    request.session['contador'] = 0
    request.session['logs'] = []
    return redirect("/")