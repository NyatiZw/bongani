document.addEventListener('DOMContentLoaded', function() {
    //Listening to button click
    const startButton = document.getElementById('startButton');
    const loginForm = document.getElementById('loginForm'); // Reference to the login form

    startButton.addEventListener('click', function() {
        loginForm.style.display = 'block'; // Show the login form
    });

    const registerButton = document.getElementById('registerButton');

    registerButton.addEventListener('click', function() {
	    //Redirect to registration.html
	    window.location.href = '/sign-up';
    });

    const loginButton = document.getElementById('loginButton');

    loginButton.addEventListener('click', function() {
        const username = document.getElementById('username');
        const password = document.getElementById('password');

        const request_login_data = {
            username: username.value,
            password: password.value
        };
        
        fetch('/template/home_drivers.html', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(request_login_data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Handle authentication result
            if (data.success) {
                // Authentication successful, check user role
                const userRole = data.role;

		if (userRole == 'driver') {
			//Redirect to home_drivers.html for drivers
			window.location.href = 'home_drivers.html';
		} else if (userRole == 'parent') {
			//Redirect to home_parents for parents
			window.location.href = 'home_parents.html';
		}
            } else {
                // Authentication failed, display an error message
                console.log('Login failed');
            }
        })
        .catch(error => {
            console.error('Error: ', error);
        });
    });
});
