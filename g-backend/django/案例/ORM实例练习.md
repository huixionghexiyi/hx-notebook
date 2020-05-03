# models.py

```py
from django.db import models
from  datetime import datetime
class Student(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.SmallIntegerField(default=1) # 1 男 0 女

    class Meta:
        db_table = 'student'

class Course(models.Model):
    '''课程表'''
    name  = models.CharField(max_length=100)
    teacher = models.ForeignKey("Teacher",on_delete=models.SET_NULL,null=True)
    class Meta:
        db_table = 'course'

class Score(models.Model):
    '''分数'''
    student = models.ForeignKey("Student",on_delete=models.CASCADE)
    course = models.ForeignKey("Course",on_delete=models.CASCADE)
    number = models.FloatField()
    class Meta:
        db_table = 'score'

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'teacher'
```

# Views.py

```py
from django.http import JsonResponse
from django.db import connection
from .models import Student, Score, Course, Teacher
from django.db.models import Avg, Count, Max, Min, Sum, Q, F

MALE = 1
FEMALE = 0


def db_demo(request):
    '''初始化数据'''
    Student.objects.bulk_create([
        Student(username='李荣浩', age=17, gender=MALE),
        Student(username='范冰冰', age=18, gender=FEMALE),
        Student(username='周杰伦', age=21, gender=MALE),
        Student(username='孙燕姿', age=21, gender=FEMALE),
        Student(username='huixiong', age=10089, gender=MALE)
    ])
    Teacher.objects.bulk_create([
        Teacher(name='数学老师'),
        Teacher(name='语文老师'),
        Teacher(name='英语老师'),
        Teacher(name='物理老师'),
    ])
    Course.objects.bulk_create([
        Course(name='math', teacher=Teacher.objects.get(name='数学老师')),
        Course(name='zh', teacher=Teacher.objects.get(name='语文老师')),
        Course(name='eng', teacher=Teacher.objects.get(name='英语老师')),
        Course(name='phy', teacher=Teacher.objects.get(name='物理老师'))
    ])
    Score.objects.bulk_create([
        Score(student=Student.objects.get(username='范冰冰'),
              course=Course.objects.get(name='math'), number='12'),
        Score(student=Student.objects.get(username='范冰冰'),
              course=Course.objects.get(name='zh'), number='12'),
        Score(student=Student.objects.get(username='范冰冰'),
              course=Course.objects.get(name='eng'), number='12'),
        Score(student=Student.objects.get(username='范冰冰'),
              course=Course.objects.get(name='phy'), number='12'),

        Score(student=Student.objects.get(username='李荣浩'),
              course=Course.objects.get(name='math'), number='25'),
        Score(student=Student.objects.get(username='李荣浩'),
              course=Course.objects.get(name='zh'), number='25'),
        Score(student=Student.objects.get(username='李荣浩'),
              course=Course.objects.get(name='eng'), number='25'),
        Score(student=Student.objects.get(username='李荣浩'),
              course=Course.objects.get(name='phy'), number='25'),

        Score(student=Student.objects.get(username='周杰伦'),
              course=Course.objects.get(name='math'), number='99'),
        Score(student=Student.objects.get(username='周杰伦'),
              course=Course.objects.get(name='zh'), number='99'),
        Score(student=Student.objects.get(username='周杰伦'),
              course=Course.objects.get(name='eng'), number='99'),
        Score(student=Student.objects.get(username='周杰伦'),
              course=Course.objects.get(name='phy'), number='99'),

        Score(student=Student.objects.get(username='孙燕姿'),
              course=Course.objects.get(name='math'), number='44'),
        Score(student=Student.objects.get(username='孙燕姿'),
              course=Course.objects.get(name='zh'), number='44'),
        Score(student=Student.objects.get(username='孙燕姿'),
              course=Course.objects.get(name='eng'), number='44'),
        Score(student=Student.objects.get(username='孙燕姿'),
              course=Course.objects.get(name='phy'), number='44'),

        Score(student=Student.objects.get(username='huixiong'),
              course=Course.objects.get(name='zh'), number=9.8)
    ])

    Course.objects.create(name='cc', teacher=Teacher.objects.get(name='语文老师'))
    hx = Student.objects.get(username='huixiong')
    Score.objects.create(student=hx,
                         course=Course.objects.get(name='cc'), number=111)
    return JsonResponse({"a": 'aaa'})


def db_demo1(request):
    '''查询平均成绩大于60分的同学的id和平均成绩'''
    # rows = Student.objects.annotate(score_avg=Avg('score__number')).filter(
    #     score_avg__gte=60).values("id", "score_avg")

    '''查询所有同学的id/姓名/选课数/总成绩'''
    # rows = Student.objects.annotate(course_nums=Count('score__course'),total_score=Sum('score__number')).values('id','username','course_nums','total_score')

    '''查询姓数学的老师的个数'''
    # rows = Teacher.objects.filter(name__startswith='数学').count()
    # print(rows)

    '''查询没学过“数学老师”课的同学的id、姓名'''
    # rows = Student.objects.exclude(score__course__teacher__name='英语老师').values('id','username')

    '''查询学过课程id为1和2的所有同学的id、姓名'''
    # rows = Student.objects.filter(score__course__in=[1,3]).distinct().values('id','username')

    '''
    查询学过“语文老师”所教的“所有课”的同学的id、姓名
    1. 筛选每个学生上了几门黄老师的课
    2. 学生上的黄老师课程总数=黄老师教的课程总数，那么该学生就是上了所有黄老师的课
    '''
    # rows = Student.objects.annotate(
    #     nums=Count("score__course", filter=Q(score__course__teacher__name='语文老师'))).filter(nums=Course.objects.filter(teacher__name='语文老师').count()).values('id', 'username','nums')

    '''
    所有课程成绩小于60分的学生的id和姓名
    '''
    # rows = Student.objects.exclude(score__number__gt=60).values('id','username','score__number')
    '''
    查询没有学全所有课程的学生的id和姓名
    '''
    # rows = Student.objects.annotate(nums=Count(F('score__course'))).filter(nums__lt=Course.objects.count()).values('id','username')
    '''
    查询所有学生的姓名、平均分，并且按照平均分从高到低排序
    '''
    # rows = Student.objects.annotate(avg=Avg(F('score__number'))).order_by('-avg').values('id','username','avg')
    '''
    查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分
    '''
    # rows = Course.objects.annotate(max=Max('score__number'),min=Min('score__number')).values('id','name','max','min')
    '''
    查询每门课程的平均成绩，按照平均成绩进行排序
    '''
    # rows = Course.objects.annotate(avg=Avg('score__number')).order_by('-avg').values('id','name','avg')
    '''
    统计总共有多少女生，多少男生
    '''
    # rows =  Student.objects.aggregate(boy=Count('gender',filter=Q(gender=1)),girl=Count('gender',filter=Q(gender=0)))
    # print(rows)
    '''
    将“英语老师”的每一门课程都在原来的基础之上加5分
    '''
    # rows = Score.objects.filter(course__teacher__name='英语老师').update(number=F('number')+5)
    # print(rows)
    '''
    查询两门以上不及格的同学的id、姓名、以及不及格课程数
    '''
    rows = Student.objects.annotate(count=Count('score__number',filter=Q(score__number__lt=60))).filter(count__gte=2).values('id','username')
    '''
    查询每门课的选课人数
    '''
    rows = Course.objects.annotate(count=Count('score__student')).values('id','name','count')
    # print(rows)
    for r in rows:
        print(r)
    return JsonResponse({"b": "bbb"})


```