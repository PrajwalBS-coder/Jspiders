let signup=document.getElementById('signup')
let closebtn=document.getElementById('closebutton')
console.log(closebtn.textContent);
signup.addEventListener('click',function(){
    console.log("clicked")

    signup.setAttribute('data-bs-target','#exampleModal');
    signup.setAttribute('data-bs-toggle','modal')
    //signup.style.display = 'none';
    


});
closebtn.addEventListener('click',function(){
    signup.style.display = 'none';

})

