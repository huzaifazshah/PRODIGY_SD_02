from flask import Flask,render_template,request,session,url_for
import random

app =Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/',methods=['GET','POST'])
def index():
    if 'number_to_guess' not in session:
        session['number_to_guess'] = random.randint(1,100)
        session['number_of_attempts'] = 0

    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['number_of_attempts'] += 1
        number_to_guess = session['number_to_guess']
    
        if guess < number_to_guess:
            feedback = 'Too low! Try again'
        elif guess > number_to_guess:
            feedback = 'Too high! Try again'
        else:
            feedback = f'Congratulations! You guessed the correct number:{number_to_guess}'
            attempts = session['number_of_attempts']
            session.pop('number_to_guess',None)
            session.pop('number_of_attempts',None)
            return render_template('index_html',feedback=feedback, attempts=attempts)
        return render_template('index.html',feedback=feedback)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


                                                                                               