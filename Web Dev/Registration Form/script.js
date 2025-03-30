document.querySelector('#registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let password = document.getElementById('password').value;
    let confirmPassword = document.getElementById('confirmPassword').value;
    let dob = document.getElementById('dob').value;
    let state = document.getElementById('state').value;

    if (!dob) {
        alert('Please enter your Date of Birth.');
        return;
    }

    if (state === "") {
        alert('Please select your State.');
        return;
    }

    if (password !== confirmPassword) {
        alert('Passwords do not match.');
        return;
    }

    alert('Registration successful!');
    this.reset();
});
