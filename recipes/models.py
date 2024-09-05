from django.db import models
from django.shortcuts import reverse, render
from cloudinary.models import CloudinaryField



# Create your models here.



class Recipe(models.Model):
    # class attributes
    ingredients = models.CharField(
        max_length=225, help_text="Enter the ingredients, separated by a comma"
    )
    cooking_time = models.IntegerField(help_text="Enter cooking time in minutes")
    name = models.CharField(max_length=100)
    pic = CloudinaryField('image', default='recipes/no_picture.jpg')
    pic_public_id = models.CharField(max_length=255)  # Store Cloudinary public_id without extension
    pic_format = models.CharField(max_length=10, default='jpg') 


    def difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients.split(',')) < 4:
            return 'easy'
        elif self.cooking_time < 10 and len(self.ingredients.split(',')) >= 4:
            return 'medium'
        elif self.cooking_time >= 10 and len(self.ingredients.split(',')) < 4:
            return 'intermediate'
        elif self.cooking_time >=10 and len(self.ingredients.split(',')) >=4:
            return 'hard'

    def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})

    # string representation
    def __str__(self):
        return str(self.name)
    
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})