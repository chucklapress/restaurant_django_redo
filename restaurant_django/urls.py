"""restaurant_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
from app.views import IndexView, ProfileView, SignUpView, MenuView, CreateOrderView, OrderListView, OrderDetailView, KitchenOrderView, MenuItemView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',IndexView.as_view(), name="index_view"),
    url(r'^signup/', SignUpView.as_view(), name="sign_up_view"),
    url(r'^accounts/profile/$', ProfileView.as_view(),name="profile_view"),
    url(r'^profiles/(?P<pk>\d+)$', ProfileView.as_view(), name="profile_view"),
    url(r'^menu/$', MenuItemView.as_view(), name="menu_item_view"),
    url(r'^login/$', login, name="login_view"),
    url(r'^logout/$', logout, name="logout_view"),
    url(r'^order/$', CreateOrderView.as_view(), name="create_order_view"),
    url(r'^orders/$', OrderListView.as_view(), name="order_list_view"),
    url(r'^orders/(?P<pk>\d+)$', OrderDetailView.as_view(), name="order_detail_view"),
    url(r'^kitchen/$', KitchenOrderView.as_view(), name="kitchen_order_view")
    #url(r'^menu_item/$',MenuItemView.as_view(), name='menu_item_view')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
