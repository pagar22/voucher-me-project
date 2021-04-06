from django.contrib.auth.models import User
from django.test import TestCase
from voucherMe.models import Business, Post, UserProfile
# Create your tests here.
import os, django
from voucherMe.forms import BusinessForm

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "voucher_me_project.settings")
django.setup()

print('hello world')


class UserProfileTest(TestCase):

    # def setUp(self) -> None:
    # User.objects.create(username1='test1', password='aiyouwoqu', email='123123@qq.com', asas='asasasa')

    # def UserProfile_create(self):
    #     # User.objects.create(username='test1', password='aiyouwoqu', email='123123@qq.com', asas='asasasa')
    #     UserProfile.objects.create(user='test1')
    #     u = UserProfile.objects.get(username='test1')
    #     self.assertEqual(u.username, 'test123')
    #     self.assertEqual(u.password, 'aiyouwoqu')
    #     self.assertEqual(u.email, 'email')

    # def setUp(self) -> None:
    # User.objects.create(username='test12', password='aiyouwoqu', email='121212@qq.com')
    # u1=User.objects.filter(username='test12').last()
    # self.assertEqual(u1.id, 1)
    # Business.objects.create(name='test1',
    #                         description='test1',
    #                         slug='test12',
    #                         image='media/profile_images/IMG_20180428_112912_769.jpg',
    #                         user_id=1)
    # Post.objects.create(name='test12',
    #                     description='这是一个测试用例12',
    #                     tags_category='测试用例12',
    #                     tags_type='1',
    #                     promo='测试用例12',
    #                     business_id=1,
    #                     visits=1)

    def test_create(self):
        User.objects.create(username='test1', password='aiyouwoqu', email='123123@qq.com')
        u2 = User.objects.filter(username='test1').last()
        self.assertEqual(u2.id, 1)
        Business.objects.create(name='test1',
                                description='test1',
                                slug='123test2',
                                image='media/profile_images/IMG_20180428_112912_769.jpg',
                                user_id=1)
        Post.objects.create(name='test1',
                            description='this is a test',
                            tags_category='this is a test1',
                            tags_type='1',
                            promo='this is a test1',
                            business_id=1,
                            visits=1
                            )

        p = Post.objects.filter(name='test1').last()
        self.assertEqual(p.name, 'test1')

    def test_delete(self):
        ret = Post.objects.filter(name='test12')
    #     # self.assertEqual(len(ret), 'test12')
    #     # self.assertEqual(ret.name, 'test12')

    def test_uses_list_template1(self):
        context_dict = {}
        response = self.client.get('/voucher/about/', context_dict)  # 使用Django测试客户端
        self.assertTemplateUsed(response, 'voucher/about.html')

    def test_uses_list_template2(self):
        business_list = Business.objects.order_by('-likes')
        context_dict = {'businesses': business_list}
        response = self.client.get('/voucher/business/', context=context_dict)  # 使用Django测试客户端
        self.assertTemplateUsed(response, 'voucher/all_businesses.html')


