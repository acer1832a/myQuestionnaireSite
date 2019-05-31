# Generated by Django 2.1.7 on 2019-05-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='annual_income',
            field=models.IntegerField(blank=True, choices=[(20, '20萬以下'), (40, '21萬至40萬'), (60, '41萬至60萬'), (100, '61萬至100萬'), (101, '100萬以上')]),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='birthday',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='education',
            field=models.CharField(blank=True, choices=[('J', '國中'), ('H', '高中'), ('B', '大學'), ('M', '碩士'), ('D', '博士')], max_length=1),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', '男性'), ('Female', '女性'), ('Others', '其它')], max_length=10),
        ),
    ]
