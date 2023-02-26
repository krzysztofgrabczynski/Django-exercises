from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class Memento:
    def __init__(self) -> None:
        self._goals_list = []
        self._index = 0

    def add(self, goal):
        if self._index != len(self._goals_list):
            self._goals_list = self._goals_list[:self._index]

        self._goals_list.append(goal)
        self._index += 1
            
    # def save(self):
    #     if self._index != len(self._goals_list):
    #         self._goals_list = self._goals_list[:self._index]

    def undo(self):
        if self._index > 0:
            self._index -= 1

    def redo(self):
        if self._index < len(self._goals_list):
            self._index += 1
        
    def read_state(self):

        if self._index-1 >= 0:
            return self._goals_list[self._index - 1]
        else:   
            return None
        
    @property
    def goals_list(self):
        return self._goals_list


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
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._goals = Memento()

    @property
    def goals(self):
        return self._goals.goals_list


    # @property
    # def goals_list(self):
    #     goals = Goal.objects.filter(user=self.user)
    #     return list(goals)

    def goals_list_len(self):
        return len(self.goals_list)