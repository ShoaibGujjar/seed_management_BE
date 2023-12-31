# Generated by Django 4.0.3 on 2023-09-26 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seeds', '0007_rename_commition_sale_commission'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='kgForPrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='kgForPrice',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True)),
                ('quantity_kg', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('kgForPrice', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('quantity_mn', models.CharField(blank=True, max_length=100, null=True)),
                ('grinding', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mixing', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('net_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vehicle', models.CharField(blank=True, max_length=100, null=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seeds.seed')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seeds.customer')),
            ],
        ),
    ]
