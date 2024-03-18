from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        db_table = "base_model"

class Author(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
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
    
class Comments(BaseModel):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.TextField()
    
    class Meta:
        db_table = "comments"
    
    def __str__(self):
        return self.comment