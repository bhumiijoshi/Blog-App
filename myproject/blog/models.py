from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Authors(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50)
    biological_info = models.TextField()

    class Meta:
        db_table = "authors"

    def __str__(self):
        return self.name

class BlogPost(BaseModel):
    title = models.TextField(default="No title available")
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name = "authors")
    content = models.TextField()
    
    class Meta:
        db_table = "blog_post"
        
    def __str__(self):
        return self.title
    
class Comment(BaseModel):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE,  related_name = "blogs")
    comment = models.TextField()
    
    class Meta:
        db_table = "comment"
    
    def __str__(self):
        return self.comment