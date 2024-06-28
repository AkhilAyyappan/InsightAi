document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    const userType = document.getElementById('user-type').value;

    if (userType === 'student') {
        window.location.href = 'students.html';
    } else if (userType === 'teacher') {
        window.location.href = 'teacher_dashboard.html';
    } else if (userType === 'parent') {
        window.location.href = 'pindex.html';
    } else {
        alert('Please select a user type');
    }
});
