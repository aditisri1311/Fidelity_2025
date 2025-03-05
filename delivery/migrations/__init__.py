from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('model_id', models.IntegerField(primary_key=True)),
                ('model_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('file', models.FilePathField(max_length=500)), 
            ],
        ),
    ]
