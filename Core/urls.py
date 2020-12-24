from django.urls import path
from .views import *

app_name = 'Core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('category', CategoryView.as_view(), name='category'),
    path('product/<slug:slug>/', ProductDetailsView.as_view(), name='product'),
    path('add-to-cart-/<int:pro_id>/', AddToCartView.as_view(), name='addtocart'),
    path('mycart', MyCartView.as_view(), name='mycart'),
    path('managecart/<int:cartprdct_id>/', ManageCartView.as_view(), name='managecart'),
    path('empty-cart', EmptyCartView.as_view(), name='emptycart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),

    path('register', CustomerRegistrationView.as_view(), name='customerregistration'),
    path('logout', CustomerLogoutView.as_view(), name='customerlogout'),
    path('login/', CustomerLoginView.as_view(), name='customerlogin'),
    path('profile/', CustomerProfileView.as_view(), name='customerprofile'),
    path('profile/order-<int:pk>/', CustomerOrderDetailView.as_view(), name='customerorderdetail'),
    path('forgot-password/', PasswordForgotView.as_view(), name='forgotpassword'),
    path('password-reset/<email>/<token>/', PasswordResetView.as_view(), name='passwordreset'),


    # Search 
    path('search/', SearchView.as_view(), name="search"),

    # Admin pages
    path('admin-login/', AdminLoginView.as_view(), name='adminlogin'),
    path('admin-home/', AdminHomeView.as_view(), name='adminhome'),
    path('admin-order/<int:pk>/', AdminOrderDetailView.as_view(), name='adminorderdetail'),
    path('admin-all-order/', AdminOrderListView.as_view(), name='adminorderlist'),
    path('admin-order/<int:pk>-change/', AdminOrderStatusChangeView.as_view(), name='adminorderstatuschange'),
    path('admin-product/list', AdminProductListView.as_view(), name="adminproductlist"),
    path('admin-product/add', AdminProductCreateView.as_view(), name="adminproductcreate"),

    # Payment 
    path('khalti-request/', KhaltiRequestView.as_view(), name="khaltirequest"),
    path('esewa-request/', EsewaRequestView.as_view(), name="esewarequest"),
]