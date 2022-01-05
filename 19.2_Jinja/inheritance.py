# Template inheritance:

  #Template inheritance plays a major role in complex applications,
  # because pages are often 95% similar to eachother;
  
# For example:
  # form/form2 and greetings/greeting2 only differ by 6 lines
  # but our copies of these routes contain hundreds of lines in total!
# Inheriting the template of our original routes will allows us to only add
# the 6 lines neccessary for a new behavior;

# We do this by creating a base template:
# See form_base.html/greetings_base.html

# <!DOCTYPE html>
# <html lang="en">
# 	<head>
#     ...
# NOTE We replace the variable parts of our template with name blocks NOTE #

# 		<title>{%block title%}<-- title content from child file -->{%endblock%}</title>

#  	</head>
# 	<body>
# 		<h1>Greeter Form</h1>
# 		<!-- set action to greeting page -->    
# 		<form action="/greetings">
# 			<input type="text" placeholder="your name" name="username" />

#      {%block content%}
#       <-- content from child file -->
#      {%endblock%}

# 			<button>Submit</button>
# 		</form>
# 	</body>
# </html>

# NOTE We then define these blocks in the child html files NOTE #
# {%extends 'base_file.html'%}

# {% block title%}
#  some title
# {%endblock%} 
# {% block content%}
#  <el><el>
# {%endblock%} 



