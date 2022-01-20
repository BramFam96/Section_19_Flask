from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        """Start up test_client, and config enviroment to testing"""
        self.client=app.test_client()
        app.config['TESTING'] = True;
    def test_home(self):
        '''Index html displays? Data is saved to session?'''
        with self.client:
        # Dummy response
            res = self.client.get('/')
        # Check HTML responses
            self.assertIn(b'High Score', res.data)
            self.assertIn(b'<p>Score', res.data)
            self.assertIn(b'Seconds Left:', res.data)
        # Check session data
            self.assertIn('board',session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
    def test_word_on_board(self):
        """Set board data and test word validation"""
        with self.client as client:
            with client.session_transaction() as session:
                session['board'] = [
                    ["B","A","T","S","S"],
                    ["B","A","T","T","L"],
                    ["B","A","A","O","O"],
                    ["B","L","T","T","T"],
                    ["L","A","T","H","H"],
                ]
        valid_words = ['bats','sloth','stall','slot']
        for word in valid_words:
            res = self.client.get(f'/check-word?word={word}')
            self.assertEqual(res.json['result'],'ok')
    def test_word_not_on_board(self):
        "Test that word validation catches words that don't exist on board"
        self.client.get('/')
        res = self.client.get('/check-word?word=onomatopoeia')
        self.assertEqual(res.json['result'],'not-on-board')
    def test_word_not_english(self):
        'Test that word validation catches non-english words'
        self.client.get('/')
        res = self.client.get('check-word?word=asdfasdf')
        self.assertEqual(res.json['result'], 'not-word')
