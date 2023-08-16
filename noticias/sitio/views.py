from django.shortcuts import render, redirect
from sitio.models import Noticia
from sitio.forms import FormNoticia, FormNoticiaCopado
from datetime import datetime
from django.contrib.auth.decorators import login_required


def inicio(request):
    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.save()

    noticias = Noticia.objects.filter(archivada=False).order_by("fecha")
    return render(request, 'inicio.html', {'lista_noticias': noticias})


def prueba_form_pelado(request):
    if request.method == "POST":
        nueva = Noticia()
        nueva.titulo = 'entro ' + request.POST['nombre']
        nueva.texto = 'tiene ' + request.POST['edad'] + ' años'
        nueva.fecha = datetime.now()
        nueva.save()

        return redirect("/inicio/")
    else:
        return render(request, 'prueba_form_pelado.html', {})


def prueba_form_django(request):
    if request.method == "POST":
        form = FormNoticia(request.POST)
        if form.is_valid():
            nueva = Noticia()
            nueva.titulo = form.cleaned_data['titulo']
            nueva.texto = form.cleaned_data['texto']
            nueva.archivada = form.cleaned_data['archivada']
            nueva.fecha = datetime.now()
            nueva.save()
            return redirect("/inicio/")
    else:
        form = FormNoticia()

    return render(request, 'prueba_form_django.html', {'form_noticia': form})


@login_required
def prueba_form_django_reloaded(request):
    if request.method == "POST":
        form = FormNoticiaCopado(request.POST)
        if form.is_valid():
            form.save()
            # nueva = form.save(commit=False)
            # nueva.archivada = False
            # nueva.save()
            return redirect("/inicio/")
    else:
        form = FormNoticiaCopado()

    return render(request, 'prueba_form_django.html', {'form_noticia': form})
