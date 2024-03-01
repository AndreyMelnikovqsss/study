# serializers.py

from rest_framework import serializers

from . import models
from .models import Product, Lesson


class ProductDetailSerializer(serializers.ModelSerializer):
    num_students = serializers.SerializerMethodField()
    group_fill_percentage = serializers.SerializerMethodField()
    product_purchase_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_num_students(self, obj):
        return obj.membership_set.count()

    def get_group_fill_percentage(self, obj):
        total_groups = obj.group_set.count()
        total_users = obj.membership_set.count()

        if total_groups == 0:
            return 0

        average_group_size = total_users / total_groups
        max_group_size = obj.group_set.aggregate(models.Max('max_users'))['max_users__max']

        if max_group_size == 0:
            return 0

        fill_percentage = (average_group_size / max_group_size) * 100
        return round(fill_percentage, 2)

    def get_product_purchase_percentage(self, obj):
        total_users = User.objects.count()
        purchased_users = obj.membership_set.count()

        if total_users == 0:
            return 0

        purchase_percentage = (purchased_users / total_users) * 100
        return round(purchase_percentage, 2)
