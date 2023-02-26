from django.test import TestCase
from .models import Goal, GoalsList, User

class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create_user(username='test_user', password='testPassword123!')
        GoalsList.objects.create(user=user)
        Goal.objects.create(
            user=user,
            title='Test Goal',
            details='Test Details',
        )

    # test for Goal model
    def test_model_Goal__str__(self):
        goal = Goal.objects.first()
        expected = goal.title

        self.assertEqual(expected, str(goal))

    # test for GoalsList model
    def test_model_GoalsList__str__(self):
        goals_list = GoalsList.objects.first()
        expected = f"{goals_list.user}'s goals list"

        self.assertEqual(expected, str(goals_list))

    def test_model_GoalsList_goals_list_property(self):
        goals_list = GoalsList.objects.first().goals_list
        goal = Goal.objects.first()
        expected = [goal]

        self.assertEqual(expected, goals_list)

    def test_model_GoalsList_goals_list_len(self):
        goals_list = GoalsList.objects.first()

        self.assertEqual(goals_list.goals_list_len(), 1)    