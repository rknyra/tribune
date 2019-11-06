from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import datetime as dt

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)
    
    # try:
    #     editor = Editor.objects.get(email = 'stl@superg.com')
    #     print('Editor found')
    # except ObjectDoesNotExist:
    #     print('Editor was not found')
    
    def __str__(self):
        return self.first_name
    def save_editor(self):
        self.save()
        
    class Meta:
        ordering = ['first_name']


class tags(models.Model):
    name = models.CharField(max_length =30)
    
    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articles/', default='image.png')
    
    @classmethod
    def today_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
    
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
    
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    
    
    def __str__(self):
        return self.title