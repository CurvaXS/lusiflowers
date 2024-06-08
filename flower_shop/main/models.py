from django.db import models

TYPE_CHOICES = (
    ('AutorsBucket', 'AutorsBucket'),
    ('Compositions', 'Compositions'),
    ('Busket', 'Busket'),
)

class AutorsBucket(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo_url = models.CharField(max_length=9999, default='')
    flowers = models.ManyToManyField('Flower', related_name='autors_buckets', blank=True)
    
    class Meta:
        db_table = 'autors_buckets'

class Compositions(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo_url = models.URLField(blank=True, null=True)
    flowers = models.ManyToManyField('Flower', related_name='compositions', blank=True)
    
    class Meta:
        db_table = 'compositions'

class Busket(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo_url = models.URLField(blank=True, null=True)
    flowers = models.ManyToManyField('Flower', related_name='baskets', blank=True)
    
    class Meta:
        db_table = 'baskets'

class Flower(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
    choise = models.CharField(max_length=100, choices=TYPE_CHOICES)
    
    class Meta:
        db_table = 'flowers'
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.choise == 'AutorsBucket':
            bucket = AutorsBucket.objects.first()
            if bucket:
                bucket.flowers.add(self)
            else:
                AutorsBucket.objects.create(name=self.name, price=self.price, photo_url=self.photo_url)
        elif self.choise == 'Compositions':
            composition = Compositions.objects.first()
            if composition:
                composition.flowers.add(self)
            else:
                Compositions.objects.create(name=self.name, price=self.price, photo_url=self.photo_url)
        else:
            basket = Busket.objects.first()
            if basket:
                basket.flowers.add(self)
            else:
                Busket.objects.create(name=self.name, price=self.price, photo_url=self.photo_url)