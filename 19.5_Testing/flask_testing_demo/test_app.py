from app import app
from flask import session
from unittest import TestCase

# Prevent code from getting error html pages;
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class ColorViewsTestCase(TestCase):
    # NOTE setUp and tearDown! less useful in this example:
        # on app with dbs setUp and tearDown will be critical for cleaning up
            # any changes we make to a real db;
# NOTE FORMAT NOTE    
# setUp and tearDown will run before each individual test;
#     def setUp(self):
    #     print("INSIDE SET UP")

    # def tearDown(self):
    #     print("INSIDE TEAR DOWN")
# setUpClass and tearDownClass will run before and after this entire class;
    # ie setUpClass -> setUp -> func -> tearDown -> setUp.. tearDownClass;
    # @classmethod
    # def setUpClass(cls):
    #     print("INSIDE SET UP CLASS")

    # @classmethod
    # def tearDownClass(cls):
    #     print("INSIDE TEAR DOWN CLASS")



############################ NOTE BASIC INTEGRATION NOTE ################################

    def test_color_form(self):
        # We should create a new test client for each test;
        with app.test_client() as client:
            # client represents our server;
            # We'll make a request:
            res = client.get('/')
            # Special key_word as_text:
            html = res.get_data(as_text=True)

            # page is rendering?
            self.assertEqual(res.status_code, 200)
            # form title rendered?
            self.assertIn('<h1>Color Form</h1>', html)

########################## NOTE POST Route - app.py line 25 NOTE ######################

    def test_color_submit(self):
        with app.test_client() as client:
            # We call client post, and pass data as dict;
            res = client.post('/fav-color', data={'color': 'orange'})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            # We need to replace {{favcolor}} with orange since we set it;
            # Check templates/color
            self.assertIn('<h3>Woah! I like orange, too</h3>',  html)

########################NOTE REDIRECT TESTING NOTE#####################################

    def test_redirection(self):
        with app.test_client() as client:
            res = client.get('/redirect-me')
            # Redirect does not have access to the template to check;
            # Instead we need to check if res.location equals the route we were expecting;
            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, 'http://localhost/')
            # We'd also like to test that we get correct html when redirect is followed
            #Let's do that in a new test:
            # Using follow_redirects
    def test_redirection_followed(self):
        with app.test_client() as client:
            res = client.get('/redirect-me', follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Color Form</h1>', html)

##########################NOTE SESSION NOTE##########################################

# Session is only keeping track of count;
    def test_session_count(self):
        with app.test_client() as client:
            res = client.get('/')
            # New client -> test for first time count;
            # If we call client.get('/') again, we'll get count of 2;
            self.assertEqual(res.status_code, 200)
            self.assertEqual(session['count'], 1)

    def test_session_count_set(self):
        with app.test_client() as client:
            # Session_transaction() lets us set session data;
            with client.session_transaction() as change_session:
                change_session['count'] = 999

            res = client.get('/')

            self.assertEqual(res.status_code, 200)
            self.assertEqual(session['count'], 1000)
