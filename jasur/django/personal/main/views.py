from django.shortcuts import render
from main.models import *
from datetime import datetime
from django.db.models import Q
import smtplib as smtp
import urllib.parse
import socket
# Create your views here.

def indexHandler(request):
    services = Service.objects.all()
    plans = Plan.objects.all()
    projects = Project.objects.all()
    projects_types = ProjectType.objects.all()
    coments = Comment.objects.all()[:2]
    posts = Post.objects.all()[:3]
    posts_authors = PostAuthor.objects.all()
    posts_category = PostCategory.objects.all()
    partners = Partner.objects.all()
    other_item = Others.objects.all()[0]

    post_author = []
    for abc in posts_authors:
        new_abc = {
            'id': abc.id,
            'author': abc,
            'count': Post.objects.filter(postauthor__id=int(abc.id)).count()
        }
        post_author.append(new_abc)
        print(new_abc)

    postauthor_sorted = sorted(post_author, key=lambda k: k['count'], reverse=True)
    chel1 = postauthor_sorted[0]
    chel2 = postauthor_sorted[1]
    print(postauthor_sorted)
    return render(request, 'index.html', {'services':services,
                                          'plans': plans,
                                          'projects': projects,
                                          'projects_types': projects_types,
                                          'coments':coments, 'posts':posts,
                                          'posts_authors':posts_authors,
                                          'posts_category':posts_category,
                                          'partners':partners,
                                          'chel1':chel1,
                                          'chel2':chel2,
                                          'other_item':other_item

                                          })

def personsHandler(request):
    return render(request, 'index.html', {})

def aboutHandler(request):
    coments = Comment.objects.all()[:2]
    partners = Partner.objects.all()
    expertnesss1 = Experience.objects.all()[0::2]
    expertnesss2 = Experience.objects.all()[1::2]
    other_item = Others.objects.all()[0]
    qualific = Qualification.objects.all()
    return render(request, 'about.html',{'coments':coments, 'qualific':qualific, 'partners':partners, 'other_item':other_item, 'expertnesss1':expertnesss1, 'expertnesss2':expertnesss2})
def serviceitemHandler(request, servis_id):
    servis = Service.objects.get(id=int(servis_id))
    return render(request, 'serviceitem.html', {'servis': servis})

def serviceHandler(request):
    services = Service.objects.all()
    plans = Plan.objects.all()
    coments = Comment.objects.all()[:2]
    other_item = Others.objects.all()[0]
    return render(request, 'service.html',{'services':services, 'other_item':other_item, 'plans': plans, 'coments':coments})

def portifolioHandler(request):
    projects = Project.objects.all()
    projects_types = ProjectType.objects.all()
    other_item = Others.objects.all()[0]
    return render(request, 'portifolio.html',{'projects': projects,'other_item':other_item, 'projects_types': projects_types})


def pricingHandler(request):
    plans = Plan.objects.all()
    faqs = FAQ.objects.all()
    other_item = Others.objects.all()[0]
    return render(request, 'pricing.html',{'plans': plans, 'other_item':other_item, 'faqs':faqs})

def blogHandler(request):
    search_value = request.GET.get('search', None)
    author_id = request.GET.get('author_id', None)
    category_id = request.GET.get('category_id', None)


    current_page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 3))
    stop = current_page * limit
    start = stop - limit


    total = Post.objects.count()
    prev_page = current_page - 1
    next_page = 0
    if total > stop:
        next_page = current_page + 1


    # SUBCRIBE
    if request.POST:
        email = request.POST.get('email', '')
        pochta = Podpischiki()
        email_pod = Podpischiki.objects.filter(email=email)
        if not email_pod:
            pochta.email = email
            pochta.save()

    posts_author = PostAuthor.objects.all()[:1][0]
    news = PostCategory.objects.all()[:3]
    if search_value:
        posts = Post.objects.filter(title__contains=search_value)
    else:
        if author_id:
            posts = Post.objects.filter(postauthor__id=int(author_id))
            posts_author = PostAuthor.objects.get(id=int(author_id))
        else:
            if category_id:
                posts = Post.objects.filter(postcategory__id=int(category_id))
            else:
                posts = Post.objects.all()[start:stop]

    posts1 = Post.objects.all()[:3]
    posts_category = PostCategory.objects.all() # [{'id':1, 'title':sport}, {'id':2, 'title':sport}]
    post_categories = []
    for pc in posts_category:
        new_pc = {
            'id': pc.id,
            'title': pc.title,
            'logo': pc.logo,
            'count': Post.objects.filter(postcategory__id=int(pc.id)).count()
        }
        post_categories.append(new_pc)
        print(new_pc)

    pages_count = int(total / limit)
    if total % limit > 0:
        pages_count += 1
    pages = range(1, pages_count + 1)

    other_item = Others.objects.all()[0]
    return render(request, 'blog.html',{'news':news, 'posts':posts,
                                        'posts1':posts1, 'posts_author':posts_author,
                                        'posts_category':post_categories, 'current_page':current_page,
                                        'prev_page':prev_page, 'next_page':next_page,
                                        'limit':limit, 'pages':pages, 'other_item':other_item,
                                        })

