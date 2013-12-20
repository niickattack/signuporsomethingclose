import webapp2

form = """

 <form method = "post">

 <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
          %(usererror)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="%(password)s">
          </td>
          <td class="error">
          %(passerror)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="%(verify)s">
          </td>
          <td class="error">
          %(vererror)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>
          <td class="error">
          %(emerror)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>
"""

import cgi
import re

def escape_html(s):
    return cgi.escape(s, quote = True)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_verify(verify):
    return PASSWORD_RE.match(verify)

def valid_email(email):
    return EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    
    def write_form(self, username="", usererror="", password="", passerror="", verify="", vererror="", email="", emerror=""):
        self.response.out.write(form % {"username": escape_html(username),
                                    "usererror": escape_html(usererror),
                                    "password": escape_html(password),
                                    "passerror": escape_html(passerror),
                                    "verify": escape_html(verify),
                                    "vererror": escape_html(vererror),
                                    "email": escape_html(email),
                                    "emerror": escape_html(emerror)})
    def get(self):
        self.write_form()

    def post(self):
        user_name = self.request.get('username')
        user_error = self.request.get('usererror')
        pass_word = self.request.get('password')
        pass_error = self.request.get('passerror')
        ver_ify = self.request.get('verify')
        ver_error = self.request.get('vererror')
        e_mail = self.request.get('email')
        em_error = self.request.get('emerror')
    
        user = valid_username(user_name)
        word = valid_password(pass_word)
        ver = valid_verify(ver_ify)
        ema = valid_email(e_mail)

        if pass_word != ver_ify:
            ver_error = "Your passwords didn't match."

        if not user:
            user_error = "That's not a valid username."

        if not word:
            pass_error = "That wasn't a valid password."

        if e_mail and not ema:
            em_error = "That's not a valid email address."

        if (user_error == "" and pass_error == "" and ver_error == "" and em_error == ""):
            self.redirect("/welcome?username=" + user_name)
        else:
            pass_word =""
            ver_ify = ""
            self.write_form(user_name, user_error, pass_word, pass_error, ver_ify, ver_error, e_mail, em_error)


class DataHandler(webapp2.RequestHandler):
  def get(self):
    username = self.request.get('username')
    self.response.out.write("Welcome, " + username + "!")

app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/welcome', DataHandler)
], debug=True)


#Things I didn't use.

#import jinja2
#import os

#jinja_environment = jinja2.Environment(
#    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
#    extensions=['jinja2.ext.autoescape'])





