from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Pergunta
from django.urls import reverse


# Create your views here.

def listar(request):
    ultimas = Pergunta.objects.order_by('-data_pub')[:3]
    context = {'Perguntas_list': ultimas}
    return render(request, 'enquetes/index.html', context)
def detalhar(request, question_id):
    try:
        p = Pergunta.objects.get(pk=question_id)
    except Pergunta.DoesNotExist:
        raise Http404("Pergunta não encontrada")
    return render(request, 'enquetes/detalhar.html', {'pergunta':p})

def resultados(request,question_id):
    p = get_object_or_404 (Pergunta, pk=question_id)
    return render(request, 'enquetes/resultados.html', {'pergunta': p})

def votar(request,question_id):
    p = get_object_or_404 (Pergunta, pk=question_id)
    try:
        selecionado = p.resposta_set.get(pk=request.POST['escolha'])
    except (KeyError, Pergunta.DoesNotExist):
        return render(request, 'enquetes/detalhar.html', {
            'pergunta': p,
            'error_message': "Você não escolheu uma resposta.",
        })
    else:
        selecionado.votos += 1
        selecionado.save()
        return HttpResponseRedirect(reverse('enquetes:resultados', args=(p.id,)))