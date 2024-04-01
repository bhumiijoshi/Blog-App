from django.test import TestCase
from .models import Author, Comment, BlogPost
from django.contrib.auth.models import User
from django.urls import reverse

class ModelsObjectNameTests(TestCase):
    
    def test_models_has_expected_obj_name(self):
        test_user = User.objects.create(username="test_user",password="test878")
        author = Author.objects.create(name="Test Author",user=test_user,biological_info="test info")
        blog = BlogPost.objects.create(title="Test Title",author = author, content= "This is content")
        comment = Comment.objects.create(user=test_user,blog=blog,comment="This is comment" )
        self.assertEqual(str(blog),"Test Title")
        self.assertEqual(str(comment),"This is comment")
        self.assertEqual(str(author), "Test Author")
        
class AuthorModelsFieldLabel(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        Author.objects.create(user=test_user1,name="test_author",biological_info='This is a bio')
        
    def test_user_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('user').verbose_name
        self.assertEquals(field_label,'user')
        
    def test_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')
        
    def test_biological_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('biological_info').verbose_name
        self.assertEquals(field_label,'biological info')
        
class BlogPostModelsFieldLabel(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        test_author = Author.objects.create(user=test_user1,name="test_author",biological_info='This is a bio')
        test_author.save()
        BlogPost.objects.create(author=test_author,title="Test_title",content="this is a title")
        
    def test_author_label(self):
        post=BlogPost.objects.get(id=1)
        field_label = post._meta.get_field('author').verbose_name
        self.assertEquals(field_label,'author')
        
    def test_title_label(self):
        post=BlogPost.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')
        
    def test_content_label(self):
        post=BlogPost.objects.get(id=1)
        field_label = post._meta.get_field('content').verbose_name
        self.assertEquals(field_label,'content')

class CommentModelsFieldLabel(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        test_author = Author.objects.create(user=test_user1,name="test_author",biological_info='This is a bio')
        test_author.save()
        test_post = BlogPost.objects.create(author=test_author,title="Test_title",content="this is a title")
        test_post.save()
        comment="this is comment"*80
        Comment.objects.create(user=test_user1,blog=test_post,comment=comment)
        
    def test_user_label(self):
        comment=Comment.objects.get(id=1)
        field_label = comment._meta.get_field('user').verbose_name
        self.assertEquals(field_label,'user')
        
    def test_blog_label(self):
        comment=Comment.objects.get(id=1)
        field_label = comment._meta.get_field('blog').verbose_name
        self.assertEquals(field_label,'blog')
        
    def test_comment_label(self):
        comment=Comment.objects.get(id=1)
        field_label = comment._meta.get_field('comment').verbose_name
        self.assertEquals(field_label,'comment')
              
class BlogListViewTestCase(TestCase):
            
    def test_view_url_accessible_by_location(self):
        url = '/blog/blogs/'  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blog:blog_list'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_url_uses_expected_template(self):
        response = self.client.get(reverse('blog:blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'blog/bloglist.html')
        
    def test_view_url_record_paginated_by_5(self):
        user = User.objects.create(username='test_user', password='test12345')
        author = Author.objects.create(name="test_author", user=user,biological_info="Test content")
        for i in range(7):
            BlogPost.objects.create(title=f'Test Post {i}', content=f'Test Content {i}', author=author)

        response = self.client.get(reverse("blog:blog_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['blogs']), 5)