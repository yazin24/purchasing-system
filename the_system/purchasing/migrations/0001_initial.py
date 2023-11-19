# Generated by Django 4.2.7 on 2023-11-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('unit_measurement', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('contact_person', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100)),
                ('items_suppliers', models.ManyToManyField(related_name='suppliers_supplier', to='purchasing.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='suppliers',
            field=models.ManyToManyField(related_name='supplier_items', to='purchasing.supplier'),
        ),
    ]
