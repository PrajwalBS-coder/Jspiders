let min = document.getElementById('min');
let sec = document.getElementById('sec');
let msec = document.getElementById('msec');
//BUTTONS
let start = document.getElementById('start');
let stop = document.getElementById('stop');
let restart = document.getElementById('reset')

//intial values
min.textContent = "00"
sec.textContent = "00"
msec.textContent = "00"

let tmin=0
let tsec=0
let tmsec=0
//

let temp=false
//timer fucntion
function time() {
    tmsec = tmsec + 10;
    if (tmsec === 1000) {
        tsec = tsec + 1;
        tmsec = 0;
    }
    if (tsec === 60) {
        tmin = tmin + 1
        tsec = 0
    }


    //settting values
    min.textContent = con(tmin)
    sec.textContent = con(tsec)
    msec.textContent = con(Math.trunc(tmsec/100))


}
//concat of zero
function con(time){
    if(time<=9)
        return "0"+time
    else
    return time
}
let interval=null;





start.addEventListener('click', () => {
    if(!temp){
        interval=setInterval(time,10);
        temp=true;
    }
})


//stop
stop.addEventListener('click', () => {
    if(temp){
        clearInterval(interval);
        temp=false;
    }
});

restart.addEventListener("click",()=>
{
  clearInterval(interval);
  temp=false
  tmin=0;
  tsec=0;
  tmsec=0;
  min.textContent = "00";
  sec.textContent = "00";
  msec.textContent = "00";
});
