# Generated by Django 2.2.3 on 2019-07-25 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
    ]
