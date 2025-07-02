from django.contrib import admin

from course.models import Entraineur, Proprietaire, Utilisateur

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Entraineur)
admin.site.register(Proprietaire)
