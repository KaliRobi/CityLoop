from django.db import migrations

def migrate_mode_of_transport(apps, schema_editor):
    YourModel = apps.get_model('yourappname', 'YourModel')
    ModeOfTransport = apps.get_model('yourappname', 'ModeOfTransport')
    for obj in YourModel.objects.all():
        mode_of_transport, created = ModeOfTransport.objects.get_or_create(name=obj.mode_of_transport)
        obj.new_mode_of_transport = mode_of_transport
        obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('yourappname', 'previous_migration'),
    ]

    operations = [
        migrations.RunPython(migrate_mode_of_transport),
    ]