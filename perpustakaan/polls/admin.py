from django.contrib import admin
from polls.models import Kelompok, Buku
# Register your models here.

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul', 'penulis', 'kelompok_id', 'jumlah']
    search_fields = ['judul', 'penulis', 'penerbit']
    list_filter = ('kelompok_id',)
    list_per_page = 5


admin.site.register(Kelompok)
admin.site.register(Buku, BukuAdmin)
