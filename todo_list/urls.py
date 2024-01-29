from django.urls import path

from todo_list.views import (TagsListView,
                             TagsCreateView,
                             TagsUpdateView,
                             TagsDeleteView,
                             TaskListView,
                             TaskCreateView,
                             DoneTask,
                             TaskUpdateView,
                             TaskDeleteView)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tags-delete"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/done-task/", DoneTask.post, name="done-task")
]

app_name = "todo_list"
