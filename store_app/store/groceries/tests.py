from django.test import TestCase, SimpleTestCase
from django.urls import reverse,resolve
from .views import index,signup
from selenium import webdriver
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
    
    def test_signup_url(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)


#Functional test
class LoginPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

    def teatDown(self):
        self.browser.close()

    def testPage(self):
        self.browser.get(self.live_server_url)
        time.sleep(5)

