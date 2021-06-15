from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField
    immenseness = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='owners/')

    def __str__(self):
        return self.first_name + self.last_name


class PizzaShop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city_of_location = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='pizzashops')

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=3, max_digits=8)
    description = models.TextField()
    sizes_of_pizzas_choises = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    ]
    size = models.CharField(choices=sizes_of_pizzas_choises, max_length=20)
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE, related_name='pizzas')

    def __str__(self):
        return self.name
