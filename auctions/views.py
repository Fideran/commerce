from django.conf.urls import url
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import AuctionComment, Category, User, Auction, Bid, WhatchList


def index(request):
    return render(request, "auctions/index.html",{
        "auctions": Auction.objects.all()
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

@login_required(login_url='index') 
def auction_detail(request, auction_id):
    auction = Auction.objects.get(pk=auction_id)
    max_auction = auction
    comments = auction.auctions.all()
    if request.method == "POST":
        bid = int(request.POST["bids"])
        max_bid = bid
        
        if request.user.is_authenticated and bid > 0 :
            bids = Bid(bid=bid, bid_user=User.objects.get(username=request.user.username))
            bids.save()
            if auction.auction_bid < bid and request.user != auction.auction_user :
                auction.auction_bid = bid
                auction.bid_user = request.user.username
                auction.save()
                max_bid = bid
                #max_auction = Auction.objects.get(bid_user = request.user.username)
                warning_message = ""
            
                
            else : 
                warning_message = f"You have to bid mor than {auction.auction_bid}$ or You are the poster"
                max_bid = int(auction.auction_bid)

        else:
           
            return HttpResponseRedirect(reverse('index'))

    else:
        bid = 0
        warning_message = ""
        max_bid = Auction.objects.get(pk=auction_id).auction_bid
    


    
    return render(request, "auctions/auction_detail.html", {
        "auction": auction,
        "bid": bid,
        "max_bid": max_bid,
        "max_user": Auction.objects.get(auction_bid = int(max_bid), auction_name = max_auction.auction_name ),
        "warning": warning_message,
        "comments": comments
        
        
    } )

@login_required(login_url='index') 
def new_auction(request):
    
    if request.user.is_authenticated:
        auction = Auction.objects.all()
        if request.method == "POST":
            auction_name = request.POST["auction_name"]
            auction_category = Category.objects.get(pk=int(request.POST["auction_categories"]))
            auction_user = User.objects.get(username = request.user.username) 
            auction_bid = int(request.POST["bid"])
            auction_comment = request.POST["description"]
            auction_image = request.FILES["auction_image"]
            auction = Auction(auction_name = auction_name, auction_category = auction_category, auction_user = auction_user , auction_bid = auction_bid, auction_comment = auction_comment, auction_image = auction_image )
            auction.save()
    else:
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "auctions/new_auction.html", {
       "categories": Category.objects.all()
    })

@login_required(login_url='index')
def watch_list(request):
    

    if request.user.is_authenticated:
        user = User.objects.get(username = request.user.username)
        
        if request.method == "POST":
            auction_id = request.POST["adds"]
            auction_list = Auction.objects.get(pk=auction_id)
     
            watch_lists = WhatchList.objects.all()
            i = 0
            for watch_list in watch_lists:
                if watch_list.auction_list == auction_list and watch_list.user == request.user:
                    i = i + 1
            if i == 0:       
                list = WhatchList(auction_list = auction_list , user = user )
                list.save()
            else:
                pass
    else:
        
        return HttpResponseRedirect(reverse("index"))
    
    
    return render(request, "auctions/watch_list.html", {
        "lists": user.watch_lists.all(),
        "watch_list": WhatchList.objects.all(),
        "auctions": Auction.objects.all()
        
    })
    

def category(request):
    categories = Category.objects.all()
    auction_lists = Auction.objects.all()
    return render(request, "auctions/category.html", {
        "categories": categories,
        "auctions": auction_lists #{%if auction_list.category == category.category%} <<<< HTML
    })

@login_required(login_url='index')
def delete(request):

    watch_list_ids = request.POST.getlist('selection')
    
    try:
        for watch_list_id in watch_list_ids:
            selection = WhatchList.objects.get(pk=watch_list_id)
            selection.delete()
    except UnboundLocalError:
        return render(request, "auctions/watch_list.html")
    
    return HttpResponseRedirect(reverse("watch_list"))

@login_required(login_url='index')         
def comment_auction(request, auction_id):
    auction = Auction.objects.get(pk=int(auction_id))
    if request.method == "POST":
        if request.POST['comment'] != "":
            user = request.user
            auction = auction
            comment = request.POST['comment']
            auction_comment = AuctionComment(user = user, auction = auction, comment = comment)
            auction_comment.save()
        else:
            return HttpResponseRedirect(f'/{auction.id}')

    else:
        return HttpResponseRedirect(f'/{auction.id}')
    return HttpResponseRedirect(f'/{auction.id}')
    