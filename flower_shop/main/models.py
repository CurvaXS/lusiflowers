from django.db import models
from django.contrib.auth.models import User


TYPE_CHOICES = (
    ('AutorsBucket', 'Авторские букеты'),
    ('Compositions', 'Композиции'),
    ('Busket', 'Корзины'),
)

class AutorsBucket(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'autors_buckets'
        verbose_name_plural = 'Авторские букеты'
        verbose_name = 'Авторский букет'

class Compositions(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'compositions'
        verbose_name = 'Композиция'
        verbose_name_plural = 'Композиции'

class Busket(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    class Meta:
        db_table = 'baskets'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    name = models.ForeignKey(User, on_delete = models.PROTECT)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.created}"
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'