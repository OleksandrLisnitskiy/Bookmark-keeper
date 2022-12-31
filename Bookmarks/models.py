from django.db import models

# Create your models here.


class Groups(models.Model):
    group_name = models.CharField(max_length=15, help_text="Few words to describe the type of tasks inside of the group")
    creation_date = models.DateTimeField(blank=True, auto_now=True, help_text="Exact time of creation of this group")
    number_of_tasks = models.IntegerField(default=0, help_text="Number of tasks inside the group, default is 0 after creating a group")

    class Meta:
        ordering = ["creation_date"]
        verbose_name = "Group"

    def __str__(self):
        return str(self.id) + " " + self.group_name


class Tasks(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, help_text="Group to which this task belongs")
    task = models.CharField(max_length=60, null=False, help_text="content of the task to be done")
    creation_date = models.DateTimeField(blank=True, auto_now=True, help_text="Exact time of adding this task to the group")
    deadline = models.DateTimeField(blank=True, default=None, null=True, help_text="Deadline of this task, not obligatory, default null")
    is_finished = models.BooleanField(default=False, help_text="This field indicates if task is finished")

    class Meta:
        ordering = ['deadline', 'creation_date']
        verbose_name = "Task"

    def __str__(self):
        return str(self.group.group_name) + ":" + str(self.id) + ": " + self.task[:30] + "..."

