function valid() {
    let name = document.getElementById("name")
    let email = document.getElementById("Email")
    let password = document.getElementById("pwd")
    let password2 = document.getElementById("cpwd")
    let vname=isemptyandlength(name, name.value);
    let vemail=empty(email,email.value)
    let vpass=isemptyandlength(password,password.value)
    let vcpass=isvalidpass(password2,password2.value,password.value)

    if(vname && vemail &&vpass&&vcpass)
        {
            return true
        }
        else{
            return false
        }

}
function isemptyandlength(ele, val) {
    if (val === "" || val.length<=4) {

        console.log(val.length)
        //alert("NAME SHOULD  not empty")
        error(ele,"red")
        return false

    }
    else
    {
        isname(ele, val)
        return true
    }

}
function empty(ele,val)
{
    if(val==="")
        {
            //console.log(val.length)
        //alert("NAME SHOULD  not empty")
        error(ele,"red")
        return false
        }
        else{
            error(ele,"green");
            return true

        }

}



function isname(ele, val) {
    if (/^[a-zA-Z ]+$/.test('val')) {
        error(ele,"green");
        return true
       
    }
    else {
        error(ele, "red")
        return false
    }

}

function isvalidpass(pass,val,val2)
{
    if(val==="" || val2!==val)
        {
            //console.log(val.length)
        //alert("NAME SHOULD  not empty")
        error(pass,"red")
        return false
        }
        else{
            error(pass,"green");
            return true

        }




}


function error(ele, clr) {
    ele.style.border = `2px solid${clr} `
    ele.style.boxShadow = `0 0 12px ${clr}`
}
