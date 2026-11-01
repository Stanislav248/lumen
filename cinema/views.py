from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .decorators import staff_required
from .forms import ScreeningForm, TicketForm
from .models import Genre, Hall, Screening, Ticket


def home(request):
    latest = (Screening.objects.select_related("genre", "hall")
              .prefetch_related("tickets").order_by("-pk")[:3])
    context = {
        "latest": latest,
        "screening_count": Screening.objects.count(),
        "hall_count": Hall.objects.count(),
        "genre_count": Genre.objects.count(),
    }
    return render(request, "cinema/home.html", context)


def screening_list(request):
    screenings = Screening.objects.select_related("genre", "hall").prefetch_related("tickets")
    q = request.GET.get("q", "").strip()
    genre_id = request.GET.get("genre", "")
    if q:
        screenings = screenings.filter(title__icontains=q)
    if genre_id.isdigit():
        screenings = screenings.filter(genre_id=int(genre_id))
    else:
        genre_id = ""
    context = {
        "screenings": screenings,
        "genres": Genre.objects.all(),
        "q": q,
        "genre_id": genre_id,
    }
    return render(request, "cinema/screening_list.html", context)


def screening_detail(request, pk):
    screening = get_object_or_404(
        Screening.objects.select_related("genre", "hall"), pk=pk
    )
    return render(request, "cinema/screening_detail.html", {"screening": screening})


@staff_required
def screening_create(request):
    if request.method == "POST":
        form = ScreeningForm(request.POST)
        if form.is_valid():
            screening = form.save()
            messages.success(request, "Сеанс створено.")
            return redirect("cinema:screening_detail", pk=screening.pk)
    else:
        form = ScreeningForm()
    return render(request, "cinema/screening_form.html",
                  {"form": form, "title": "Новий сеанс"})


@staff_required
def screening_update(request, pk):
    screening = get_object_or_404(Screening, pk=pk)
    if request.method == "POST":
        form = ScreeningForm(request.POST, instance=screening)
        if form.is_valid():
            form.save()
            messages.success(request, "Сеанс оновлено.")
            return redirect("cinema:screening_detail", pk=screening.pk)
    else:
        form = ScreeningForm(instance=screening)
    return render(request, "cinema/screening_form.html",
                  {"form": form, "title": "Редагування сеансу"})


@staff_required
def screening_delete(request, pk):
    screening = get_object_or_404(Screening, pk=pk)
    if request.method == "POST":
        screening.delete()
        messages.success(request, "Сеанс видалено.")
        return redirect("cinema:screening_list")
    return render(request, "cinema/screening_confirm_delete.html",
                  {"screening": screening})


def hall_list(request):
    return render(request, "cinema/hall_list.html", {"halls": Hall.objects.all()})


def hall_detail(request, pk):
    hall = get_object_or_404(Hall, pk=pk)
    screenings = hall.screenings.select_related("genre").order_by("start_time")
    return render(request, "cinema/hall_detail.html",
                  {"hall": hall, "screenings": screenings})


def ticket_create(request, pk):
    screening = get_object_or_404(Screening, pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, screening=screening)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.screening = screening
            ticket.save()
            messages.success(request, "Квитки придбано!")
            return redirect("cinema:screening_detail", pk=screening.pk)
    else:
        form = TicketForm(screening=screening)
    return render(request, "cinema/ticket_form.html",
                  {"form": form, "screening": screening})


@staff_required
def ticket_list(request):
    tickets = Ticket.objects.select_related("screening")
    return render(request, "cinema/ticket_list.html", {"tickets": tickets})
