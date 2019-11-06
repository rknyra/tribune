from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

class EditorTestClass(TestCase):
    
    #set-up method
    def setUp(self):
        self.stl=Editor(first_name = 'Stl', last_name = 'SuperG', email = 'stl@superg.com')
        
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.stl,Editor))
        
    #testing save method
    def test_save_method(self):
        self.stl.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
        
class ArticleTestClass(TestCase):
    def setUp(self):
        
        #Creating a new editor and saving it
        self.chyle=Editor(first_name = 'Chyle', last_name = 'Ella', email = 'chyle@ella.com')
        self.chyle.save_editor()
        
        #Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()
        
        self.new_article = Article(title = 'Test Article', post = 'This is a random post', editor = self.chyle)
        self.new_article.save()
        
        self.new_article.tags.add(self.new_tag)
        
    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
        
    
    def test_get_news_today(self):
        today_news = Article.today_news()
        self.assertTrue(len(today_news)>0)
    
    def test_get_news_by_date(self):
        test_date = '2019-11-04'
        date = dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
    
    
    