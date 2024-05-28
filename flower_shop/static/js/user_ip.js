fetch('https://api.ipify.org?format=json')
    .then(response => response.json())
    .then(data => {
        let input = document.body.querySelector('#ip')
        input.value = data.ip
    })
    .catch(error => console.error(error))



let username = document.querySelector('.username').textContent;
let email = document.querySelector('.userEmail').textContent;

let usernameInput = document.querySelector('#name');
let emailInput = document.querySelector('#email');

usernameInput.value = username
emailInput.value = email
