from django.db import models


# Create your models here.


class Department(models.Model):
    """部门表"""
    # id = models.BigAutoField(verbose_name="ID", primary_key=True) # 可以自动创建
    title = models.CharField(verbose_name="标题", max_length=32)
    title = models.CharField(verbose_name="标题", max_length=32)


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="员工", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)  # 可以是小数
    create_time = models.DateTimeField(verbose_name="入职时间")

    # 无约束 id只能是部门中存在的id
    # depart_id = models.BigIntegerField(verbose_name="部门ID")

    # 1. 有约束  id只能是部门中存在的id
    #    - to, 与哪张表关联
    #    - to_field,表中的哪一列关联
    # 2. django自动
    #    -  写的depart
    #    -  生成数据列 depart_id
    # 3 部门表被删除
    #   3.1级联删除
    # depart = models.ForeignKey(to="Department", to_fields="id", on_delete=models.CASCADE)
    #   3.2置空
    depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)

    # django中做的约束
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
