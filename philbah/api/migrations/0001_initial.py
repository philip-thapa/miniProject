from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="philbah",
                          email="philbah@miniproject.com",
                          is_staff=True,
                          is_superuser=True,
                          phoneNumber="8106267754",
                          gender="Male"
                          )
        user.set_password("philbah528")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
