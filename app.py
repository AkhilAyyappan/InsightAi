from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
# In-memory list to store assignments (replace with database in production)
assignments_list = []
uploaded_files = []

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
        elif user_type == 'teacher':
            return redirect(url_for('tindex'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

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
    return render_template('assignments.html', assignments=assignments_list, uploaded_files=uploaded_files)

@app.route('/submit_assignment', methods=['POST'])
def submit_assignment():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    assignment_title = request.form['assignment_title']
    
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Update assignment status or perform other actions as needed
    for assignment in assignments_list:
        if assignment['title'] == assignment_title:
            assignment['has_submission'] = True

    return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/messages')
def messages():
    return render_template('messages.html')


#teacher routes

@app.route('/tindex')
def tindex():
    return render_template('tindex.html')

@app.route('/assign')
def assign():
    return render_template('assign.html')

@app.route('/timetable')
def timetable():
    return render_template('timetable.html')

@app.route('/ai_feedback')
def ai_feedback():
    return render_template('ai-feedback.html')

@app.route('/class_overview')
def class_overview():
    return render_template('class-overview.html')

@app.route('/create_assignments', methods=['GET', 'POST'])
def create_assignments():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due-date']
        
        # Handle file upload
        if 'file-upload' in request.files:
            files = request.files.getlist('file-upload')
            for file in files:
                if file.filename != '':
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    uploaded_files.append(filename)
                    
        files_for_assignment = uploaded_files[-1] if uploaded_files else None
        
        assignment = {
            'title': title,
            'description': description,
            'due_date': due_date,
            'files': files_for_assignment  # Attach uploaded file names to the assignment
        }
        assignments_list.insert(0,assignment)

        
        return redirect(url_for('create_assignments'))
    return render_template('create-assignments.html')

@app.route('/grade_assignments')
def grade_assignments():
    return render_template('grade-assignments.html')

@app.route('/resource_library')
def resource_library():
    return render_template('resource-library.html')

@app.route('/tresource')
def tresource():
    return render_template('tresource.html')

@app.route('/share_learning_material')
def share_learning_material():
    return render_template('share-learning-materials.html')

@app.route('/upload_resources')
def upload_resources():
    return render_template('upload-resources.html')

@app.route('/student_performance')
def student_performance():
    return render_template('student-performance.html')

#logout route

@app.route('/logout')
def logout():
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)
