# Generated by Django 3.1.4 on 2021-02-20 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0002_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_group', to='auth.group', to_field='name'),
        ),
    ]
