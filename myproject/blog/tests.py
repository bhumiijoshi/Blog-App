from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Author, BlogPost, Comment


class ModelsObjectNameTests(TestCase):

    def test_models_has_expected_obj_name(self):
        test_user = User.objects.create(username="test_user", password="test878")
        author = Author.objects.create(
            name="Test Author", user=test_user, biological_info="test info"
        )
        blog = BlogPost.objects.create(
            title="Test Title", author=author, content="This is content"
        )
        comment = Comment.objects.create(
            user=test_user, blog=blog, comment="This is comment"
        )
        self.assertEqual(str(blog), "Test Title")
        self.assertEqual(str(comment), "This is comment")
        self.assertEqual(str(author), "Test Author")


class AuthorModelsField(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username="testuser1", password="12345")
        test_user1.save()
        Author.objects.create(
            user=test_user1, name="test_author", biological_info="This is a bio"
        )

    def test_user(self):
        author = Author.objects.get(id=1)
        test_user = User.objects.get(id=1)
        self.assertEqual(author.user, test_user)

    def test_name(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.name, "test_author")

    def test_biological(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.biological_info, "This is a bio")


class BlogPostModelsFieldLabel(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username="testuser1", password="12345")
        test_user1.save()
        test_author = Author.objects.create(
            user=test_user1, name="test_author", biological_info="This is a bio"
        )
        test_author.save()
        BlogPost.objects.create(
            author=test_author, title="Test_title", content="this is a content"
        )

    def test_author(self):
        post = BlogPost.objects.get(id=1)
        test_author = Author.objects.get(id=1)
        self.assertEquals(post.author, test_author)

    def test_title(self):
        post = BlogPost.objects.get(id=1)
        self.assertEquals(post.title, "Test_title")

    def test_content(self):
        post = BlogPost.objects.get(id=1)
        self.assertEquals(post.content, "this is a content")


class CommentModelsFieldLabel(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username="testuser1", password="12345")
        test_user1.save()
        test_author = Author.objects.create(
            user=test_user1, name="test_author", biological_info="This is a bio"
        )
        test_author.save()
        test_post = BlogPost.objects.create(
            author=test_author, title="Test_title", content="this is a title"
        )
        test_post.save()

        Comment.objects.create(
            user=test_user1, blog=test_post, comment="this is comment"
        )

    def test_user(self):
        comment = Comment.objects.get(id=1)
        user = User.objects.get(id=1)
        self.assertEquals(comment.user, user)

    def test_blog(self):
        comment = Comment.objects.get(id=1)
        blog = BlogPost.objects.get(id=1)
        self.assertEquals(comment.blog, blog)

    def test_comment(self):
        comment = Comment.objects.get(id=1)
        self.assertEquals(comment.comment, "this is comment")


class BlogListViewTestCase(TestCase):

    def test_view_url_accessible_by_location(self):
        url = "/blog/blogs/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("blog:blog_list"))
        self.assertEqual(response.status_code, 200)

    def test_view_url_uses_expected_template(self):
        response = self.client.get(reverse("blog:blog_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/bloglist.html")

    def test_view_url_record_paginated_by_5(self):
        user = User.objects.create(username="test_user", password="test12345")
        author = Author.objects.create(
            name="test_author", user=user, biological_info="Test content"
        )
        for i in range(7):
            BlogPost.objects.create(
                title=f"Test Post {i}", content=f"Test Content {i}", author=author
            )

        response = self.client.get(reverse("blog:blog_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["blogs"]), 5)
