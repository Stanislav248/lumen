from django.urls import path

from . import views

app_name = "cinema"

urlpatterns = [
    path("", views.home, name="home"),
    path("screenings/", views.screening_list, name="screening_list"),
    path("screenings/add/", views.screening_create, name="screening_create"),
    path("screenings/<int:pk>/", views.screening_detail, name="screening_detail"),
    path("screenings/<int:pk>/edit/", views.screening_update, name="screening_update"),
    path("screenings/<int:pk>/delete/", views.screening_delete, name="screening_delete"),
    path("screenings/<int:pk>/ticket/", views.ticket_create, name="ticket_create"),
    path("halls/", views.hall_list, name="hall_list"),
    path("halls/<int:pk>/", views.hall_detail, name="hall_detail"),
    path("tickets/", views.ticket_list, name="ticket_list"),
]
