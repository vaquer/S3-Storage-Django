from django.db import models


class TestModel(models.Model):
	name = models.CharField('Name', max_length=250, null=True)
	pic = models.ImageField('Image', upload_to='test_images')
