"""
URL configuration for day16 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    # path("admin/", admin.site.urls),

    # 部门列表
    path("depart/list/", views.depart_list),

    # 添加部门
    path("depart/add/", views.depart_add),

    # 删除部门
    path("depart/delete/", views.depart_delete),

    # 编辑
    # http://127.0.0.1:8000/depart/1/edit/  # 携带行号
    # http://127.0.0.1:8000/depart/3/edit/
    # http://127.0.0.1:8000/depart/10/edit/
    path("depart/<int:nid>/edit/", views.depart_edit),
]
