from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    title = models.CharField(max_length=256, blank=False)
    details = models.TextField(blank=False)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    def __repr__(self) -> str:
        return self.__str__()


class GoalsList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals_list')
    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)

    def __str__(self) -> str:
        return f"{self.user}'s goals list"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    @property
    def goals_list(self):
        goals = Goal.objects.filter(user=self.user)
        return list(goals)

    def goals_list_len(self):
        return len(self.goals_list)
    
