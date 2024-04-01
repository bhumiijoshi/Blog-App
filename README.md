# Blogs
User can read blogs, write blogs and also can comment on blogs.
---
## Screenshots
### Homepage
![Screenshot 2024-04-01 at 6 03 21 PM](https://github.com/bhumiijoshi/Blog-App/assets/160118977/e9bd1a26-0780-49fc-a65f-3dca48b2a3a5)
### Blog List
![Screenshot 2024-04-01 at 5 59 23 PM](https://github.com/bhumiijoshi/Blog-App/assets/160118977/2de57027-442c-4261-84c3-b7d7102e6f8e)
### Post
![Screenshot 2024-04-01 at 6 04 46 PM](https://github.com/bhumiijoshi/Blog-App/assets/160118977/e9832291-e52c-4125-8169-bf0780e22cae)
### Author Detail
![Screenshot 2024-04-01 at 6 06 12 PM](https://github.com/bhumiijoshi/Blog-App/assets/160118977/c5f63cb5-16c1-4360-b822-a8d51dd85be4)
### Author Profile
![Screenshot 2024-04-01 at 6 09 16 PM](https://github.com/bhumiijoshi/Blog-App/assets/160118977/0fbbac3d-e860-47e2-8d47-025091459f1d)
---
### Functions

### Reader
- An individual can read all blogs with the detail of it's post date and author who post that blog.
- User can read about author's detail and all the post author has posted.
- After login user can add a comment on blog page.
- A logged in user can become an author after creating author profile.

### Author
- After creating an author profile user can add, update and delete his/her posts.
---

## HOW TO RUN THIS PROJECT
- Install Python(3.8.9) (Dont Forget to Tick Add to Path while installing Python)
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :

```
python3 -m pip install -r requirements. txt
```

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/blog/
```
- To access admin site run the following command :

```
py manage.py createsuperuser
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/admin/
```
---