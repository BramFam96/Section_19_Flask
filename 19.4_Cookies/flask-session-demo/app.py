from flask import Flask, request, render_template, redirect, sessions
from flask import session, make_response
from secret import *


# Flask uses a secret key to encrypt cookies used to connect
# the browser to the session--so if you want to use sessions,
# you have to have a secret key. If the public learns this
# value, they can forge session information--so for sites with
# security concerns, make sure this isn't checked into a
# public place like GitHub

# NOTE key has been moved to secret.py, and added to gitignore file;

##########################################################
# NOTE Reading cookies NOTE #
##########################################################
# Before request will run on the way to any other route:
# We'll use it to read out cookies:
@app.before_request
def print_cookies():
    """For every single request that comes in, print out request.cookies (printed to terminal)"""
    print("*********************")
    # Request contains a cookie attribute:
    print(request.cookies)

    print("*********************")
###########################################################
# Cont from Session.txt line 17:
@app.route("/")
def index():
    # Session creates a single illegible cookie called session;
    # We can set and access them like regular dicts:
    session['username'] = 'OneMillionAnts'
    session['leaderboard'] = ['OneMillionAnts', 'WeinMachine', 'sleeep']
    # Once they're set we could delete the two lines above and go with
    # print(session['username']/session['leaderboard']); 
    # NOTE Example can be found on line 152 of this file:
    """Homepage."""
    return render_template("index.html")
    # fundamentally, flask takes this file, extracts the text, creates a res, and 
    # converts that res to a string to be transmitted;


@app.route("/demo")
# Picking up from Cookies.txt line 73:
# We must change our underlying response object!
def set_response_demo():
    content = "<h1>HELLO!!</h1>"
    # To make our response manually we first pass content into make_response"
    # This could still be an imported file we've iterated over;
    res = make_response(content)
    # Then we override this new response's cookies with set_cookie:
    res.set_cookie("jolly_rancher_flavor", "grape")
    # Ultimately we return the response directly:
    return res
    # Flask still takes this res obj, turns it into text and responds with it;
    # Browser now contains a cookie for jolly_rancher_flavor;
    # The browser will always respond with jolly_ranch_flavor; 
    # Back to Cookies.txt line 75

################################################################
# Routes that demonstrate cookies


@app.route("/form-cookie")
def show_form():
    """Show form that prompts for favorite color."""

    return render_template("form-cookie.html")


@app.route("/handle-form-cookie")
def handle_form():
    """Return form response; include cookie for browser."""

    fav_color = request.args["fav_color"]

    # Get HTML to send back. Normally, we'd return this, but
    # we need to do in pieces, so we can add a cookie first
    html = render_template("response-cookie.html", fav_color=fav_color)

    # In order to set a cookie from Flask, we need to deal
    # with the response a bit more directly than usual.
    # First, let's make a response obj from that HTML
    resp = make_response(html)

    # Let's add a cookie to our response. (There are lots of
    # other options here--see the Flask docs for how to set
    # cookie expiration, domain it should apply to, or path)
    resp.set_cookie("fav_color", fav_color)

    return resp


@app.route("/later-cookie")
def later():
    """An example page that can use that cookie."""

    fav_color = request.cookies.get("fav_color", "<unset>")

    return render_template("later-cookie.html", fav_color=fav_color)


################################################################
# Routes that demonstrate sessions


@app.route("/form-session")
def show_sessions_form():
    """Show form that prompts for nickname and lucky number."""

    return render_template("form-session.html")


@app.route("/handle-form-session")
def handle_sessions_form():
    """Return agreeable response and save to session."""

    # Get nickname and lucky number from form and put them
    # into the session--this will automatically trigger Flask's
    # session machinery, so it will now send out a cookie with
    # a session ID. Since we're using the standard
    # "store session data as a cookie", it will include that
    # Use request.args since this is a get route
    session["nickname"] = request.args["nickname"]
    session["lucky_number"] = int(request.args["lucky_number"])

    # Since we stored this in the session, we don't even need
    # to pass it to the template directly--jinja templates
    # automatically have access to session information
    return render_template("response-session.html")
    # Within our template we can access session['data'];
    # See templates/response-session.html


@app.route("/later-session")
def session_later():
    """An example page that uses that session info."""

    # We could simply get the information from the session
    # directly in our template (as shown in the template
    # for handle_session_form), but we'll demonstrate here
    # that we can also get to the session information in
    # Flask code
    nickname = session.get("nickname", "<no nickname>")

    return render_template("later-session.html", nickname=nickname)


# **************************
# SECRET-INVITE DEMO ROUTES:
# **************************
# What we're trying to do:
# Make a secret invite page, only accessible to those with the passcode;
# Let's call this route secret-invite:
@app.route("/secret-invite")
def show_secret_invite():
    """
    Check to see if session contains 'entered-pin' 
    (Checks to see if pin is correct secret code)

    - If it is, render the invite template

    - If session['entered-pin'] is missing or False, redirect user 
    to the form to enter the secret code
    """
    if session.get("entered-pin", False):
        return render_template("invite.html")
    else:
        # On false case we redirect to a login form
        return redirect("/login-form")
# Let's make the login form

@app.route("/login-form")
def show_login_form():
    """Show form that prompts users to enter the secret access code"""
    return render_template("login-form.html")


@app.route("/verify-login")
def verify_secret_code():
    """
    Checks to see if the entered access code is correct

    - If the code is incorrect, redirect users back to the login form to try again

    - If the code is correct...
        - set session to indicate that user has access
        - redirect to the secret invite
    """
    SECRET = "chickenz_are_gr8"
    entered_code = request.args["secret_code"]
    if entered_code == SECRET:
        session["entered-pin"] = True
        return redirect("/secret-invite")
    else:
        return redirect("/login-form")

# We didn't need session for a single use token, but now we can see its magic;
# We can navigate around, open a new browser, and still have access to the secret page


