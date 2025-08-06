from django.urls import path
from tasks import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task_list"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path("<int:pk>/update", views.TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete", views.TaskDeleteView.as_view(), name="task_delete"),
    path("task-create/", views.TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/complete", views.TaskCompleteView.as_view(), name="task_complete"),
    path("comment/edit/<int:pk>/", views.CommentUpdateView.as_view(), name="edit_comment"),
    path("comment/delete/<int:pk>/", views.CommentDeleteView.as_view(), name="delete_comment"),
    path("comment/like/<int:pk>/", views.CommentLikeToggle.as_view(), name="comment_like_toggle"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),

]

app_name = "tasks"
