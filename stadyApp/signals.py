from time import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Membership, Group


@receiver(post_save, sender=Membership)
def distribute_user_to_group(sender, instance, **kwargs):
    # Получаем продукт и пользователя из Membership
    product = instance.product
    user = instance.user

    # Если продукт еще не начался
    if product.start_datetime > timezone.now():
        # Получаем или создаем все группы для данного продукта
        groups = Group.objects.filter(product=product)
        if not groups.exists():
            groups = [Group.objects.create(product=product, name=f"Group {i+1}") for i in range(3)]

        # Распределяем пользователя в группу
        group = min(groups, key=lambda g: g.users.count())
        group.users.add(user)

        # Проверяем, что количество пользователей в группе не превышает максимальное значение
        if group.users.count() > group.max_users:
            # Удаляем пользователя из группы и добавляем в следующую
            group.users.remove(user)
            next_group = min(groups, key=lambda g: g.users.count() + 1)
            next_group.users.add(user)

    # Сохраняем изменения
    instance.save()
