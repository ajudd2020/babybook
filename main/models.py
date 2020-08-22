from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime, date
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class BabyBookEntry (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length= 200)
    main_image = models.ImageField(null=True, blank=True, upload_to="images/")
    entry = RichTextField(blank=True, null=True, max_length=2000)
    #entry = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    image_caption = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request,obj,form,change)
    

    def get_absolute_url(self):
        return reverse('view_book')
        #return reverse('article-detail', args=(str(self.id)))


