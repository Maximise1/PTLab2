from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()

    def update(self, new_q):
        self.quantity = new_q

    def getQuantity(self):
        return self.quantity

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)