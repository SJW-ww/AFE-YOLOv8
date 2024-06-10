from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.
def depart_list(request):
    """部门列表"""

    # 去数据库取数据（部门列表）
    queryset = models.Department.objects.all()
    return render(request, "depart_list.html", {'queryset': queryset})


def depart_add(request):
    """添加部门"""
    if request.method == "GET":
        return render(request, "depart_add.html")

    # 获取用户POST提交过来的数据(title输入为空先不考虑)
    title = request.POST.get("title")

    # 保存到数据库
    models.Department.objects.create(title=title)

    return redirect("/depart/list/")


def depart_delete(request):
    """删除部门"""
    # 获取id
    # http://127.0.0.1:8000/depart/delete/?nid=2
    nid = request.GET.get('nid')

    # 删除
    models.Department.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/depart/list/")


def depart_edit(request, nid):
    """修改部门"""
    # 将要修改的内容进行显示
    if request.method == "GET":
        # 根据nid，获取数据[obj,] row_object设为默认值显示在编辑框
        # row_object = models.Department.objects.filter(id=nid)[0]
        row_object = models.Department.objects.filter(id=nid).first()

        return render(request, 'depart_edit.html', {'row_object': row_object})
    # 对POST提交的内容进行修改然后进行修改
    else:
        # 用户提交的标题
        title = request.POST.get('title')

        # 根据ID找到数据库中的数据并进行更新
        models.Department.objects.filter(id=nid).update(title=title)

        # 重定向回部门列表页面
        return redirect("/depart/list/")
