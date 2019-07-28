from django.urls import path,include

from todolist import views
app_name = 'todolist'
urlpatterns = [
    path('home/',views.home,name='主页'),
    path('about/',views.about,name='关于'),
    path('edit/<每件事_id>',views.edit,name='编辑'),
    path('del/<每件事_id>',views.delete,name='删除'),
    path('cross/<每件事_id>',views.cross,name='划掉'),


]