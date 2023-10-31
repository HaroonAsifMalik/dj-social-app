from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from post.models import Post ,ResponseAgainstPost
# from django.ren

# Create your views here.
def home_page(request):
    all_post = Post.objects.all()
    all_res = ResponseAgainstPost.objects.all()
    post = Post.objects.get(id=3)
    responses = ResponseAgainstPost.objects.filter(post=post)
    print ( responses[0].comment)

    

    return HttpResponse( "asd")


