from songsets.models import SongSet, SetItem
from django.contrib import admin

class ItemInline(admin.TabularInline):
    model = SetItem

class SetAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    filter_horizontal = ['songs']
    inlines = [ItemInline]

admin.site.register(SongSet, SetAdmin)
admin.site.register(SetItem)
