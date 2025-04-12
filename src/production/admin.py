from django.contrib import admin
from .models import Production

@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ("nom", "date", "quantite", "user", "vendue")
    search_fields = ("nom", "user__email")  # ou "user__username" selon ton User model
    list_filter = ("date",)
