const numbers = [1, 2];
/*
1 - orel
2 - reshka
*/

flag = true;

let roundCounter = 0
let boolRoundCounter = true
let altRoundCounter = 0

let step_1 = document.querySelector('.step-1')
let step_2 = document.querySelector('.step-2')
let step_3 = document.querySelector('.step-3')
let step_4 = document.querySelector('.step-4')
let step_5 = document.querySelector('.step-5')
let step_6 = document.querySelector('.step-6')
let step_7 = document.querySelector('.step-7')
let steps = document.querySelectorAll('.step')

let container_result = document.querySelector('.container__result')
const coin = document.querySelector('.coin')
let winValue = document.querySelector('.win-value')
let round = document.querySelector('.round__number')
let ratio = document.querySelector('.ratio__v')
let infMess = document.querySelector('.info_messgaes')
let grabButton = document.querySelector('#grab_button')

function check() {
    input_bet.classList.remove('bet__error')
    bet = document.querySelector('#bet').value
    if (bet == 0 || bet < 0) {
        flag = false;
    }
}


function waiting() {
    coin.classList.add('coin__animate')
}


function ManipulateWithElements() {

}


function getRandomNumber(rc) {

    let ratioIndex = 1.95

    const randomIndex = Math.floor(Math.random() * numbers.length);
    number = numbers[randomIndex];
    //number = 1;
    choise = document.querySelector('[name="choise"]').id
    if (choise == "orel" && number == 1 || choise == "reshka" && number == 2) {

        step_1.classList.remove('step__fail')
        step_1.classList.remove('step__background')
        step_1.classList.add('step__success')


        rc += 1
        if (rc == 1) { PlayOrTake(rc, 1.95, bet) }// 1
        if (rc == 2) { PlayOrTake(rc, 2.5, bet) } // 2
        if (rc == 3) { PlayOrTake(rc, 3.1, bet) } // 3
        if (rc == 4) { PlayOrTake(rc, 3.9, bet) } // 4
        if (rc == 5) { PlayOrTake(rc, 4.5, bet) } // 5
        if (rc == 6) { PlayOrTake(rc, 5, bet) }   // 6
        if (rc == 7) { PlayOrTake(rc, 10, bet) }  // 7
    }
    else {
        winValue.innerHTML = `${bet * 0}`
        /*
        step_1.classList.remove('step__success')
        step_1.classList.remove('step__background')
        step_1.classList.add('step__fail')
        */

        steps[rc].classList.remove('step__success')
        steps[rc].classList.remove('step__background')
        steps[rc].classList.add('step__fail')

        infMess.classList.remove('info_messgaes-suc')
        infMess.classList.add('info_messgaes-err')
        infMess.innerHTML = 'Поражение'

        return rc;
    }

    console.log(number);
    console.log(choise);
    console.log(roundCounter)

}

function PlayOrTake(rc, ri, bet) {
    round.innerHTML = rc
    ratio.innerHTML = ri

    let wb = bet * ri
    winValue.innerHTML = wb

    infMess.classList.remove('info_messgaes-err')
    infMess.classList.add('info_messgaes-suc')
    infMess.innerHTML = 'Продолжи игру или забери приз!'

    steps[rc-1].classList.remove('step__fail')
    steps[rc-1].classList.remove('step__background')
    steps[rc-1].classList.add('step__success')

    if (rc==7){
        alert('Вы победили!')
    }
/*
    if (rc == 1) {

    }// 1
    if (rc == 2) { } // 2
    if (rc == 3) { } // 3
    if (rc == 4) { } // 4
    if (rc == 5) { } // 5
    if (rc == 6) { }   // 6
    if (rc == 7) { }  // 7
*/
    grabButton.addEventListener('click', function () {
        console.log(steps)
    })
    altRoundCounter = rc; 
    return altRoundCounter;
}


function Main() {
    //roundCounter = 0
    if (boolRoundCounter == false) {
        step_1.classList.remove('step__success')
        step_1.classList.remove('step__fail')
        step_1.classList.add('step__background')
        round.innerHTML = roundCounter
    }

    /* нужна функция деактивирующая кнопку вывода до результата */

    input_bet = document.querySelector('#bet')

    check()

    if (flag == false) {
        flag = true;

        input_bet.classList.add('bet__error')
        return;
    }


    else {
        waiting()

        infMess.classList.remove('info_messgaes-suc')
        infMess.classList.remove('info_messgaes-err')
        infMess.innerHTML = ' '

        /* всё что выше можно не трогать*/

        //ManipulateWithElements()

        
        setTimeout(function () {
            getRandomNumber(roundCounter);
            if (getRandomNumber(roundCounter) == 0) {
                boolRoundCounter = false
            }
            else {
                boolRoundCounter = true
                roundCounter = altRoundCounter
            }
            coin.classList.remove('coin__animate')
        }, 3);


    }

}


/*
const startButton = document.getElementById('start_coinflip');
startButton.addEventListener('click', Main);
*/

let or = document.querySelector('#orel')
or.addEventListener('click', Main);

let re = document.querySelector('#reshka')
re.addEventListener('click', Main);






