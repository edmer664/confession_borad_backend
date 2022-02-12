from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from api.models import Post
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_posts(request):
    posts = Post.objects.all()
    json_posts = [{
        'id': post.id,
        'title': post.title,
        'body': post.body,
        'pub_date': post.pub_date,
        'author': post.author,
        'updated_at': post.updated_at
    } for post in posts]
    return JsonResponse(json_posts, safe=False)

@csrf_exempt
def make_post(request):
    data = {
        'title': request.POST['title'],
        'body': request.POST['body'],
        'author': request.POST['author'],
    }
    post = Post(
        title=data['title'],
        body=data['body'],
        author=data['author'],
    )
    post.save()
    return redirect(request.META.get('HTTP_REFERER') + '/home')
    
def get_post(request,post_id):
    post = Post.objects.get(id=post_id)
    json_post = {
        'id': post.id,
        'title': post.title,
        'body': post.body,
        'pub_date': post.pub_date,
        'author': post.author,
        'updated_at': post.updated_at
    }
    return JsonResponse(json_post, safe=False)
    