from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)




def write_to_file(data):
    '''
        Takes in json data and writes the values to a txt file

        input json example:
        {'email': 'blank@nomail.com', 'subject': 'testing', 'message': 'the message is'}

        txt output:
        'blank@nomail.com','testing','this message is'

    '''
    with open('./database.txt', 'a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        # append the data to the database.txt file
        file = db.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    '''
        Takes in json data and writes the values to a csv file

        input json example:
        {'email': 'blank@nomail.com', 'subject': 'testing', 'message': 'the message is'}

        txt output:
        'blank@nomail.com','testing','this message is'

    '''
    with open('./database.csv', newline='', mode='a') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        # append the data to the database.txt file
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"')
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():

    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to the database'

    else:
        return 'something went wrong. Try again!'
