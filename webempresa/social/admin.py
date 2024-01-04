from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    #Para extender esta función en tiempo de ejecución:
    def get_readonly_fields(self, request, obj=None):
        #request nos permite comprobar en el tiempo de ejecución si hay un usuario y si ese usuario forma parte del grupo PERSONAL:
        #Si en tiempo de ejecución, el usuario que está accediendo al admin forma parte del grupo PERSONAL, readonly_fields pasará a tener el valor de la tupla
        if request.user.groups.filter(name="Personal").exists():
            return ('created', 'updated', 'key', 'name')
        else:
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)