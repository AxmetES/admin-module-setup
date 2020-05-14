from django.contrib import admin

from .models import Flat
from .models import Complaint
from .models import Owner


class OwnerFlatInline(admin.TabularInline):
    model = Owner.owned_flat.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [
        OwnerFlatInline,
    ]
    exclude = ('by_flats',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat')
    list_display = ('text',)
    list_editable = list_display
    list_display_links = None


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'owner_phone_pure')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
