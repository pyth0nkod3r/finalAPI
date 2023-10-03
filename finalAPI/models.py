from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserModel(User):
    REQUIRED_FIELDS = ['username', 'email']
    USERNAME_FIELD = ['username']

class CategoryModel(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, db_index=True)
    
    def __str__(self) -> str:
        return self.title


class MenuItemModel(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    featured = models.BooleanField(db_index=True)
    price = models.DecimalField(decimal_places=2, db_index=True, max_digits=7)
    category = models.ForeignKey(
        CategoryModel, on_delete=models.PROTECT
    )


class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItemModel, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        unique_together = ('menu_item', 'user')


class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(db_index=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    delivery_status = models.BooleanField(default=0, db_index=True)
    delivery_crew = models.ForeignKey(
        User, related_name="delivery_crew", on_delete=models.SET_NULL, null=True
    )


class OrderItemModel(models.Model):
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItemModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('order', 'menu_item')
