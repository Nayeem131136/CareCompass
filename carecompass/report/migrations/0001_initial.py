from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='reports/photos/')),
                ('video', models.FileField(blank=True, null=True, upload_to='reports/videos/')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(
                    choices=[('pending','Pending'),('accepted','Accepted'),('rejected','Rejected'),('completed','Completed')],
                    default='pending', max_length=20
                )),
                ('created_by', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='reports',
                    to=settings.AUTH_USER_MODEL
                )),
                ('accepted_by', models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='accepted_reports',
                    to=settings.AUTH_USER_MODEL
                )),
                ('proof', models.FileField(blank=True, null=True, upload_to='proofs/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
