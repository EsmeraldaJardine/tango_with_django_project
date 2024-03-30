from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    max_name_length = 128
    name = models.CharField(max_name_length, unique=True)
    views = models.IntegerField(default=0)
    likes= models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        """
        The `save` method is being overridden in `Category` to 
         add custom behavior before the instance of the model is saved to the database.
         In this case, before saving the `Category` instance, the `name` attribute
         is being slugified and assigned to the `slug` attribute. 
         By slugifying the `name` attribute and saving it as `slug`, you ensure 
         that each category has a URL-friendly identifier that can be used in routing and linking.
         The `super(Category, self).save(*args, **kwargs)` line is calling the original `save` method
         from the parent class (in this case, likely the Django `Model` class), which handles the actual 
         saving of the object to the database. This is done after the slugification to ensure that the updated `slug` is the one that gets stored.
        """
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    max_title_length = 128
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_title_length)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

