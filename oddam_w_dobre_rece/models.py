from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
TypesOfInstituion = (
        ('Foundation', "Fundacja"),
        ('Non-governmental organization', "Organizacja pozarządowa"),
        ('Local collection', "Zbiórka lokalna"),
    )

class Category(models.Model):
    name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.name



class Institution(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    type = models.CharField(max_length=35, choices=TypesOfInstituion, default="Foundation")
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator('^(?:\(?\?)?(?:[-\.\(\)\s]*(\d)){9}\)?$')])
    city = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=6, validators=[RegexValidator('[0-9]{2}-[0-9]{3}')])
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_taken = models.BooleanField(default=False)
    taken_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.address}, {self.pick_up_date} {self.quantity} worków, dla {self.institution}'