from django.shortcuts import render,redirect,HttpResponse
from .models import Post,Comment,SavePost
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('date')
    rem = len(posts)//3
    old_post = posts[:len(posts)-rem+1]
    old_post.reverse()
    recent_post = posts[len(posts)-rem+1:len(posts)]
    recent_post.reverse()
    user = None
    user_auth = request.user.is_authenticated
    if user_auth:
        user = request.user
    return render(request,'posts/posts_list.html',{'old_post':old_post,'user':user,'recent_post':recent_post})

def Post_detail(request,name):
    post = Post.objects.get(title=name)
    comments = Comment.objects.filter(post=post)
    new_comment = None
    save_post = False
    form = forms.CommentForm()
    user_commented = Comment.objects.filter(name=request.user, post=post)
    user_saved_post = 0
    user_auth = request.user.is_authenticated

    if user_auth:
        user_saved_post = len(SavePost.objects.filter(user=request.user, post=post))
        form = None
    elif not user_auth:
        form = None

    if len(user_commented) == 0 and user_auth:
        form = forms.CommentForm()

    if 'save' in request.POST:
        savepost = SavePost()
        savepost.user = request.user
        savepost.post = post
        savepost.title = post.title
        savepost.save()
        save_post = True

    elif request.method=='POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user
            new_comment.save()
            form = None


    return render(request,'posts/post_detail.html',{'post':post,'comments':comments,'new_comment':new_comment,'form':form,"save_post":save_post,'user_auth':user_auth,'saved_post':user_saved_post})

@login_required(login_url="/accounts/Login/")
def post_create(request):
    if request.method=="POST":
        form = forms.CreatePost(request.POST,request.FILES)
        if form.is_valid():
            # save to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request,'posts/post_create.html',{'form':form})

@login_required(login_url="/accounts/Login/")
def saved_post(request):
    saved_post = SavePost.objects.filter(user=request.user)
    posts = []
    for post in saved_post:
        posts.append(Post.objects.get(title=post.title))
    return render(request,'posts/saved_post.html', {'posts': posts})

def saved_detail(request,name):
    post = Post.objects.get(title=name)
    comments = Comment.objects.filter(post=post)
    return render(request, 'posts/saved_detail.html',
                  {'post': post, 'comments': comments})

def user_post(request):
    userpost = Post.objects.filter(author=request.user)
    return render(request,'posts/user_post.html', {'posts': userpost})

def user_post_detail(request,name):
    post = Post.objects.get(title=name)
    comments = Comment.objects.filter(post=post)
    return render(request, 'posts/user_post_detail.html',
                  {'post': post, 'comments': comments})

def user_post_edit(request,name):
    post = Post.objects.get(title=name)
    if 'save' in request.POST:
        form = forms.CreatePost(request.POST,request.FILES,instance=post)
        if form.is_valid():
            # save to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost(instance=post)
    return render(request,'posts/user_post_edit.html',{'form':form,'name':name})
