# Generated by Django 3.0.5 on 2020-04-10 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_password',
            field=models.CharField(default='password', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_name', models.CharField(max_length=200, null=True)),
                ('follower_mobile', models.CharField(max_length=200, null=True)),
                ('follower_email', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm_title', models.CharField(max_length=200, null=True)),
                ('comm_type', models.CharField(max_length=200, null=True)),
                ('comm_desc', models.TextField(blank=True)),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
            ],
        ),
    ]
