from django.db import models

# Create your models here.

class FileUploader(models.Model):
	file_name = models.CharField(max_length=200)
	file_type = models.CharField(max_length=100)
	file = models.FileField(upload_to='files', null=True, verbose_name="")
	description = models.CharField(max_length=500)

	def __str__(self):
		return self.file_name