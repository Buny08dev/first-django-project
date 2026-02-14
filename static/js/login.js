function toggleForms() {
    const loginBox = document.getElementById('signin-box');
    const signupBox = document.getElementById('signup-box');
    
    loginBox.classList.toggle('hidden');
    signupBox.classList.toggle('hidden');
    
    // URL manziliga belgi qo'yamiz
    if (loginBox.classList.contains('hidden')) {
        window.location.hash = 'signup';
    } else {
        window.location.hash = 'login';
    }
}

// Sahifa yangilanganda URL hash-ga qarab to'g'ri blokni ko'rsatish
window.addEventListener('DOMContentLoaded', (event) => {
    if (window.location.hash === '#signup') {
        document.getElementById('signin-box').classList.add('hidden');
        document.getElementById('signup-box').classList.remove('hidden');
    }
});