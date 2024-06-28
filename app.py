from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Parent routes
@app.route('/pindex')
def pindex():
    return render_template('pindex.html')

@app.route('/pdashboard')
def pdashboard():
    return render_template('pdashboard.html')

@app.route('/passignments')
def passignments():
    return render_template('passignments.html')

@app.route('/presources')
def presources():
    return render_template('presources.html')

@app.route('/plearning_resources')
def plearning_resources():
    return render_template('plearning_resources.html')

@app.route('/peducational_articles')
def peducational_articles():
    return render_template('peducational_articles.html')

@app.route('/pmessages')
def pmessages():
    return render_template('pmessages.html')

@app.route('/pprofile')
def pprofile():
    return render_template('pprofile.html')

@app.route('/ptrack_submissions')
def ptrack_submissions():
    return render_template('ptrack_submissions.html')

@app.route('/pview_feedback_grades')
def pview_feedback_grades():
    return render_template('pview_feedback_grades.html')


# Student routes
@app.route('/index')
def index():
    return render_template('students.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/assignments')
def assignments():
    return render_template('assignments.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')



# Login route
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_type = request.form.get('user-type')
        username = request.form.get('username')
        password = request.form.get('password')
        if user_type == 'student':
            return redirect(url_for('index'))
        elif user_type == 'parent':
            return redirect(url_for('pindex'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
