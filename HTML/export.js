//let n = Number(prompt("Enter the no"))

/*function mulfun() {
    for (let i = 1; i <= 10; i++) {
        console.log(`${n} * ${i}=${n * i}`);
    }

}
*/
function getdata() {
    let na = prompt("NAME")
    let age = prompt("Age")
    console.log(`Name is ${na} and birth year is ${age}`)
    return age;
}

function calcage(age) {
    return new Date().getFullYear() - age;
}


export function prime() {
    let n = Number(prompt("ENter A no"))
    for (let i = 2; i <= n; i++) {
       
        let c=0
       for(let j=2;j<i;j++)
        {
            if(i%j===0)
                c+=1
           
            
          
        }

        if(c==0){
            console.log(i)
        }

    
        }


    }

    //export default mulfun;//we can pass only one default export in js

    export { getdata, calcage }//named export all at once