from django.contrib import admin

from oddam_w_dobre_rece.models import Category, Donation, Institution

admin.site.register(Category)
admin.site.register(Institution)
admin.site.register(Donation)