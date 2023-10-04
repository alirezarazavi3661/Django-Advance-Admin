from django.db import models




class Post(models.Model):
    """
    this is a class to define posts for Blog app
    """
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    status = models.BooleanField()
    category = models.ForeignKey("category",on_delete=models.SET_NULL,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    def __str__(self):
        return self.title





class Category(models.Model):
    """
    this is a class to define categories
    """
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name