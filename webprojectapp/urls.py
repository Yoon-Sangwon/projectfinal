from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('map1/', views.map1, name='map1'),
    path('map2/', views.map2, name='map2'),
    path('map2_1/', views.map2_1, name='map2_1'),
    path('board/', views.board, name='board'),
    path('register/', views.register, name='register'),  # 수정's 추가
    path('login/', views.login, name='login'),  # 수정's 추가
    path('logout/', views.logout, name='logout'),  # 수정's 추가
    path('board/<int:pk>/', views.board_view, name='board_view'),
    path('board_write/', views.board_write, name='board_write'),
    path('write/', views.write, name='write'),
    path('board/<int:pk>/remove/', views.remove_board, name='board_remove'),
    path('board/update/<int:pk>', views.update_board, name='board_update'),
    path('board_search/', views.search, name='search'),
    path('update/<int:pk>', views.update, name='update'),
    path('like/', views.board_like, name='board_like'),
]