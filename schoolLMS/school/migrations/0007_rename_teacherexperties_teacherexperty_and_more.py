# Generated by Django 4.0.8 on 2022-11-21 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0006_rename_teacherclasse_teacherclass_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="TeacherExperties",
            new_name="TeacherExperty",
        ),
        migrations.AlterUniqueTogether(
            name="teacherclass",
            unique_together={("class_grade", "teacher")},
        ),
    ]