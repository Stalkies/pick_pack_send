from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=24)
    phone = models.CharField(max_length=12)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Клиент"
class Cart(models.Model):
    good_id = models.BigIntegerField('Товары', max_length=24)
    client_id = models.BigIntegerField('Клиент', max_length=10)
    class Meta:
        verbose_name_plural = "Корзина"

class Good(models.Model):
    title = models.CharField('Название товара', max_length=256)
    description = models.TextField('Описание товара', max_length=4069)
    class Meta:
        verbose_name_plural = "Товары"

class Photo(models.Model):
    url = models.CharField(max_length=512)
    class Meta:
        verbose_name_plural = "Фото"
