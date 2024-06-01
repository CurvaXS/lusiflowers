from django.db import models


TYPE_CHOISES = {
    ('AutorsBucket', 'AutorsBucket'),
    ('Compositions', 'Compositions'),
    ('Busket', 'Busket'),
}

class AutorsBucket(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    
    class Meta:
        db_table = 'autors_buckets'

class Compositions(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    
    class Meta:
        db_table = 'compositions'

class Busket(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    
    class Meta:
        db_table = 'baskets'

class Flower(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    choise = models.CharField(max_length=100, choices=TYPE_CHOISES)
    
    
    class Meta:
        db_table = 'flowers'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Логика для дублирования объекта Flower в одну из таблиц
        if self.choise == 'AutorsBucket':  # Например, условие для добавления в AutorsBucket
            bucket = AutorsBucket.objects.first()
            if bucket:
                bucket.flowers.add(self)
            else:
                AutorsBucket.objects.create(name=self.name, price=self.price)
        elif self.choise == 'Compositions':  # Условие для добавления в Compositions
            composition = Compositions.objects.first()
            if composition:
                composition.flowers.add(self)
            else:
                Compositions.objects.create(name=self.name, price=self.price)
        else:  # Условие для добавления в Busket
            basket = Busket.objects.first()
            if basket:
                basket.flowers.add(self)
            else:
                Busket.objects.create(name=self.name, price=self.price)
