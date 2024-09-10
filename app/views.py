from django.shortcuts import render, redirect, get_object_or_404
from .models import list
from .form import formulario

def list_view(request):
    all_list = list.objects.all()
    search = request.GET.get('search')
    
    if search:
        all_list = list.objects.filter(model__contains=search)
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
    return render(request, 'list_form.html', {'form':form})


def delete_list(request, Task_id):
    if request.method == 'POST':
        Task = get_object_or_404(list, id=Task_id)
        Task.delete()
        return redirect('list_view')

    return redirect('list_view')

    

    


    

