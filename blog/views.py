from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post, ContactMessage

def index(request):
    """Main portfolio page"""
    from resume.models import Experience, Education, Certificate
    
    # Handle contact form submission
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('/#contact')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    recent_posts = Post.objects.filter(published=True)[:3]
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    certificates = Certificate.objects.all()
    
    context = {
        'recent_posts': recent_posts,
        'experiences': experiences,
        'educations': educations,
        'certificates': certificates,
    }
    return render(request, 'index.html', context)

def blog_list(request):
    """Blog listing page"""
    posts = Post.objects.filter(published=True)
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    """Individual blog post page"""
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog_detail.html', {'post': post})