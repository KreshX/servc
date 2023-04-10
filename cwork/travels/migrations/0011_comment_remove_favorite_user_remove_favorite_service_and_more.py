# Generated by Django 4.0.5 on 2022-07-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0010_company_user_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40)),
                ('text', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='service',
        ),
        migrations.AddField(
            model_name='favorite',
            name='service',
            field=models.CharField(default='1', max_length=40),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
