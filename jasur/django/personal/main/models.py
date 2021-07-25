from django.db import models
from datetime import datetime
# Create your models here.
class Person(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    mini_description = models.TextField()
    logo = models.ImageField(upload_to='upload', blank=True)
    logo2 = models.ImageField(upload_to='upload', blank=True)
    mini_description2 = models.TextField()

    def __str__(self):
        return self.last_name

class Service(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Information(models.Model):
    title = models.CharField(max_length=200)
    completed_project = models.IntegerField()
    happy_client = models.IntegerField()
    cup_of_coffee = models.IntegerField()
    real_professionals = models.IntegerField()

    def __str__(self):
        return self.title

class ProjectType(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='upload', blank=True)
    projecttype = models.ForeignKey(ProjectType, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Plan(models.Model):
    title = models.CharField(max_length=200, default='title')
    title_info = models.TextField()
    info1 = models.TextField()
    info2 = models.TextField()
    info3 = models.TextField()
    info4 = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Partner(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='upload', blank=True)
    link = models.TextField()

    def __str__(self):
        return self.title

class PostCategory(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='upload', blank=True)
    description = models.TextField(default="description", blank=True)

    def __str__(self):
        return self.title

class PostAuthor(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    fio = models.CharField(max_length=200)
    link = models.TextField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.fio

class Post(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='upload', blank=True)
    description = models.TextField()
    pub_date = models.DateField()
    like_count = models.IntegerField()
    comment_count = models.IntegerField()
    show_count = models.IntegerField()
    description2 = models.TextField()
    postcategory = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    postauthor = models.ForeignKey(PostAuthor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author_logo = models.ImageField(upload_to='upload', blank=True, default='')
    text = models.TextField(max_length=200)
    name_author = models.CharField(max_length=200)
    info_author = models.TextField()
    link_author = models.CharField(max_length=200)
    pub_date = models.DateField(blank=True)
    comment_id = models.IntegerField(default=0)
    email = models.CharField(default='', blank=True, max_length=200)
    subject = models.CharField(default='', blank=True, max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.name_author

class Qualification(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='upload', blank=True)
    date = models.DateField(blank=True)
    result = models.CharField(max_length=200, blank=True)
    session = models.DateField(blank=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=200)
    percent = models.IntegerField()

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    response = models.TextField()
    title = models.CharField(max_length=200, default='title')

    def __str__(self):
        return self.title

class Food(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    title = models.CharField(max_length=200, default='title')
    description = models.TextField()

    def __str__(self):
        return self.title

class New(models.Model):
    logo = models.ImageField(upload_to='upload', blank=True)
    postcategory = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return self.postcategory.title

class Podpischiki(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200,  default='', blank=True)
    subject = models.CharField(max_length=200, default='', blank=True)
    message = models.TextField(blank=True, default='')

    def __str__(self):
        return self.email

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    midle_name = models.CharField(max_length=200, blank=True)
    rate1 = models.IntegerField(blank=True, default=0)
    rate2 = models.IntegerField(blank=True, default=0)
    rate3 = models.IntegerField(blank=True, default=0)
    rate4 = models.IntegerField(blank=True, default=0)
    rate5 = models.IntegerField(blank=True, default=0)
    rate_orta = models.FloatField(blank=True, default=0.0)
    grup_name = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField(blank=True)
    enter_date = models.DateField(blank=True)
    course = models.IntegerField(default=1, blank=True)
    faculty = models.CharField(max_length=300, blank=True)
    citizenship = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.first_name



class Others(models.Model):
    my_offered_services_title = models.TextField(blank=True)
    my_offered_services_desc = models.TextField(blank=True)
    Our_Latest_Featured_Projects = models.TextField(blank=True)
    Our_Latest_Featured_Projects_desc = models.TextField(blank=True)
    Clients_Feedback_About_Me = models.TextField(blank=True)
    Clients_Feedback_About_Me_desc = models.TextField(blank=True)
    choose_your_plan = models.TextField(blank=True)
    choose_your_plan_desc = models.TextField(blank=True)
    Latest_Posts_From_Our_Blog = models.TextField(blank=True)
    Latest_Posts_From_Our_Blog_desc = models.TextField(blank=True)
    my_qualifications = models.TextField(blank=True)
    my_qualifications_desc = models.TextField(blank=True)
    about_me = models.TextField(blank=True)
    about_me_desc = models.TextField(blank=True)
    footer_desc = models.TextField(blank=True)
    footer_newsletter = models.TextField(blank=True)
    footer_newsletter_desc = models.TextField(blank=True)
    footer_follow_me = models.TextField(blank=True)
    footer_follow_me_desc = models.TextField(blank=True)
    Frequently_Asked_Questions = models.TextField(blank=True)
    Frequently_Asked_Questions_desc = models.TextField(blank=True)
    blog_newsletter = models.TextField(blank=True)
    blog_newsletter_desc = models.TextField(blank=True)
    blog_newsletter_desc2 = models.TextField(blank=True)
    tag_clouds = models.TextField(blank=True)
    con_address = models.TextField(blank=True)
    con_address_desc = models.TextField(blank=True)
    con_number = models.TextField(blank=True)
    con_number_desc = models.TextField(blank=True)
    con_mail = models.TextField(blank=True)
    con_mail_desc = models.TextField(blank=True)



    def __str__(self):
        return self.my_offered_services_title

