from django.db import models

TYPE_CHOICES = (
    ('AutorsBucket', 'AutorsBucket'),
    ('Compositions', 'Compositions'),
    ('Busket', 'Busket'),
)

class AutorsBucket(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
    flowers = models.ManyToManyField('Flower', related_name='autors_buckets', blank=True)
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    class Meta:
        db_table = 'autors_buckets'

class Compositions(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
    flowers = models.ManyToManyField('Flower', related_name='compositions', blank=True)
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    class Meta:
        db_table = 'compositions'

class Busket(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
    flowers = models.ManyToManyField('Flower', related_name='baskets', blank=True)
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    class Meta:
        db_table = 'baskets'

class Flower(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
    choise = models.CharField(max_length=100, choices=TYPE_CHOICES)
    
    class Meta:
        db_table = 'flowers'
    
    
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.choise == 'AutorsBucket':
            bucket, _ = AutorsBucket.objects.get_or_create(name=self.name, price=self.price, photo=self.photo)
            bucket.flowers.add(self)
        elif self.choise == 'Compositions':
            composition, _ = Compositions.objects.get_or_create(name=self.name, price=self.price, photo=self.photo)
            composition.flowers.add(self)
        else:
            basket, _ = Busket.objects.get_or_create(name=self.name, price=self.price, photo=self.photo)
            basket.flowers.add(self)