from django.contrib import admin

from .models import Flat
from .models import Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)

    list_filter = ('new_building', 'rooms_number', 'has_balcony')

    raw_id_fields = ('liked_by',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')
    list_display = ('text',)
    list_editable = list_display
    list_display_links = None


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
