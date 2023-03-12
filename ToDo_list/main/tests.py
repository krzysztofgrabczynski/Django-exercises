from django.test import TestCase, Client
from django.urls import reverse, resolve
from .models import Goal, GoalsList, User
from . import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


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
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create_user(
            username='test',
            password='examplepassword123!',
        )
        GoalsList.objects.create(
            user = User.objects.first()
        )

    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.first()
        self.client.login(username=self.user.username, password='examplepassword123!')

    # test for sign-up view
    def test_view_sign_up_GET_status_code(self):
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)

    def test_view_sign_up_GET_template(self):
        response = self.client.get(reverse('sign_up'))
        self.assertTemplateUsed(response, 'registration/sign-up.html')

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

    # test for home view
    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_home_view_context_without_filter(self):
        Goal.objects.create(
                user=self.user,
                details='test',
            )
        response = self.client.get(reverse('home'))
        goals = Goal.objects.all()
        
        self.assertEqual(list(response.context['goals']), list(goals))

    def test_home_view_context_with_Completed_filter(self):
        goal_1=Goal.objects.create(
                user=self.user,
                details='test1',
            )
        goal_1.is_completed = True
        goal_1.save()
        goal_2=Goal.objects.create(
                user=self.user,
                details='test2',
            )

        response = self.client.get(reverse('home'), {
            'filter': 'Completed'
        })
        goals = [goal_1]

        self.assertEqual(list(response.context['goals']), goals)

    def test_home_view_context_with_NotCompleted_filter(self):
        goal_1=Goal.objects.create(
                user=self.user,
                details='test1',
            )
        goal_1.is_completed = True
        goal_1.save()
        goal_2=Goal.objects.create(
                user=self.user,
                details='test2',
            )

        response = self.client.get(reverse('home'), {
            'filter': 'NotCompleted'
        })
        goals = [goal_2]

        self.assertEqual(list(response.context['goals']), goals)

    # test for add view
    def test_view_add_status_code(self):
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 302)

    def test_view_add_goal_correct_data(self):
        self.client.get(reverse('add'), {
            'add_goal': 'test'
        })
        
        goals = Goal.objects.all()
        self.assertEqual(goals.count(), 1)

    def test_view_add_goal_incorrect_data(self):
        self.client.get(reverse('add'), {
            'add_goal': ''
        })
        
        goals = Goal.objects.all()
        self.assertEqual(goals.count(), 0)

    # test for delete view
    def test_view_delete(self):
        goal = Goal.objects.create(
                user=self.user,
                details='test',
            )
        self.client.get(reverse('delete', kwargs={'id': goal.id}))

        goals = Goal.objects.all()
        self.assertEqual(goals.count(), 0)

    # test for check_status_completed view
    def test_view_check_status_completed(self):
        goal = Goal.objects.create(
                user=self.user,
                details='test',
            )
        goals = Goal.objects.first()
        self.assertFalse(goals.is_completed)
        
        self.client.get(reverse('check_status_completed', kwargs={'id': goal.id}))
        goals.refresh_from_db()

        self.assertTrue(goals.is_completed)
        
class TestUrls(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create_user(
            username='test',
            password='examplepassword123!',
        )

        Goal.objects.create(
            user=user,
            details='test details',
        )

    def test_url_home(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)

    def test_url_sign_up(self):
        url = reverse('sign_up')
        self.assertEqual(resolve(url).func, views.sign_up)
    
    def test_url_login(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_url_logout(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)

    def test_url_add(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func, views.add)

    def test_url_delete(self):
        goal = Goal.objects.first()
        url = reverse('delete', args=[goal.id])
        self.assertEqual(resolve(url).func, views.delete)   

    def test_url_status_completed(self):
        goal = Goal.objects.first()
        url = reverse('check_status_completed', args=[goal.id])
        self.assertEqual(resolve(url).func, views.check_status_completed)                  
                         

    
        