from django.contrib import admin
from .models import Var, VarOption, VarSlug, Attestation

# Register your models here.
admin.site.register(Var)
admin.site.register(VarOption)
admin.site.register(VarSlug)
admin.site.register(Attestation)
