
from django.urls import path
from .views import home, registro, contactos, nosotros, pagina_usuario, inicio_sesion, cerrar_sesion, inventario, artefacto, informe, imprimir_pdf, proyecciones
from .calculadora import eliminar_dia_en_inventario, eliminar_artefacto, eliminar_inventario, grafico_consumo_actual, grafico_proyeccion_mensual, grafico_artefacto_mas_usado, grafico_proyeccion_semanal
urlpatterns = [
    path('', home, name="home"),
    path('login/', inicio_sesion, name="login"),
    path('registro/', registro, name="registro"),
    path('contactos/', contactos, name="contactos"),
    path('nosotros/', nosotros, name="nosotros"),
    path('paginaUsuario/', pagina_usuario, name="paginaUsuario"),
    path('c', cerrar_sesion, name="cerrarSesion"),
    path('paginaUsuario/inventario/', inventario, name="inventario"),
    path('paginaUsuario/inventario/<int:inventario_id>/', eliminar_dia_en_inventario, name='eliminarDiaEnInventario'),
    path('paginaUsuario/inventario/eliminarInventario/', eliminar_inventario, name='eliminarInventario'),
    path('paginaUsuario/inventario/artefactos/', artefacto, name="artefacto"),
    path('paginaUsuario/inventario/artefactos/<int:artefacto_id>/', eliminar_artefacto, name='eliminarArtefacto'),
    path('paginaUsuario/inventario/informe/', informe, name="informe"),
    path('paginaUsuario/inventario/informe/pdf', imprimir_pdf, name="imprimirPDF"),
    path('paginaUsuario/proyecciones/', proyecciones, name="proyecciones"),
    path('paginaUsuario/proyecciones/graficoConsumoActual', grafico_consumo_actual, name="graficoConsumoActual"),
    path('paginaUsuario/proyecciones/graficoProyeccionSemanal', grafico_proyeccion_semanal, name="grafico_proyeccion_semanal"),
    path('paginaUsuario/proyecciones/graficoProyeccionMensual', grafico_proyeccion_mensual, name="grafico_proyeccion_semanal"),
    path('paginaUsuario/proyecciones/graficoArtefactoMasUsado', grafico_artefacto_mas_usado, name="grafico_proyeccion_semanal"),

]