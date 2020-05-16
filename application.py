from flask import Flask
import boto3
import json
import base64

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# list to display
list = '<ul>'

try:
    kms = boto3.Session(region_name='us-east-1').client('kms')
    s3 = boto3.Session(region_name='us-east-1').client('s3')

    # get file from s3 bucket
    file = s3.get_object(Bucket='eb-secret-bucket', Key='secret_data.json')

    secret = file['Body'].read()

    decoded_secret = base64.b64decode(secret)

    # decrypt file with kms
    decrypted_secret = kms.decrypt(CiphertextBlob=bytes(decoded_secret))

    secret = json.loads(decrypted_secret["Plaintext"])

    # add object key and values into list
    for key, value in secret.items():
        list += '<li>{} - {} </li>'.format(key, value)

except:
    list += '<li>Error</li>'

list += '</ul>'

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n
    {}
    '''.format(list)
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()