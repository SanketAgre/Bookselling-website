
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .controller import authviews, cartviews,checkout, wishlist

urlpatterns = [
    path('', views.index, name="home"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>',  views.collectionviews, name="collectionviews"),
    path('collections/<str:cat_slug>/<str:prod_slug>', views.productviews, name="productviews"),
    
    path('register', authviews.register, name="register"),
    path('login', authviews.loginpage, name='loginpage'),
    path('logout', authviews.logoutpage, name='logoutpage'),

    path('add-to-cart', cartviews.addtocart, name="addtocart"),
    path('viewcart', cartviews.cart, name="cart"),
    path('update-cart', cartviews.updatecart, name="updatecart"),
    path('delete-cart-item', cartviews.deletecartitem, name="deletecartitem"),

    path('wishlist',wishlist.wishlist, name="wishlist"),
    path('add-to-wishlist', wishlist.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item', wishlist.deletewishlistitem,name="deletewishlistitem"),

    path('checkout', checkout.checkout, name="checkout"),
]





if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

