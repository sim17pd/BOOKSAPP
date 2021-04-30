from django.db import models

# Create your models here.
class Books(models.Model):
	title=models.CharField(max_length=20)
	author=models.CharField(max_length=20)
	pdf=models.FileField(upload_to='uploadedbooks/pdf')

	def __str__(self):
		return self.title
		
