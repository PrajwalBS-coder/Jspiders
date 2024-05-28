var e = document.getElementById("s");
var fees = document.getElementById("fees")
var feesdeduction=document.getElementById("dedfees")
var payfees=document.getElementById("payfees")
var payfeesdeduction=document.getElementById("remainingfees")
var submit=document.getElementById("finalfees")
function onChange() {
    var value = e.value;
    var text = e.options[e.selectedIndex].text;
    //console.log(value, text);
    if (text === "Python") {
        fees.value = 35590
    }
    else if (text === "Java") {
        fees.value = 36000
    }
    else if (text === "MERN") {
        fees.value = 30000
    }
    else if (text === "DevOps") {
        fees.value = 25000
    }

}
e.onchange = onChange;
//onChange();

 
document.addEventListener('input',(e)=>{

    if(e.target.getAttribute('name')=="caste")
    console.log(e.target.value)
if(e.target.value==="OBC")
    {
feesdeduction.value=5000;
    }
    else if(e.target.value==="GROUP 1")
        {
            feesdeduction.value=2000; 
        }
    })

submit.addEventListener("click",function(){
    console.log(fees.value)
    console.log(feesdeduction.value)
    console.log(payfees)
    payfeesdeduction.value=fees.value-feesdeduction.value-payfees.value;

})



    //payfeesdeduction.value=fees.value-feesdeduction.value-payfees


