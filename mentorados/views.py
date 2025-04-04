from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mentorados, Navigators
from django.contrib.messages import constants
from django.contrib import messages
from datetime import datetime

def mentorados(request):

  if not request.user.is_authenticated:
    return redirect('login')
  
  if request.method == 'GET':
    navigators = Navigators.objects.filter(user=request.user)
    mentorados = Mentorados.objects.filter(user=request.user)

    estagios_flat = []
    for i in Mentorados.estagio_choices:
      estagios_flat.append(i[1])
      
    qtd_estagios = []

    for i, j in Mentorados.estagio_choices:
      x = Mentorados.objects.filter(estagio=i).filter(user=request.user).count()
      qtd_estagios.append(x) 

    return render (request, 'mentorados.html', {'estagios': Mentorados.estagio_choices, 'navigators': navigators,'mentorados': mentorados, 'estagios_flat': estagios_flat, 'qtd_estagios': qtd_estagios})
  
  elif request.method == 'POST':
        
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        estagio = request.POST.get("estagio")
        navigator = request.POST.get('navigator')

        mentorado = Mentorados(
            nome=nome,
            foto=foto,
            estagio=estagio,
            navigator_id=navigator,
            user=request.user
        )

        mentorado.save()

        messages.add_message(request, constants.SUCCESS, 'Mentorado cadastrado com sucesso.')
        return redirect('mentorados')

def reunioes(request):
  if request.method == 'GET':
    return render(request, 'reunioes.html')

  elif request.method == 'POST':
    data = request.POST.get('data')
    data = datetime.strptime(data, "%Y-%m-%dT:%M")
    print(data)
    print(type(data))
    return HttpResponse(data)
