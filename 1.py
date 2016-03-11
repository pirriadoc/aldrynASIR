from django_auth_ldap.backend import LDAPBackend
import cms
from cms import api
from cms.models.pagemodel import Page
alumno='javier'
titulo='javier'

ldap=LDAPBackend()
login=ldap.populate_user(alumno)
pagina=cms.api.create_page(title=titulo,template='fullwidth.html',language='en')
pag=Page.objects.filter(title_set__title=titulo)[0]
place=pagina.placeholders.get(slot='feature')
plugin=cms.api.add_plugin(placeholder=place,plugin_type='StylePlugin',language='en')
owner=cms.api.assign_user_to_page(page=pagina, user=login, grant_all=True)
public=cms.api.publish_page(page=pag,user=login,language='en')
