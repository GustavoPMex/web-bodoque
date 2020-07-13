from django.contrib import admin
from .models import Fotografia

# Register your models here.


class FotografiaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Fotografia, FotografiaAdmin)