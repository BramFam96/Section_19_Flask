from flask import Flask, request, render_template, redirect, flash, sessions
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

responses = [];

# Generate and setup server

app = Flask(__name__);

# Config and init toolbar:
app.config['SECRET_KEY'] = 'secret';

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False;

# debug = DebugToolbarExtension(app);
# Home Routing
@app.route('/')
def survey_intro():
  '''Shows survey intro'''
  
  return render_template('start_survey.html', survey=satisfaction_survey);

@app.route('/', methods = ["POST"])
def start_survey():
  '''Clears responses and begins survey'''
  responses.clear();
  return redirect('/questions/0');

#Question Routing
@app.route('/questions/<int:q_num>')
def show_question(q_num):
  '''Display question'''
  if (len(responses) == len(satisfaction_survey.questions)):
    return redirect("/complete")

  if (len(responses) != q_num):
    flash('Invalid question')
    return redirect(f"/questions/{len(responses)}")

  question_dict = satisfaction_survey.questions[q_num]
  
  return render_template(
    "question.html", q_num=q_num, question=question_dict)

# Results routing
@app.route('/completed')
def completed_msg():
  """Displays thank you message"""
  if(len(responses) == 0):
    return redirect('/')

  elif(len(responses) != len(satisfaction_survey.questions)):
    return redirect(f'/questions/{len(responses)}')
  
  else:
    return render_template('completed_survey.html', 
    survey=satisfaction_survey, responses=responses)

# Updating responses
@app.route('/update-responses', methods = ['POST'])
def handle_response():
  "Save response to response list and redirect to next question"
  
  answer = request.form['answer']
  text = request.form.get('text','');

  responses.append({'answer':answer, 'text':text});

  if(len(responses) == len(satisfaction_survey.questions)):
    return redirect('/completed')
  else:
    return redirect(f'/questions/{len(responses)}')