def blog_singleHandler(request, blog_id):
    if request.POST:
        print('****'*10)
        print(request.POST)
        new_post_comment = Comment()
        new_post_comment.name_author = request.POST.get('name_author','')
        new_post_comment.email = request.POST.get('email', '')
        new_post_comment.comment_id = int(request.POST.get('comment_id', 0))
        new_post_comment.subject = request.POST.get('subject', '')
        new_post_comment.text = request.POST.get('text', '')
        new_post_comment.pub_date = datetime.now()
        new_post_comment.post = Post.objects.get(id=int(blog_id))
        new_post_comment.save()

    blogpost = Post.objects.get(id = int(blog_id))
    blogpost.show_count = blogpost.show_count + 1
    blogpost.save()




    if blog_id > 1:
        prevpost = Post.objects.get(id=int(blog_id)-1)
    else:
        prevpost = Post.objects.all().order_by('-id')[:1][0]

    blog_count = Post.objects.all().count()
    print(blog_count)
    if int(blog_id) != blog_count:
        nextpost = Post.objects.get(id=int(blog_id)+1)
    else:
        nextpost = Post.objects.get(id=1)

    posts1 = Post.objects.all()[:3]
    posts = Post.objects.all()
    posts_authors = PostAuthor.objects.all()
    posts_category = PostCategory.objects.all()


    comments = Comment.objects.filter(post__id=int(blog_id)).order_by('id')
    comments_count = len(comments)
    new_comments = []
    for com in comments:
        if com.comment_id == 0:
            new_comment = {
                "id": com.id,
                "orig_comment": com,
                "replies": []
            }
            new_comments.append(new_comment)
        else:
            for c in new_comments:
                if c["id"] == com.comment_id:
                    c["replies"].append(com)
    
    return render(request, 'blog-single.html',{'posts':posts, 'posts_authors':posts_authors,
                                               'posts_category':posts_category, 'comments':comments,
                                               'blogpost':blogpost,
                                                'posts1':posts1,
                                               'prevpost':prevpost,
                                               'nextpost':nextpost,
                                               'comments_count':comments_count,
                                               'new_comments':new_comments

                                               })

def elementsHandler(request):
    return render(request, 'elements.html',{})

def pagesHandler(request):
    return render(request, 'pages.html',{})

def contactHandler(request):
    other_item = Others.objects.all()[0]

    if request.POST:
        new_contact = Podpischiki()
        new_contact.name = request.POST.get('name', '')
        new_contact.email = request.POST.get('email', '')
        new_contact.subject = request.POST.get('subject', '')
        new_contact.message = request.POST.get('message', '')
        new_contact.save()




        email = 'zhtursimatov@yandex.ru'
        password = 'jas0910t'
        dest_email = ['m_mirzafar@mail.ru']
        subject = new_contact.subject
        email_text = f'message:{new_contact.message}\n email:{new_contact.email}\n name:{new_contact.name}'



        message = 'From: {}\nSubject: {}\n\n{}'.format(email, subject, email_text)

        server = smtp.SMTP_SSL('smtp.yandex.com')
        server.set_debuglevel(1)
        server.ehlo(email)
        server.login(email, password)
        server.sendmail(email, dest_email, message)
        server.quit()

        subject = 'RAHMAT'
        email_text = f'Sizning zaprosingiz qabullandi'

        message = 'From: {}\nSubject: {}\n\n{}'.format(email, subject, email_text)

        server = smtp.SMTP_SSL('smtp.yandex.com')
        server.set_debuglevel(1)
        server.ehlo(email)
        server.login(email, password)
        server.sendmail(email, [new_contact.email], message)
        server.quit()






    return render(request, 'contacts.html',{'other_item':other_item})




def studentsHandler(request):
    dtn = datetime.now()
    search = request.GET.get('search','')
    if search:
        students = Student.objects.filter((Q(last_name__contains=search) |
                                           Q(first_name__contains=search) |
                                           Q(midle_name__contains=search)) &
                                          (Q(rate_orta__gt = 80)))
        # students = Student.objects.filter(Q(birth_date__lt=dtn))
    else:
        students = Student.objects.all()
    return render(request, 'students.html',{'students':students,
                                            'search':search
                                            })





def baseHandler(request):
    # SUBCRIBE
    if request.POST:
        email = request.POST.get('email', '')
        pochta = Podpischiki()
        email_pod = Podpischiki.objects.filter(email=email)
        if not email_pod:
            pochta.email = email
            pochta.save()

    other_item = Others.objects.all()[0]

    return  render(request, 'base.html', {'other_item':other_item})


