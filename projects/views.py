from urllib.parse import unquote

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages

from projects.models import Department, Topic, Transaction, Paystack
from utils import helper


def projects(request, department):
    departments = Department.objects.all()
    # paginator = Paginator(category_list, 1)

    try:
        page = request.GET['page']
    except:
        page = 1

    # Try fetching the department passed in the  url
    department = department.replace('-', ' ')
    department = Department.objects.filter(name__iexact=department).first()

    # Invalid department passed, use default
    if not department:
        return redirect('projects', department='accounting')
       
    topics = Topic.objects.filter(department=department)

    paginator = Paginator(topics, per_page=50)
    page_object = paginator.get_page(page)
    page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
   
    context = {
        "page": 'projects',
        "department": department,
        "departments": departments,
        "count": paginator.count,
        "page_obj": page_object,
    }
    
    # if helper.refresh_data():
    #     return refresh_content(request)
        
    return render(request, "projects/pages/projects.dj", context)


def project(request, department, topic):
    paystack = Paystack.objects.all().first()
    
    departments = Department.objects.all()
    # paginator = Paginator(category_list, 1)
        
    # Try fetching the department passed in the  url
    department = department.replace('-', ' ')
    department = Department.objects.filter(name__iexact=department).first()
    
    topic = topic.replace('-', ' ').replace('symeorsign', '/').replace('symedashsign', '-')
    
    topic = Topic.objects.filter(department=department, title__iexact=unquote(topic)).first()

    if topic:
        related_topics = list(set(Topic.objects.filter(tags__name__in=[tag.name for tag in topic.tags.all()])))
        related_topics.remove(topic)
        
    # Invalid department or topic passed, use default
    if not department or not topic:
        topic = Topic.objects.all().order_by('title').first()

        if topic:
            topic = topic.title
            return redirect('project', department='accounting', topic=topic.lower())
        else:
            return redirect('home')

    context = {
        "page": 'project',
        "department": department,
        "departments": departments,
        "topic": topic,
        "count": Topic.objects.filter(department=department).count(),
        "related_topics": related_topics,
        "paystack_pk": paystack.public_key,
    }
    
    # if helper.refresh_data():
    #     return refresh_content(request)
        
    return render(request, "projects/pages/project.dj", context)
    
    
def refresh_content(request):
    context = {}
    return render(request, "core/pages/refresh.dj", context)
    

def payment(request, department, topic, firstName, lastName, email, phone, selected, referrer, amount, reference):
    department = department.replace('-', ' ')
    department = Department.objects.filter(name__iexact=department).first()

    topic = topic.replace('-', ' ')
    topic = Topic.objects.filter(department=department, title__iexact=topic).first()
    
    if selected == 'default':
        selected = 'Default'
    elif selected == 'social':
        selected = 'Social media (e.g. Facebook, Twitter, Instagram)'
    elif selected == 'search':
        selected = 'Online search (e.g. Google, Bing)'
    elif selected == 'person':
        selected = 'A friend or family member'
    elif selected == 'ads':
        selected = 'A local event or advertisement'
    elif selected == 'newsletter':
        selected = 'A newsletter or email marketing campaign'
    elif selected == 'commercial':
        selected = 'A radio or television commercial'
    elif selected == 'mag':
        selected = 'A newspaper or magazine advertisement'
    else:
        selected = 'Other'

    Transaction.objects.create(topic=topic, first_name=firstName, last_name=lastName, email=email, phone=phone, paid=amount, where_heard=selected, referrer_phone=referrer, reference=reference)
    messages.success(request, "Payment completed successfully! Project materials will be sent to your email shortly." )
    
    department = department.name
    topic = topic.title
    
    # if helper.refresh_data():
    #     return refresh_content(request)
        
    return redirect('project', department=department.lower(), topic=topic.lower())
