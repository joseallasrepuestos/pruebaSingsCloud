"""pruebaSingsCloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls.conf import include
from pruebaSingsCloud.views import saludo
from pruebaSingsCloud.views import ft_get_stores
from pruebaSingsCloud.views import ft_get_deals
from pruebaSingsCloud.views import ft_get_brands
from pruebaSingsCloud.views import ft_proc_inst_store_users
from pruebaSingsCloud.views import ft_get_users_suscrip_store


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('ft_get_stores/', ft_get_stores),
    path('ft_get_deals/', ft_get_deals),
    path('ft_get_brands/', ft_get_brands),
    path('ft_proc_inst_store_users/', ft_proc_inst_store_users),
    path('ft_get_users_suscrip_store/', ft_get_users_suscrip_store),
    
    # path('o/', include('oauth2_provider.urls',namespace='oauth2_provider')),
    
    
]
