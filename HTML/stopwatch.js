let min = document.getElementById('min');
let sec = document.getElementById('sec');
let msec = document.getElementById('msec');
//BUTTONS
let start = document.getElementById('start');
let stop = document.getElementById('stop');
let restart = document.getElementById('reset')

//intial values
let tmin = 19
let tsec = 59
let tmsec = 59000

min.textContent = tmin
sec.textContent = tsec
msec.textContent = tmsec / 1000;


//

let temp = false
//timer fucntion
function time() {
    //tmsec=1000;
    tmsec = tmsec - 10;
    if (tmsec === 0) {
        tsec = tsec - 1;
        tmsec = 60000;
    }
    if (tsec === 60) {
        tmin = tmin - 1
        tsec = 0
    }


    //settting values
    min.textContent = con(tmin)
    sec.textContent = con(tsec)

    msec.textContent = con((Math.trunc(tmsec / 1000)))


}
//concat of zero
function con(time) {
    if (time <= 9)
        return "0" + time
    else
        return time
}
let interval = null;





start.addEventListener('click', () => {
    if (!temp) {
        interval = setInterval(time, 10);
        temp = true;
    }
})


//stop
stop.addEventListener('click', () => {
    if (temp) {
        clearInterval(interval);
        temp = false;
    }
});

restart.addEventListener("click", () => {
    clearInterval(interval);
    let tmin = 19
    let tsec = 59
    let tmsec = 59000

    min.textContent = tmin
    sec.textContent = tsec
    msec.textContent = tmsec / 1000;
});
