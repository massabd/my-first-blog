from django.conf import settings
from django.db import models
from django.utils import timezone

# Double-check that you use two underscore characters (_) on each side of str. 
# This convention is used frequently in Python and sometimes we also call them "dunder" 
# (short for "double-underscore").

# Methods often return something. There is an example of that in 
# the __str__ method. In this scenario, when we call __str__() we will get 
# a text (string) with a Post title.

# Also notice that both def publish(self): and def __str__(self): 
# are indented inside our class. Because Python is sensitive to whitespace,
# we need to indent our methods inside the class. Otherwise, the methods won't 
# belong to the class, and you can get some unexpected behavior.



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



