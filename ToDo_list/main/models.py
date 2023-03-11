from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    details = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.details
    
    def __repr__(self) -> str:
        return self.__str__()


class GoalsList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals_list')
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    def __str__(self) -> str:
        return f"{self.user}'s goals list"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    @property
    def goals_list(self):
        try:
            goals = Goal.objects.filter(user=self.user).order_by('-date')
            return list(goals)
        except:
            return None

    def goals_list_len(self):
        return len(self.goals_list)
    
