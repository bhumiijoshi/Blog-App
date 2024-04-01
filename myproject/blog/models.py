from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, related_name = "author")
    name = models.CharField(max_length=50)
    biological_info = models.TextField()

    class Meta:
        db_table = "authors"

    def __str__(self):
        return self.name

class BlogPost(BaseModel):
    title = models.TextField(default="No title available")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = "blogs")
    content = models.TextField()
    
    class Meta:
        db_table = "blog_post"
        
    def __str__(self):
        return self.title
    
class Comment(BaseModel):
    user = models.ForeignKey(User,on_delete = models.CASCADE, default=None, related_name = "created_comments")                 
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE,  related_name = "comments")
    comment = models.TextField()
    
    class Meta:
        db_table = "comments"
    
    def __str__(self):
        comment_length = settings.DEFAULT_COMMENT_LENGTH
        if len(self.comment) > comment_length:
            return self.comment[:comment_length] + "..."
        else:
            return self.comment