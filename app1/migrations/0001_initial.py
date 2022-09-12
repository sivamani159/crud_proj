# Generated by Django 3.2 on 2022-09-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('courses', models.CharField(choices=[('1', 'python'), ('2', 'django'), ('3', 'devops'), ('4', 'others')], default='1', max_length=30)),
                ('jdate', models.DateField()),
            ],
        ),
    ]