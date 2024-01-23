from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render

from Todo_List.models import Tag, Task


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "todo_list/tags-list.html"


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    context_object_name = "tags_form"
    template_name = "todo_list/tags_form.html"
    success_url = reverse_lazy("todo_list:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    context_object_name = "tags_form"
    template_name = "todo_list/tags_form.html"
    success_url = reverse_lazy("todo_list:tags-list")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    context_object_name = "tags_delete"
    template_name = "todo_list/tags_delete.html"
    success_url = reverse_lazy("todo_list:tags-list")


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo_list/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    context_object_name = "task_form"
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    context_object_name = "task_form"
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    context_object_name = "task_delete"
    template_name = "todo_list/task_delete.html"
    success_url = reverse_lazy("todo_list:index")


def done_task(request, pk):
    if Task.objects.get(id=pk).ready:
        Task.objects.filter(id=pk).update(ready=False)
    else:
        Task.objects.filter(id=pk).update(ready=True)
    return HttpResponseRedirect(reverse_lazy("todo_list:index"))
