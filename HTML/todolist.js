let formid = document.getElementById('form')
formid.addEventListener('submit', function (e) {
    e.preventDefault();
    var task = document.getElementById('task');
    //console.log(name.value)
    tasklist = localStorage.getItem('todolist') ? JSON.parse(localStorage.getItem('todolist')) : [];
    console.log(tasklist)
    if (task.value != '') {
        tasklist.unshift(task.value);
        localStorage.setItem('todolist', JSON.stringify(tasklist));
    }
    else {
        console.log('eere')
    }

    console.log(JSON.parse(localStorage.getItem('todolist')))
    task.value = '';
    otput()


});
//Dispaly
function otput() {
    display = document.getElementById('output');
    let listoftask = ``;
    tasklist = localStorage.getItem('todolist') ? JSON.parse(localStorage.getItem('todolist')) : [];
    console.log(tasklist, tasklist.length)
    if (tasklist.length!=0) {
        console.log("enter")

        for (let task of tasklist) {

            listoftask += `<li class="list-group-item mb-4"> <span>${task}</span> <i class="bi bi-pen float-end"></i>    <i class="bi bi-trash3 float-end"> </i> </li> `
        }
        display.innerHTML = listoftask;
    }
    else {
        listoftask += ``
        display.innerHTML = listoftask;
    }


}

//Deleting
eventtag = document.getElementById('output');
eventtag.addEventListener('click', function (e) {

    let targetele = e.target;
    console.log(targetele)
    //console.log(targetele.classList)
    if (targetele.classList.contains('bi-trash3')) {
        let actuallele = targetele.parentElement;
        console.log(actuallele)
        let realtext = actuallele.innerText;
        console.log(realtext)

        let tasklist = localStorage.getItem('todolist') ? JSON.parse(localStorage.getItem('todolist')) : [];
        tasklist = tasklist.filter((value) => {
            return value != realtext
        })
        localStorage.setItem('todolist', JSON.stringify(tasklist))
        otput();
    }
});

