from django.contrib import admin
from .models import Product
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django import forms
from django.urls import path
import csv
from io import TextIOWrapper

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
    
    export_as_csv.short_description = "Export selected"

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class ProductAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('id', 'sku', 'title')
    list_display_links = ('id', 'sku', 'title')
    change_list_template = "product/products_changelist.html"

    actions = ["export_as_csv"]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = TextIOWrapper(request.FILES['csv_file'].file, encoding=request.encoding)
            reader = csv.reader(csv_file)
            next(reader, None)
            for row in reader:
                defaults = {
                    "title": row[1],
                    "sku": row[2],
                    "id_product": row[3],
                    "category": row[4],
                    "shipping_class": row[5],
                    "image_url": row[6],
                    "price_b2b": row[7],
                    "price_b2c": row[8],
                    "pa_color": row[9],
                    "pa_type": row[10],
                    "pa_year": row[11],
                    "pa_wheels": row[12],
                    "pa_model": row[13],
                    "pa_class": row[14],
                    "pa_brand": row[15],
                    "pa_battery": row[16],
                    "description": row[17],
                }
                try:
                    obj = Product.objects.get(sku=row[2])
                    for key, value in defaults.items():
                        setattr(obj, key, value)
                    obj.save()
                except Product.DoesNotExist:
                    obj = Product(**defaults)
                    obj.save()
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)

admin.site.register(Product, ProductAdmin)