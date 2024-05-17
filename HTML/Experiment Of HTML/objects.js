let obj = document.getElementById("obj")
let add_button = document.getElementById("add")
let details = {
    name: "Jhon",
    age: 25,
    address: "New York"
};
//onload(localStorage("person1",details))
add_button.addEventListener("click", function () {
    localStorage.setItem("person1", JSON.stringify(details));

})

let info=localStorage.getItem("person1")
add_button.addEventListener("dblclick",function(){
   console.log(JSON.parse(info));
   let p1=JSON.parse(info)
   console.log(p1.name);
})
