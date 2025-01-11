import logging

from diario.models import Diario, Pessoa

logger = logging.getLogger(__name__)

from datetime import datetime, timedelta
from django.shortcuts import redirect, render


def home(request):
    textos = Diario.objects.order_by('create_at')[:3]
    pessoas = Pessoa.objects.all()

    nomes = [pessoa.nome for pessoa in pessoas]
    qtds = []
    for pessoa in pessoas:
        qtd = Diario.objects.filter(pessoas=pessoa).count()
        qtds.append(qtd)


    '''pessoas_com_contagem = Pessoa.objects.annotate(qtd_diarios=Count('diario'))
    nomes = [pessoa.nome for pessoa in pessoas_com_contagem]
    qtds = [pessoa.qtd_diarios for pessoa in pessoas_com_contagem]'''

    return render(request, 'home.html', {'textos': textos, 'nomes': nomes, 'qtds': qtds})

def escrever(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()  # Busca todas as pessoas
        textos = Diario.objects.order_by('create_at')  # Busca todos os diários ordenados pela data de criação
        return render(request, 'escrever.html', {'pessoas': pessoas, 'textos': textos})
    else:
        title = request.POST.get('title')  # Obtém o título do diário
        tags = request.POST.getlist('tags')  # Obtém as tags selecionadas
        people = request.POST.getlist('people')  # Obtém as pessoas associadas ao diário
        text = request.POST.get('text')  # Obtém o conteúdo do diário

        # Verifica se o título ou texto estão vazios
        if len(title.strip()) == 0 or len(text.strip()) == 0:
            logger.error("Erro: Título ou texto vazio.")
            return redirect('escrever')

        try:
            # Cria o diário
            diario = Diario(
                titulo=title,
                texto=text
            )

            # Salva o diário primeiro para gerar o id
            diario.save()

            # Usa o método set_tags para associar as tags ao diário
            if tags:
                diario.set_tags(tags)

            # Obtém as pessoas selecionadas e as associa ao diário
            pessoa_objs = Pessoa.objects.filter(id__in=people)
            diario.pessoas.add(*pessoa_objs)

            # Salva novamente após adicionar as tags e as pessoas
            diario.save()

            logger.info(f"Diário criado com sucesso. Título: {title}")
            
        except Exception as e:
            logger.error(f"Erro ao salvar o diário: {e}")
            return redirect('escrever')

        return redirect('escrever')
    
def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'pessoa.html')
    else:
        nome = request.POST.get('name')
        foto = request.FILES.get('photo')

        pessoa = Pessoa(
            nome=nome,
            foto=foto
        )
        pessoa.save()
        return redirect('escrever')
    
def dia(request):
    data = request.GET.get('data')
    data_formatada = datetime.strptime(data, '%Y-%m-%d')
    diarios = Diario.objects.filter(create_at__gte=data_formatada).filter(create_at__lte=data_formatada + timedelta(days=1))

    return render(request, 'dia.html', {'diarios': diarios, 'total': diarios.count(), 'data': data})

def excluir_dia(request):
    dia = datetime.strptime(request.GET.get('data'), '%Y-%m-%d')
    diarios = Diario.objects.filter(create_at__gte=dia).filter(create_at__lte=dia + timedelta(days=1))
    diarios.delete()
    return redirect('escrever')
