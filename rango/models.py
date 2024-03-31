from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    max_name_length = 128
    name = models.CharField(max_length=max_name_length, unique=True)
    views = models.IntegerField(default=0)
    likes= models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    max_title_length = 128
    max_url_length = 200
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=max_title_length)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    '''
    For fields website and picture, we have set blank=True for both. This allows
    each of the fields to be blank if necessary, meaning that users do not have to supply
    values for the attributes.
    '''
    def __str__(self):
        return self.user.username