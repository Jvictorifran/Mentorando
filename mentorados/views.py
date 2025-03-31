from django.shortcuts import render
from django.http import HttpResponse
from .models import Mentorados

def mentorados(request):
  if request.method == 'GET':
    return render (request, 'mentorados.html', {'estagios': Mentorados.estagio_choices})