from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ArtefactoForm, InventarioForm, CrearUsuario
from .models import Artefacto, Inventario, Informe
import datetime
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint.text.fonts import FontConfiguration
from weasyprint import HTML
from .calculadora import calcular_consumo_total, eliminar_dia_en_inventario, eliminar_artefacto, calcular_consumo_total_mensual , eliminar_inventario


# Create your views here.
def home(request):
    return render(request, 'energy/home/index.html')
def contactos(request):
    return render(request, 'energy/home/contactos.html')
def nosotros(request):
    return render(request, 'energy/home/sobreNosotros.html')
def pagina_usuario(request):
    return render(request, 'energy/home/paginaUsuario.html')

def cerrar_sesion(request):
    return render(request, 'energy/home/index.html', {'cS': logout(request)})




def registro(request):
    if request.method == 'GET':
        return render(request, 'energy/home/registro.html', {
            'form': CrearUsuario
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                user.save()
                login(request, user)
                return redirect('paginaUsuario')
            except IntegrityError:
                return render(request, 'energy/home/registro.html', {
                    'form': CrearUsuario,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'energy/home/registro.html', {
            'form': CrearUsuario,
            'error': 'Las contraseñas no coinciden'
        })
def inicio_sesion(request):
    if request.user.is_authenticated:
        return redirect('paginaUsuario')
    if request.method == 'GET':
        return render(request, 'energy/home/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'energy/home/login.html', {
                'form': AuthenticationForm,
                'error': 'El usuario es incorrecto',
            })
        else:
            login(request, user)
            return render(request, 'energy/home/paginaUsuario.html')







def artefacto(request):
    if request.user.is_authenticated:
        artefacto = Artefacto.objects.filter(user=request.user)
        if request.method == 'GET':
            form = ArtefactoForm()
            return render(request, 'energy/home/artefactos.html', {
                'form': form,
                'artefacto': artefacto
            })
        elif request.method == 'POST':
            form = ArtefactoForm(request.POST)
            if form.is_valid():
                artefacto = form.save(commit=False)
                #artefacto ya existe dentro del usuario
                if Artefacto.objects.filter(user=request.user, nombre_artefacto=artefacto.nombre_artefacto).exists():
                    return render(request, 'energy/home/artefactos.html', {
                        'form': form,
                        'artefacto': artefacto,
                        'error': 'El artefacto ya existe',
                    })
                artefacto.user = request.user
                artefacto.save()
                return redirect('artefacto')
            else:
                # Manejar el caso de un formulario no válido
                return render(request, 'energy/home/artefactos.html', {
                    'form': form,
                    'artefacto': artefacto,
                })
    return render(request, 'energy/home/artefactos.html', {
        'eliminar': eliminar_artefacto,
        })








def inventario(request):
    if request.user.is_authenticated:
        inventario_artefacto = Inventario.objects.filter(user=request.user)
        consumo_diario_del_mes = Informe.objects.filter(user=request.user)

        if request.method == 'GET':
            form = InventarioForm(user=request.user)
            return render(request, 'energy/home/inventario.html', {
                'form': form,
                'inventario_artefacto': inventario_artefacto,
                'consumo_diario': consumo_diario_del_mes,
                'eliminar_inventario': eliminar_inventario,
            })

        elif request.method == 'POST':
            form = InventarioForm(request.user, request.POST)
            if form.is_valid():
                inventario = form.save(commit=False)
                # Obtén el ID del artefacto desde el formulario
                artefacto = InventarioForm(request.user, request.POST).data['artefacto']
                print(artefacto)
                # Verifica si ya existe un inventario para el usuario, el día y el artefacto
                if Inventario.objects.filter(user=request.user, dia=inventario.dia, artefacto_id=artefacto).exists():
                    return redirect('inventario')
                else:
                    inventario.user = request.user
                    inventario.artefacto = Artefacto.objects.get(id=artefacto)
                    ######################
                    inventario.consumo_artefacto = calcular_consumo_total(inventario.artefacto.consumo_wh, inventario.artefacto.horas_de_uso, inventario.cantidad_artefacto)
                    inventario.save()
                    Informe.actualizar_consumo_diario(request.user, inventario.dia, inventario.consumo_artefacto)

                ######################
                    return redirect('inventario')
            else:
                # Manejar el caso de un formulario no válido
                return render(request, 'energy/home/inventario.html', {
                    'form': form,
                    'inventario_artefacto': inventario_artefacto,
                    'consumoDiario': consumo_diario_del_mes,
                    'eliminarInventario': eliminar_inventario,
                })
    else:
        # Manejar el caso en que el usuario no está autenticado
        return render(request, 'energy/home/inventario.html', {
            'eliminar': eliminar_dia_en_inventario,
        })



def informe(request):
    if request.user.is_authenticated:
        consumo_diario_del_mes = Informe.objects.filter(user=request.user)
        total_mensual = calcular_consumo_total_mensual(request.user)
        return render(request, 'energy/home/informe.html', {
            'consumoDiario': consumo_diario_del_mes,
            'user': request.user,
            'consumoTotalMensual': total_mensual
        })
    return render(request, 'energy/home/informe.html')



def imprimir_pdf(request):
    context = {
        'consumoDiario': Informe.objects.filter(user=request.user),
        'user': request.user,
        'consumoTotalMensual': calcular_consumo_total_mensual(request.user),
    }

    html = render_to_string('energy/home/informe.html', context)
    response = HttpResponse(content_type='application/pdf')

    # Incluir la fecha actual en el nombre del archivo
    fecha_actual = datetime.date.today().strftime("%Y-%m-%d")
    nombre_archivo = f"Inform_de_{request.user.username}_{fecha_actual}.pdf"

    # Sanitizar el nombre del archivo para manejar caracteres especiales
    response['Content-Disposition'] = 'filename="{}"'.format(nombre_archivo)

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)
    return response



def proyecciones(request):
    if request.user.is_authenticated:
        return render(request, 'energy/home/proyecciones.html')
    else:
      return render(request, 'energy/home/paginaUsuario.html')
