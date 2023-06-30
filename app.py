from flask import Flask,render_template

app = Flask(__name__)

JOBS =[
        {
            'id': 1,
            'title' : 'Data Scientist',
            'location' : 'Bengaluru, India',
            'salary' : 'Rs. 10,00000'
        },
        {
            'id': 2,
            'title' : 'Data Analyst',
            'location' : 'Delhi, India',
            'salary' : 'Rs. 10,0000'
        },
        {
            'id': 3,
            'title' : 'ML engineering',
            'location' : 'Kolkata, India',
            'salary' : 'Rs. 10,000'
        },
        {
            'id': 4,
            'title' : 'Front-end Engineer',
            'location' : 'Kolkata, India',
            'salary' : 'Rs. 1,000'
        },
        {
            'id': 5,
            'title' : 'Back-end Engineer',
            'location' : 'Kolkata, India',
            'salary' : 'Rs. 100'
        },
      ]
@app.route('/')
def home():
    return render_template('home.html',job=JOBS)

if __name__ == '__main__':

    app.run(host="0.0.0.0",debug=True)



