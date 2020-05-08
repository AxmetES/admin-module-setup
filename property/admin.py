from django.contrib import admin

from .models import Flat
from .models import Complaint
from .models import Owner


class OwnerFlatInline(admin.TabularInline):
    model = Owner.owned_flat.through


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by', 'by_flats',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')
    list_display = ('text',)
    list_editable = list_display
    list_display_links = None


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    raw_id_fields = ('owned_flat',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
