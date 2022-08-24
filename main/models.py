from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=24)
    phone = models.CharField(max_length=12)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Клиент"
class Cart(models.Model):
    good_id = models.IntegerField('Товары')
    client_id = models.IntegerField('Клиент')
    class Meta:
        verbose_name_plural = "Корзина"

class Good(models.Model):
    title = models.CharField('Название товара', max_length=256)
    price = models.IntegerField('Цена Товара')
    image = models.ImageField(default='no_image.jpg', upload_to='product_image')
    class Meta:
        verbose_name_plural = "Товары"
    def __str__(self):
        return f'{self.title}'

class Photo(models.Model):
    url = models.CharField(max_length=512)
    class Meta:
        verbose_name_plural = "Фото"
