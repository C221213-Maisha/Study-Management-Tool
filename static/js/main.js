// main.js

document.getElementById('signup-form').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Sign-Up form submitted');
});

document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Log-In form submitted');
});

// main.js

document.querySelectorAll('.feature-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.classList.add('animate__pulse');
    });

    card.addEventListener('mouseleave', () => {
        card.classList.remove('animate__pulse');
    });
});
