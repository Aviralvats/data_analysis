from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm,userRegisterationForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

#.means:
#“look inside the current app folder”
# Create your views here.



def index(request):
    return render(request,'index.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})
@login_required
def tweet_create(request):
    if request.method=="POST":
        form=TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
        pass
    else:
        form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})
@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=="POST":
       form=TweetForm(request.POST,request.FILES,instance=tweet)
       if form.is_valid():
           tweet=form.save(commit=False)
           tweet.user=request.user
           tweet.save()
           return redirect('tweet_list')


    
       pass

    else:
        form=TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})
@login_required
def delete_tweet(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})
#POST is an HTTP method used to send data to the server.
def register(request):
    if request.method=='POST':
        form=userRegisterationForm(request.POST) 
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form=userRegisterationForm()
            
    return render(request,'registration/register.html',{'form':form})





      



