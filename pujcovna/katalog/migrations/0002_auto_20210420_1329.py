# Generated by Django 3.2 on 2021-04-20 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vypujcka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zahajeni_vypujcky', models.DateTimeField()),
                ('konec_vypujcky', models.DateTimeField()),
                ('cena', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='auto',
            name='datum_STK',
            field=models.DateField(),
        ),
    ]
