# Generated by Django 4.0.4 on 2022-10-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencer', '0006_influencer_profile_facebook_page_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouTubeCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Category', models.CharField(max_length=50)),
            ],
        ),
    ]