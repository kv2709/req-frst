from django.contrib import admin
from import_export.admin import ImportExportMixin
from import_export import resources

# Register your models here.
from reqs.models import RequestForsto


class RequestForstoResource(resources.ModelResource):
    class Meta:
        model = RequestForsto
        fields = ('client_name', 'phone', 'date_added', 'res_response')


class RequestForstoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['owner', 'date_added']
    resource_class = RequestForstoResource


admin.site.register(RequestForsto, RequestForstoAdmin)