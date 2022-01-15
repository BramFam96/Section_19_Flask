from flask import Flask, request, render_template, redirect, flash, session, sessions
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

R = 'responses'
# Generate and setup server

app = Flask(__name__);


# Config:
app.config['SECRET_KEY'] = 'secret';
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False;

debug = DebugToolbarExtension(app);
# Home Routing
@app.route('/')
def survey_intro():
  '''Shows survey intro'''
  
  return render_template('start_survey.html', survey=satisfaction_survey);

@app.route('/', methods = ["POST"])
def start_survey():
  '''Clears responses and begins survey'''
  session[R] = [];
  return redirect('/questions/0');

#Question Routing
@app.route('/questions/<int:q_num>')
def show_question(q_num):
  responses = session.get(R);
  '''Ensures users are presented with the current question'''
  # Prevent early access to question page:
  if (responses is None ):
    flash('Please start the survey first', 'err');
    return redirect('/')
  # Prevent users from accessing questions out of order:  
  if (len(responses) != q_num):
    flash(f'Redirected to question: {q_num}', 'err')
    return redirect(f"/questions/{len(responses)}")
  elif (len(responses) == len(satisfaction_survey.questions)):
    return redirect("/complete")



  question_dict = satisfaction_survey.questions[q_num]
  
  return render_template(
    "question.html", q_num=q_num, question=question_dict)

# Results routing
@app.route('/completed')
def completed_msg():
  """Displays thank you message"""
  responses = session[R]
  if(responses is None):
    return redirect('/')

  elif(len(responses) != len(satisfaction_survey.questions)):
    flash('Please complete to view answers', 'err')
    return redirect(f'/questions/{len(responses)}')
  
  else:
    return render_template('completed_survey.html', survey=satisfaction_survey)

# Updating session with responses
@app.route('/update-responses', methods = ['POST'])
def handle_response():
  "Save response to response list and redirect to next question"
  # form data:
  answer = request.form['answer']
  text = request.form.get('text','');
  #add this to session
  responses = session[R] 
  responses.append({'answer':answer, 'text':text});
  session[R] = responses
  if(len(responses) == len(satisfaction_survey.questions)):
    return redirect('/completed')
  else:
    return redirect(f'/questions/{len(responses)}')

