from django.db import migrations

def migrate_mode_of_transport(apps, schema_editor):
    shipmentDetailsModel = apps.get_model('shipmentregister', 'ShipmentDetailsModel')
    modeOfTransportmodel = apps.get_model('shipmentregister', 'ModeOfTransport')
    for obj in shipmentDetailsModel.objects.all():
        mode_of_transport, created = modeOfTransportmodel.objects.get_or_create(name=obj.mode_of_transport)
        obj.new_mode_of_transport = mode_of_transport
        obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('yourappname', '0003_alter_shipmentdetailsmodel_mode_of_transport'),
    ]

    operations = [
        migrations.RunPython(migrate_mode_of_transport),
    ]