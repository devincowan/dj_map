from django.db import models

# Create your models here.

class Point(models.Model):
	"""A Geo Point"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Retrun string rep of this model"""
		return self.text
