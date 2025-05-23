# Generated by Django 4.2.20 on 2025-05-23 06:59

from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_mainservice_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecializedServiceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
                ('icon', models.CharField(help_text="FontAwesome class (e.g., 'fas fa-star')", max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/service_images/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialized_service_cards', to='main.mainservice')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ServiceTypeCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
                ('icon', models.CharField(help_text="FontAwesome class (e.g., 'fas fa-home')", max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/service_images/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_type_cards', to='main.mainservice')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='IdealForCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
                ('icon', models.CharField(help_text="FontAwesome class (e.g., 'fas fa-home')", max_length=50)),
                ('order', models.PositiveIntegerField(default=0)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ideal_for_cards', to='main.mainservice')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='HyperlinkCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
                ('link_text', models.CharField(max_length=100)),
                ('link_url', models.CharField(max_length=200)),
                ('icon', models.CharField(help_text="FontAwesome class (e.g., 'fas fa-link')", max_length=50)),
                ('order', models.PositiveIntegerField(default=0)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hyperlink_cards', to='main.mainservice')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='BookingStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=200)),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
                ('icon', models.CharField(help_text="FontAwesome class (e.g., 'fas fa-calendar')", max_length=50)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_steps', to='main.mainservice')),
            ],
            options={
                'ordering': ['step_number'],
            },
        ),
    ]
