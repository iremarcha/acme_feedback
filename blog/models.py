from django.db import models
from django.utils import timezone
from users.models import CustomUser
#v10
from django_project import settings
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#SI SE ELIMINA UN AUTHOR SE ELIMINAN SUS POSTS

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
