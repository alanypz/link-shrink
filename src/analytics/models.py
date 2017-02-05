from django.db import models
from shortener.models import AnyzURL


class ClickEventManager(models.Manager):
	def create_event(self, instance):
		if isinstance(instance, AnyzURL):
			obj, created = self.get_or_create(anyz_url=instance)
			obj.count += 1
			obj.save()
			return obj.count
		return None

class ClickEvent(models.Model):
	anyz_url 	= models.OneToOneField(AnyzURL)
	count 		= models.IntegerField(default=0)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)