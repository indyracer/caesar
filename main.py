#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

import cgi

from caesar import encrypt

#html boilerplate for the top of the page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Formation</title>
</head>
<body>
    <h1>Enter some text for ROT13</h1>
"""

#html boilerplate for the bottom of the page_header
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    #Handles requests coming in to '/' (the root of our site)

    def get(self):

        #a form to submit text
        text_form = """
        <form action="/changeText" method="post" name="text-change">
            <textarea name="text" style="height: 100px; width: 400px;"></textarea>
            <br>
            <input type="submit" value="encrypt_text">
        </form>
        """
        #combine pieces to build content of page
        main_content = page_header + text_form + page_footer
        self.response.write(main_content)


class ChangeText(webapp2.RequestHandler):
    #look into the textarea and handle the encryptions
    def post(self):
        changetext = self.request.get("text-change")
        self.response.write(changetext)

     #change_text = cgi.escape(change_text, quote=True)

     #am i calling the encrypt function correctly?????
    # answer = encrypt(change_text, 13)

     #answer_content = page_header + answer + page_footer
     #self.response.write(answer_content)

"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
"""
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/changeText', ChangeText)
], debug=True)
