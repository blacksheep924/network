from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import newPost
from .models import NewPost, Profile
from django.http import JsonResponse
import json
from .models import User
from django.core.paginator import Paginator
from django.views.generic import ListView


def index(request):
    

    if request.user.is_authenticated:
        
        
        
        form = newPost
                 
            
            
            
            
        if request.method == "POST":

            form = newPost(request.POST)

            if form.is_valid():
                user = request.user
                new_post = NewPost(
                    poster = user,
                    postContent = form.cleaned_data['content']
                    
                )
                new_post.save()

            
                
        return render(request, "network/index.html",{'form' : form})
    else:
        

        return render(request, "network/login.html")
    
def all_posts(request):

    posts = NewPost.objects.all().order_by("timestamp").values()
    p = Paginator(posts, 10)

    
    return render(request, "network/index.html")



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def listing(request):
    post_list = NewPost.objects.all().order_by('-timestamp')
    paginator = Paginator(post_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'network/listing.html',{'page_obj' : page_obj})

def profile(request,profilename):
    
    user  = User.objects.get(username = profilename)
    name = str(user)
    posts_list = NewPost.objects.filter(poster = user).order_by('-timestamp')
    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    followers = Profile.objects.all()
    number_of_follower = []
    for follower in followers:
        if profilename in follower.profile.username and follower.followed == True :
            number_of_follower.append(follower)
        if request.user.username in follower.profile.username and follower.followed == True :
            followed = request.user.username
        else:
            followed = follower.followed
            
    
    number = len(number_of_follower)
    
        

    
    return render(request , "network/profile.html", {'profilename': profilename, 'page_obj' : page_obj, 'name' : name, 'number' : number, 'followed' : followed})

def follow(request, profilename):
    
    
    
    if request.method == "POST":
        
        profile_followed = User.objects.get(username = profilename)
        name = request.user.username
        follower = User.objects.get(username=name)
        followed = True

        if profile_followed == follower:
            return JsonResponse({"message": "you can not follow yourself"}, status=400)
            
        else:
            profile_exist = Profile.objects.filter(profile = profile_followed, follower = follower)
            profile_save = Profile(
                profile = profile_followed,
                follower = follower,
                followed = followed
            )
            if profile_exist :
                profile_exist = Profile.objects.get(profile = profile_followed, follower = follower)
                if profile_exist.followed == True:
                    profile_exist.followed = False
                    profile_exist.save()
                    return JsonResponse({"message" : "User unfollowed"}, status=201)
                else:
                    profile_exist.followed = True

                    profile_exist.save()
                    return JsonResponse({"message" : "User followed"}, status=201)
            
            else:
                profile_save.save()
                
                

           

            return JsonResponse({"message": "User followed"}, status=201)
    
def following(request, profilename):
    user  = User.objects.get(username = profilename)
    name = str(user)
    followed_post = []
    
    followers = Profile.objects.all()
    number_of_follower = []
    for follower in followers:
        if profilename in follower.follower.username and follower.followed == True :
            number_of_follower.append(follower.profile.username)
        if request.user.username in follower.profile.username and follower.followed == True :
            followed = request.user.username
        else:
            followed = follower.followed
            
    
    
    
    posts_list = NewPost.objects.all().order_by('-timestamp')
    for post in posts_list:
        if post.poster.username in number_of_follower:
            followed_post.append(post)
    

    paginator = Paginator(followed_post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    number = len(number_of_follower)
    
        

    
    return render(request ,"network/following.html", {'profilename': profilename, 'page_obj' : page_obj, 'name' : name, 'number' : number, 'followed' : followed, 'number_of_follower' : number_of_follower})
    
    
    








    
        



    

