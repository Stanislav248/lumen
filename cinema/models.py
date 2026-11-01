from django.db import models


class Hall(models.Model):
    name = models.CharField("Назва", max_length=50)
    seats = models.PositiveIntegerField("Кількість місць")

    class Meta:
        ordering = ["name"]
        verbose_name = "Зал"
        verbose_name_plural = "Зали"

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField("Назва", max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"

    def __str__(self):
        return self.name


class Screening(models.Model):
    title = models.CharField("Назва фільму", max_length=150)
    description = models.TextField("Опис", blank=True)
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT,
        related_name="screenings", verbose_name="Жанр",
    )
    hall = models.ForeignKey(
        Hall, on_delete=models.PROTECT,
        related_name="screenings", verbose_name="Зал",
    )
    start_time = models.DateTimeField("Початок сеансу")
    price = models.DecimalField("Ціна", max_digits=6, decimal_places=2)
    age_limit = models.PositiveIntegerField("Віковий ліміт", default=0)

    class Meta:
        ordering = ["start_time"]
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеанси"

    def __str__(self):
        return f"{self.title} ({self.start_time:%d.%m %H:%M})"

    def free_seats(self):
        sold = sum(t.seats_count for t in self.tickets.all())
        return self.hall.seats - sold


class Ticket(models.Model):
    screening = models.ForeignKey(
        Screening, on_delete=models.CASCADE,
        related_name="tickets", verbose_name="Сеанс",
    )
    client_name = models.CharField("Ім'я клієнта", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    seats_count = models.PositiveIntegerField("Кількість квитків", default=1)
    created_at = models.DateTimeField("Створено", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Квиток"
        verbose_name_plural = "Квитки"

    def __str__(self):
        return f"{self.client_name} — {self.screening.title}"
