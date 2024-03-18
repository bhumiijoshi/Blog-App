from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        db_table = "base_model"

class Author(BaseModel):
    name = models.CharField(max_length=50)
    biological_info = models.TextField()
    
    class Meta:
        db_table = "author"
        
    def __str__(self):
        return self.name
    
class BlogPost(BaseModel):
    blog_title = models.CharField(max_length=200)
    post_date = models.DateTimeField("date posted")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    
    class Meta:
        db_table = "blog_post"
        
    def __str__(self):
        return self.blog_title
    
class Comment(BaseModel):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_post_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    
    class Meta:
        db_table = "comment"
    
    def __str__(self):
        return self.comment
    
    
    

