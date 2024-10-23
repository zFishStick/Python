const username = sessionStorage.getItem('username')
const password = sessionStorage.getItem('password')

function showUser() {
    let h1 = document.getElementById('user-welcome');
    h1.textContent = "Ciao " + username + " ! Scegli l'operazione che vuoi eseguire";
}

showUser()

function getFollowers() {
    console.log(username, password);
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/get_followers", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.onload = function () {
        if (xhr.status === 200) {
            console.log(xhr.responseText);
        }
    };
    xhr.send(JSON.stringify({ username: username, password: password }));

}


function getFollowees(params) {

}

function getNotFollowees(params) {

}

function getNotFollowers(params) {

}