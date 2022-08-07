from django.contrib import admin
from .models import Company,Tag,Category
from django.contrib.auth.models import Group

class TagInline(admin.TabularInline):
    model = Company.tags.through

class CompanyAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['tags']

admin.site.register(Company,CompanyAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.unregister(Group)
