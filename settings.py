# -*- coding: utf-8 -*-

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'aldryn-django-cms',
    'aldryn-devsync',
    'aldryn-bootstrap3',
    'aldryn-common',
    'aldryn-disqus',
    'aldryn-events',
    'aldryn-faq',
    'aldryn-forms',
    'aldryn-jobs',
    'aldryn-newsblog',
    'aldryn-people',
    'aldryn-style',
#   'django_extensions',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings
aldryn_addons.settings.load(locals())


# all django settings can be altered here

INSTALLED_APPS.extend([
    # add you project specific apps he
    'django_extensions',
])

TEMPLATE_CONTEXT_PROCESSORS.extend([
    # add your template context processors here
])

MIDDLEWARE_CLASSES.extend([
    # add your own middlewares here
])

import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = "ldap://172.17.0.10"

AUTH_LDAP_BIND_DN = "cn=admin,dc=example,dc=org"
AUTH_LDAP_BIND_PASSWORD = "admin"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=People,dc=example,dc=org",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Groups,dc=example,dc=org",
    ldap.SCOPE_SUBTREE, "(objectClass=PosixGroup)"
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType(name_attr="cn")

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=active,ou=Groups,dc=example,dc=org",
    "is_staff": "cn=staff,ou=groups,dc=example,dc=org",
    "is_superuser": "cn=superuser,ou=Groups,dc=example,dc=org"
}

AUTH_LDAP_FIND_GROUP_PERMS = True

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn"
}

CMS_PERMISSION = True
