from django.test import TestCase, Client
from django.urls import reverse
from .models import Goal, GoalsList, User
from . import views
from django.contrib.auth.forms import UserCreationForm


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create_user(username='test_user', password='testPassword123!')
        GoalsList.objects.create(user=user)
        Goal.objects.create(
            user=user,
            details='Test Details',
        )

    # test for Goal model
    def test_model_Goal__str__(self):
        goal = Goal.objects.first()
        expected = goal.details

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


class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    # test for sign-up view
    def test_view_sign_up_GET_status_code(self):
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)

    def test_view_sign_up_GET_template(self):
        response = self.client.get(reverse('sign_up'))
        self.assertTemplateUsed(response, 'registration/sign-up.html')

    def test_view_sign_up_GET_context(self):
        response = self.client.get(reverse('sign_up'))
        form = UserCreationForm()
        self.assertEqual(str(response.context['form']), str(form))

    def test_view_sign_up_POST_status_code(self):
        response = self.client.post(reverse('sign_up'), {
            'username': 'test_user',
            'password1': 'test_password123!',
            'password2': 'test_password123!'
        })
        self.assertEqual(response.status_code, 302)
    
    def test_view_sign_up_POST_if_user_craeted_incorrectly(self):
        response = self.client.post(reverse('sign_up'), {
            'username': 'test_user',
            'password1': 'test_password123!',
            'password2': 'test'
        })
        self.assertEqual(response.status_code, 200)
        
        

        