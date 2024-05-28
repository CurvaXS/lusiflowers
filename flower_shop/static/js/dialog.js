
let input = document.getElementById('dialog-input')
input.addEventListener('click', (e) => {
    input.classList.remove('active')
})
if (input.value == '') {
    input.classList.add('active')
}

dialog = document.querySelector('.dialog')

function create_dialog() {
    dialog.classList.add('dialog-transition')
    dialog.style.right = `5px`;
    setTimeout(function () {
        interval();
    }, 1200)
}

function close_dialog() {
    dialog.classList.add('dialog-transition-back')
    dialog.style.right = `-240px`;
    setTimeout(function () {
        interval();
    }, 1200)
}

function interval() {
    if (document.querySelector('.dialog-transition')) {
        dialog.classList.remove('dialog-transition')
    }
    if (document.querySelector('.dialog-transition-back')) {
        dialog.classList.remove('dialog-transition-back')
    }
}

let clickMe = document.querySelector('.click-me')
clickMe.addEventListener('click', create_dialog)

let TechSupport_btn = document.querySelector('#TechSupport')
TechSupport.addEventListener('click', create_dialog)

let closeMe = document.querySelector('.dialog-close')
closeMe.addEventListener('click', close_dialog)
