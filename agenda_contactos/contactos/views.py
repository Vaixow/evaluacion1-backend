from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm
from django.db.models import Q

# Crear un contacto
def agregar_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contactos')
    else:
        form = ContactoForm()
    return render(request, 'contactos/agregar_contacto.html', {'form': form})

# Listar contactos
def listar_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'contactos/listar_contactos.html', {'contactos': contactos})

# Buscar contactos
def buscar_contactos(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Contacto.objects.filter(
            Q(nombre__icontains=query) | Q(correo__icontains=query)
        )
    return render(request, 'contactos/buscar_contactos.html', {'resultados': resultados, 'query': query})

# Eliminar contacto
def eliminar_contacto(request, contacto_id):
    contacto = get_object_or_404(Contacto, id=contacto_id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('listar_contactos')
    return render(request, 'contactos/eliminar_contacto.html', {'contacto': contacto})
# Create your views here.
