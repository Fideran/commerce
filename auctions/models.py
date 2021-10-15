from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.core.exceptions import ValidationError




class User(AbstractUser):
    pass

class Bid(models.Model):
    bid = models.IntegerField(max_length=13)
    bid_user = models.ForeignKey(User, default=None, on_delete=CASCADE)

    def __str__(self):
        return f"{self.bid} $"


class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Auction(models.Model):
    auction_name = models.CharField(max_length=64)
    auction_category = models.ForeignKey(Category, on_delete=CASCADE, related_name="categories")
    auction_bid = models.IntegerField()
    auction_comment = models.CharField(max_length=64, blank=True)
    auction_user = models.ForeignKey(User, default=None, on_delete=CASCADE)
    bid_user = models.CharField(max_length=64, blank=True)
    post_time = models.DateTimeField(auto_now_add=True, blank = True)
    auction_image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return f"{self.auction_name} posted by {self.auction_user}"
    
class AuctionComment(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=CASCADE, related_name="users")
    auction = models.ForeignKey(Auction, default=None, on_delete=CASCADE, related_name="auctions")
    comment = models.CharField(max_length=150)
    def __str__(self):
        return f"{self.user}: {self.comment}"

class WhatchList(models.Model):
    auction_list = models.ForeignKey(Auction, default=None, on_delete=CASCADE, related_name="auction_lists")
    user = models.ForeignKey(User, default=None, on_delete=CASCADE, related_name="watch_lists")

    def __str__(self):
        return f"{self.auction_list}"

