# Generated by Django 1.11.27 on 2020-01-07 16:52


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0016_auto_20190703_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persistentsubsectiongradeoverridehistory',
            name='user',
        ),
        migrations.DeleteModel(
            name='PersistentSubsectionGradeOverrideHistory',
        ),
    ]
