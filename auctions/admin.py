from django.db import models
from auctions.models import User
from django.contrib import admin

from .models import AuctionComment, Bid, Category, User, Auction, WhatchList

# Register your models here.
class AuctionAdmin(admin.ModelAdmin):
    list_display = ("id", "auction_name", "auction_category", "auction_user", "bid_user", "auction_bid", "post_time", "auction_comment", "auction_image")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "bid", "bid_user")

class WatchListAdmin(admin.ModelAdmin):
    list_display = ("auction_list", "user")

admin.site.register(User)
admin.site.register(Auction, AuctionAdmin ) 
admin.site.register(Category, CategoryAdmin)
admin.site.register(Bid, BidAdmin )
admin.site.register(WhatchList, WatchListAdmin)
admin.site.register(AuctionComment)