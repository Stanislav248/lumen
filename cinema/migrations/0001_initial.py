import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанри',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
                ('seats', models.PositiveIntegerField(verbose_name='Кількість місць')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Зали',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Назва фільму')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('start_time', models.DateTimeField(verbose_name='Початок сеансу')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Ціна')),
                ('age_limit', models.PositiveIntegerField(default=0, verbose_name='Віковий ліміт')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='screenings', to='cinema.genre', verbose_name='Жанр')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='screenings', to='cinema.hall', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Сеанс',
                'verbose_name_plural': 'Сеанси',
                'ordering': ['start_time'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100, verbose_name="Ім'я клієнта")),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('seats_count', models.PositiveIntegerField(default=1, verbose_name='Кількість квитків')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('screening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='cinema.screening', verbose_name='Сеанс')),
            ],
            options={
                'verbose_name': 'Квиток',
                'verbose_name_plural': 'Квитки',
                'ordering': ['-created_at'],
            },
        ),
    ]
