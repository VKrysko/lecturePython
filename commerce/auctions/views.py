from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Category, Product, Watchlist, Bid, Comment, User
from django.shortcuts import render, get_object_or_404



def index(request):
    return render(request, "auctions/index.html", {
        "categories": Category.objects.all()
    })




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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def category_list(request, id, url):
    categories = get_object_or_404(Category,
                                id=id,
                                url=url,
                                available=True)
    return render(request,
                  'index',
                  {'category': categories})

def product_list(request, category_url=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_url:
        category = get_object_or_404(Category, url=category_url)
        products = products.filter(category=category)
    return render(request,
                  'auctions/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})



def detail(request, id, url):
    product = get_object_or_404(Product,
                                id=id,
                                url=url,
                                available=True)
    return render(request,
                  'auctions/detail.html',
                  {'product': product})


