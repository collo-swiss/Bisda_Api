# Generated by Django 2.1 on 2018-10-08 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_customfields'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistinctIds',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False, help_text='Deletes should deactivate not do actual deletes')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_ids', models.IntegerField(default=0)),
                ('distinct_ids', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='DistinctRows',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False, help_text='Deletes should deactivate not do actual deletes')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_count', models.IntegerField(default=0)),
                ('distinct_rows', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='MissingObservations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False, help_text='Deletes should deactivate not do actual deletes')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('rows_missing', models.TextField(null=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='projects.Project')),
            ],
        ),
    ]
