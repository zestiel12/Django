from django.shortcuts import render, get_object_or_404, redirect

from django import forms
from .models import News, Category, Tag,NewsImage,ImageReplaceForm

# Create your views here.


def news_list(request):
    news = News.objects.filter(is_published=True)
    cat = Category.objects.all()
    tag = Tag.objects.all()

    search = request.GET.get("search", "")
    category_id = request.GET.get("category", "")

    if search:
        news = news.filter(title__icontains=search)

    if category_id:
        try:
            category = Category.objects.get(id=int(category_id))
            news = news.filter(category=category)
        except:
            category = None
    else:
        category = None

    return render(
        request,
        "blog/news.html",
        context={
            "news_list": news,
            "news": news,
            "cat": cat,
            "tag": tag,
            "search": search,
        },
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
    return render(
        request,
        "blog/news_detail.html",
        context={"news": news, "cat": cat, "view": view},
    )


def news_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    news = News.objects.filter(cat=category)
    cat = Category.objects.all()

    return render(
        request,
        "blog/news.html",
        context={"news": news, "cat": cat, "selected_category": category},
    )


def creat_news(request):
    cat = Category.objects.all()
    tag = Tag.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")

    context = {
        "cats": cat,
        "tags": tag,
    }

    return render(request, "blog/create_news.html", context)


def creat_tag(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Tag.objects.create(name=name)
            return redirect("creat_tag")

    tags = Tag.objects.all()
    return render(request, "blog/creat_tag.html", {"tags": tags})


def creat_category(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Category.objects.create(title=title)
            return redirect("creat_category")

    categories = Category.objects.all()
    return render(request, "blog/creat_category.html", {"categories": categories})


def change_news(request,id):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    news = News.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get("title",news.title)
        cat = request.POST.get("cat")
        tag = request.POST.get("tag")
        description = request.POST.get("description")
        author = request.POST.get("author")
        is_published = request.POST.get("is_published")
        news.title=title,
        news.cat=cat,
        news.tag.clear()
        news.tag.set(tag),
        news.description=description,
        news.author=author,
        news.is_published=is_published,
        news.save()

        return redirect("news_detail")
    return render(request,"blog/change_news.html",{"news":news,"cat":categories,"tag":tags})


def change_category(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Category.objects.update(title=title)
            return redirect("change_cat")

    categories = Category.objects.all()
    return render(request, "blog/change_cat.html", {"categories": categories})


def change_tag(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Tag.objects.update(name=name)
            return redirect("change_tag")

    tags = Tag.objects.all()
    return render(request, "blog/change_tag.html", {"tags": tags})
def images_all(request):
    news = News.objects.all()
    cat = Category.objects.all()

    return render(request,"blog/images_all.html",{"news":news,"cat":cat})


def change_img(request,img_id):
    img1 = News.objects.get(id = img_id)
    cat = Category.objects.all()

    if request.method == "POST":
        image = request.POST.get("image")
        if image:
            img1 = image
            return redirect('change_img')
        
    return render(request,"blog/change_img.html",{"img":img1,"cat":cat})



def delete_img(request, img_id):
    image = get_object_or_404(NewsImage, id=img_id)
    image.delete()
    return redirect("images_all")


def replace_img(request, img_id):
    news = get_object_or_404(News, id=img_id)

    if request.method == "POST":
        form = ImageReplaceForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            if news.image:
                news.image.delete(save=False)
            form.save()
            return redirect("images_all")
    else:
        form = ImageReplaceForm(instance=news)

    return render(request, "blog/change_img.html", {"form": form, "news": news})