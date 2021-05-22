from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Users(models.Model):
	id = models.AutoField(primary_key= True)
	name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 100)
	phone = models.PositiveIntegerField(validators = [MaxValueValidator(999999999)])
	oriented = (('M', 'Male'), ('F', 'Female'))
	sex = models.CharField(max_length = 1, choices = oriented, default = 'M')

	def __str__(self):
		return self.name
