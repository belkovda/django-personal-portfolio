from django.db import models

class Blog(models.Model):
    post_title = models.CharField(max_length=200)
    date = models.DateField()
    blog_text = models.TextField(max_length=250)
    
    def __str__(self):
        return self.post_title