from django.shortcuts import render, get_object_or_404


from .models import News, Category, Tag

# Create your views here.


def news_list(request):
    news = News.objects.all()
    cat = Category.objects.all()
    tag = Tag.objects.all()
    return render(
        request,
        "blog/news.html",
        context={"news_list": news, "news": news, "cat": cat, "tag": tag},
    )


def index(request):
    news_list = News.objects.all()
    return render(request, "index.html", {"news_list": news_list})


def news_detail(request, id):
    news = News.objects.get(id=id)
    cat = Category.objects.all()
    view = get_object_or_404(News, id=id)
    view.views += 1
    view.save()
    return render(request, "blog/news_detail.html", context={"news": news,"cat":cat,'view':view})

# def news_by_category(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     news = News.objects.get(category=category)
#     return render(request, 'blog/news_by_category.html', {
#         'category': category,
#         'news_list': news
#     })
