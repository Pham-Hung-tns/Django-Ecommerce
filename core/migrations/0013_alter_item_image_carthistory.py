# Generated by Django 5.1.2 on 2024-11-23 08:46

import django.db.models.deletion
import imagekit.models.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_payment_vnpay_amount_payment_vnpay_order_desc_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=''),
        ),
        migrations.CreateModel(
            name='CartHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]