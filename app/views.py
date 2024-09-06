from django.shortcuts import render, redirect
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

        
    

    

    

