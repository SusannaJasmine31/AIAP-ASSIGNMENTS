// Login Form Validation Script

function validateLoginForm(event) {
    // Prevent form submission
    event.preventDefault();
    
    // Get form elements
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const errorMessage = document.getElementById('error-message');
    
    // Clear previous error messages
    errorMessage.textContent = '';
    errorMessage.style.display = 'none';
    
    // Validate username
    if (username === '') {
        showError('Username cannot be empty');
        return false;
    }
    
    // Validate password
    if (password === '') {
        showError('Password cannot be empty');
        return false;
    }
    
    // If validation passes, send to Flask backend
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showSuccess(data.message);
        } else {
            showError(data.message);
        }
    })
    .catch(error => {
        showError('An error occurred. Please try again.');
        console.error('Error:', error);
    });
    
    return false;
}

function showError(message) {
    const errorMessage = document.getElementById('error-message');
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    errorMessage.style.color = '#e74c3c';
    errorMessage.style.padding = '10px';
    errorMessage.style.marginTop = '10px';
    errorMessage.style.borderRadius = '4px';
    errorMessage.style.backgroundColor = '#fadbd8';
}

function showSuccess(message) {
    const errorMessage = document.getElementById('error-message');
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    errorMessage.style.color = '#27ae60';
    errorMessage.style.padding = '10px';
    errorMessage.style.marginTop = '10px';
    errorMessage.style.borderRadius = '4px';
    errorMessage.style.backgroundColor = '#d5f4e6';
}

// Attach event listener when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', validateLoginForm);
    }
});
