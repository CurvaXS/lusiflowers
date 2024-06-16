

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function setItem(name, price, photo_url){
    let item = document.createElement('div');
    item.classList.add('item');
    item.innerHTML = `
        <img src="${photo_url}" alt="">
        <div class="item-info">
            <p class="item-name">${name}</p>
            <span>Бесплатная доставка через 2 ч с 10:00 до 20:00</span>
            <p class="item-price">${price}</p>
        </div>
    `;
    return item;
}


const csrftoken = getCookie('csrftoken');

document.getElementById('show-more-btn-autors').addEventListener('click', function () {
    const csrftoken = getCookie('csrftoken');
    fetch('/show-more/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json', // Убедитесь, что тип контента установлен правильно
            // Если вы отправляете какие-либо данные в запросе, добавьте их здесь
        }
    })
        .then(response => {
            if (response.ok) {
                if (response.headers.get('Content-Type').includes('application/json')) {
                    return response.json();
                } else {
                    throw new Error('Expected JSON response but got something else');
                }
            } else {
                throw new Error('Network response was not ok');
            }
        })
        .then(data => {
            if (data.more_items) {
                let div = document.querySelector('#autors_bucket_items');
                data.more_items.forEach(item => {
                    let el = setItem(item.name, item.price, item.photo_url);
                    div.appendChild(el);
                });
            } else {
                this.disabled = true;
            }
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
        });
});

document.getElementById('show-more-btn-compositions').addEventListener('click', function () {
    const csrftoken = getCookie('csrftoken');
    fetch('/show-more-compositions/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json', // Убедитесь, что тип контента установлен правильно
            // Если вы отправляете какие-либо данные в запросе, добавьте их здесь
        }
    })
        .then(response => {
            if (response.ok) {
                if (response.headers.get('Content-Type').includes('application/json')) {
                    return response.json();
                } else {
                    throw new Error('Expected JSON response but got something else');
                }
            } else {
                throw new Error('Network response was not ok');
            }
        })
        .then(data => {
            if (data.more_items) {
                let div = document.querySelector('#compositions_items');
                data.more_items.forEach(item => {
                    let el = setItem(item.name, item.price, item.photo_url);
                    div.appendChild(el);
                });
            } else {
                this.disabled = true;
            }
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
        });
});

document.getElementById('show-more-btn-busket').addEventListener('click', function () {
    const csrftoken = getCookie('csrftoken');
    fetch('/show-more-busket/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json', 
        }
    })
        .then(response => {
            if (response.ok) {
                if (response.headers.get('Content-Type').includes('application/json')) {
                    return response.json();
                } else {
                    throw new Error('Expected JSON response but got something else');
                }
            } else {
                throw new Error('Network response was not ok');
            }
        })
        .then(data => {
            if (data.more_items) {
                let div = document.querySelector('#busket_items');
                data.more_items.forEach(item => {
                    let el = setItem(item.name, item.price, item.photo_url);
                    div.appendChild(el);
                });
            } else {
                this.disabled = true;
            }
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
        });
});