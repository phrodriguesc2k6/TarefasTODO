from django.shortcuts import render, redirect, get_object_or_404
from .models import list
from .form import formulario  # Certifique-se de que a importação está correta

def list_view(request):
    all_list = list.objects.all()
    search = request.GET.get('search')
    
    if search:
        all_list = list.objects.filter(Name__icontains=search)  # Use o campo correto para a busca
    else:
        all_list = list.objects.all()
    return render(request, 'list.html', {'all_list': all_list})

def form_view(request):
    if request.method == "POST":
        form = formulario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_view')
    else:
        form = formulario()
    return render(request, 'list_form.html', {'form': form})

def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(list, id=tarefa_id)  # Obtém a tarefa existente
    
    if request.method == 'POST':
        form = formulario(request.POST, request.FILES, instance=tarefa)  # Preenche o formulário com a tarefa existente
        if form.is_valid():
            form.save()  # Atualiza a tarefa existente
            return redirect('list_view')
    else:
        form = formulario(instance=tarefa)  # Cria o formulário preenchido com os dados da tarefa existente
    
    return render(request, 'editar_tarefa.html', {'form': form, 'tarefa': tarefa})

def delete_list(request, Task_id):
    if request.method == 'POST':
        Task = get_object_or_404(list, id=Task_id)
        Task.delete()
        return redirect('list_view')

    return redirect('list_view')
