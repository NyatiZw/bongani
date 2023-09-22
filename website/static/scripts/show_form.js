document.addEventListener('DOMContentLoaded', function() {
    //Listening to button click
    const startButton = document.getElementById('startButton');
    const loginForm = document.getElementById('loginForm');

    startButton.addEventListener('click', function() {
        loginForm.style.display = 'block';
    });
});
