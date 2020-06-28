from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.shortcuts import render

from newsletter.models import Signup
from .models import Post


def get_category_count():
    queryset = Post.objects.values("categories__title").annotate(Count("categories"))
    return queryset


def search(request):
    query = request.GET.get("q")
    queryset = Post.objects.filter(
        Q(title__icontains=query) | Q(overview__icontains=query)
    ).distinct()
    return render(request, "blog/search_result.html", {"queryset": queryset})


def home(request):
    if request.method == "POST":
        email = request.POST.get("email")
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    context = {
        "post_featured": Post.objects.filter(featured=True),
        "latest_post": Post.objects.order_by("-created")[:3],
    }
    return render(request, "blog/home.html", context)


def blog(request):
    category_count = get_category_count()
    recent_post = Post.objects.order_by("-created")[:3]
    paginator = Paginator(Post.objects.all(), 4)
    page_num = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    return render(
        request,
        "blog/blog.html",
        {
            "page_obj": page_obj,
            "recent_post": recent_post,
            "category_count": category_count,
        },
    )


def post(request, id):
    return render(request, "blog/post.html")
