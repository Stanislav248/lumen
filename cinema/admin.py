from django.contrib import admin

from .models import Genre, Hall, Screening, Ticket


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ("name", "seats")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "hall", "start_time", "price", "age_limit")
    list_filter = ("genre", "hall")
    search_fields = ("title",)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("client_name", "screening", "seats_count", "created_at")
