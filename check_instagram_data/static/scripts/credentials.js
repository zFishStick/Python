function saveCredentials() {
    const username = document.getElementById('username').getAttribute('data-username');
    const password = document.getElementById('password').getAttribute('data-password');
    sessionStorage.setItem('username', username);
    sessionStorage.setItem('password', password);
    window.location.href = "/operations";
}

saveCredentials();
