from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pending')


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_link = models.URLField()


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    min_users = models.PositiveIntegerField()
    max_users = models.PositiveIntegerField()
    users = models.ManyToManyField(User, related_name='groups')
