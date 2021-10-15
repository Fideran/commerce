from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:auction_id>", views.auction_detail, name="auction_detail"),
    path("new", views.new_auction, name="new_auction"),
    path("watch_list", views.watch_list, name="watch_list" ),
    path("category", views.category, name="category"),
    path("watch_list/delete", views.delete, name="delete"),
    path("<int:auction_id>/comment", views.comment_auction, name="comment")

]
