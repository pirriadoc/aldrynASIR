from django_auth_ldap.backend import LDAPBackend
import cms
from cms import api
from cms.models.pagemodel import Page
import aldryn_newsblog
from aldryn_newsblog.models import NewsBlogConfig
from django.core.management.base import BaseCommand, CommandError
#alumno='prueba3'

class Command(BaseCommand):
    def add_arguments(self, parser):
        # Parametro posicional
        parser.add_argument('usuario', nargs='+', type=str)
    def handle(self, *args, **options):
        for alumno in options['usuario']:
            ldap=LDAPBackend()
#poblamos el ldap con el usuario que va a poseer la pagina
            login=ldap.populate_user(alumno)
#instanciamos la pagina padre para poder usarla luego en la creacion
            padre=Page.objects.filter(title_set__title='Alumnos')[0]
#creamos una instancia de NewsblogConfig para crear el namespace y pasarle a apphook la instancia de la app
            configuracion=NewsBlogConfig(app_title='NewsBlog',namespace=alumno)
            configuracion.save_base()
            configuracion.create_translation(language_code='en')
#creamos la pagina
            pagina=cms.api.create_page(title=alumno,template='fullwidth.html',language='en',apphook='NewsBlogApp',apphook_namespace=configuracion.namespace,parent=padre,in_navigation=True,published=True,created_by=login)
#ponemos un placeholder a la pagina
            place=pagina.placeholders.get(slot='feature')
#ponemos un par de plugins al placeholder
            plugin1=cms.api.add_plugin(placeholder=place,plugin_type='StylePlugin',language='en')
            plugin2=cms.api.add_plugin(placeholder=place,plugin_type='StylePlugin',language='en')
#asignamos propietario y permisos de acceso a la pagina
            propietario=cms.api.assign_user_to_page(page=pagina, user=login, grant_all=True)
#publicamos los cambios
            pagina.publish(language='en')

##original_filename para buscar imagenes por su nombre, a=Image.objects.get(original_filename=loquesea.jpg)
#permisos pal usuario
#aldryn_newsblog.add_article
#aldryn_newsblog.change_article
#aldryn_newsblog.delete_article
