let formid = document.getElementById('form')
formid.addEventListener('submit', function (e) {
    e.preventDefault();
    var task = document.getElementById('task');
    console.log(task.value)
    tasklist = localStorage.getItem('todolist') ? JSON.parse(localStorage.getItem('todolist')) : [];
    // console.log(tasklist)
    if (task.value != '') {
        tasklist.push(task.value);
        localStorage.setItem('todolist', JSON.stringify(tasklist));
    }
    else {
        // console.log('eere')
    }

    //console.log(JSON.parse(localStorage.getItem('todolist')))
    task.value = '';
    otput()


});
//Dispaly
function otput() {
    display = document.getElementById('output');
    let listoftask = ``;
    tasklist = localStorage.getItem('todolist') ? JSON.parse(localStorage.getItem('todolist')) : [];
    //console.log(tasklist, tasklist.length)
    if (tasklist.length != 0) {
        console.log("enter")

        for (let task of tasklist) {

            listoftask += `<li class="list-group-item mb-4"> <span>${task}</span> <i class="bi bi-pen float-end" id="update" data-bs-toggle= 'modal' data-bs-target='#exampleModal'   ></i> <i class="bi bi-trash3 float-end" > </i> </li> `
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
    //console.log(targetele)
    //console.log(targetele.classList)
    if (targetele.classList.contains('bi-trash3')) {
        let actuallele = targetele.parentElement;
        //console.log(actuallele)
        let realtext = actuallele.innerText;
        //console.log(realtext)

        let tasklist = localStorage.getItem('todolist') ? JSON.parse(localStorage.getItem('todolist')) : [];
        tasklist = tasklist.filter((value) => {
            return value != realtext
        })
        localStorage.setItem('todolist', JSON.stringify(tasklist))
        otput();
    }
});



///updation


eventtag = document.getElementById('output');
eventtag.addEventListener('click', function (e) {

    let targetele = e.target;
    console.log(targetele)
    //console.log(targetele.classList)
    if (targetele.classList.contains('bi-pen')) {
        let actuallele = targetele.parentElement;
        console.log(actuallele)
        let realtext = actuallele.innerText;
        console.log(realtext)
        let tasklist = localStorage.getItem('todolist') ? JSON.parse(localStorage.getItem('todolist')) : [];
        let ind = tasklist.indexOf(realtext);
        console.log(ind);
        //alteration(ind,realtext);


        //function updation
        //let tasklist= localStorage.getItem('todolist') ? JSON.parse(localStorage.getItem('todolist')) : [];

        let tg = ``;
        let show = document.getElementById('update')
        //show.setAttribute('data-bs-target','#exampleModal')
        //console.log(showdata.textContent);
        //console.log(task)
        //load();
        console.log(realtext)
        tg += `<div class="modal fade" id="exampleModal" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Please Fillout For Registration</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                    <div class="modal-body">
                        <form>
                        <form class="col-md-12 " id="form">
                        <input type="text" class="form-control input-group mb-2 "
                            aria-label="Text input with checkbox" autocomplete="on" id="exist"  >
                        
                        <input type="text" class="form-control input-group mb-2 "
                            aria-label="Text input with checkbox" id="uadd">
                        <input type="submit" name="" id="add" class="btn btn btn-dark m-auto" data-bs-dismiss="modal" >
                    </form>
                        
                    </div>
                    
                </div>
            </div>
            </div>`;
            
//////////Updating array and local storage            
       
        let formid = document.getElementById('form');
        let additem=document.getElementById('add')
        var task = document.getElementById('uadd');
        let data=document.getElementById('exist')
            data.value=tasklist[ind];
            console.log(data.value);
           
            console.log(ind)
        console.log(task.value)
        console.log('Near Update',ind)
        pos=ind;
        additem.addEventListener('click', function (e) {

            e.preventDefault();
           console.log("addd")
           // var task = document.getElementById('task');
            console.log(task.value)
            //
            console.log(pos)
            tasklist = localStorage.getItem('todolist') ? JSON.parse(localStorage.getItem('todolist')) : [];
            // console.log(tasklist)
            if (task.value != '') {
                if (ind !== -1) {
                    console.log(ind,task.value)
                    tasklist[pos] = task.value;
                }
                localStorage.setItem('todolist', JSON.stringify(tasklist));
                task.value="";
                //ind=-1;
                otput()
                

            }
           
    }); 
    show.innerHTML = tg;
        //console.log(val.value)

    }
});


/*Function OF Updation
function alteration(ind,task){
    let tasklist= localStorage.getItem('todolist') ? JSON.parse(localStorage.getItem('todolist')) : [];

    let tg = ``;
       let show=document.getElementById('update')
        //console.log(showdata.textContent);
        console.log(task)
        //load();
        tg += `<div class="modal fade" id="exampleModal" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Please Fillout For Registration</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                    <div class="modal-body">
                        <form>
                            <input type="text" class="form-control" placeholder="ENter Your name" value=${task} ><br>
                            <input type="text" class="form-control" placeholder="ENter Updation Task" id="newval"><br>
                          
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" id="closebutton" data-bs-dismiss="modal">Save
                            changes</button>
                    </div>
                </div>
            </div>
            </div>`;

            val=document.getElementById('newval')
           // console.log(val.value)
            if (show.innerHTML = tg) {
                console.log("showdata")
            }
            else {
                console.log("NOT POSSIBLE")
            };


}


function load() {
    eventtag = document.getElementById('update');
    eventtag.setAttribute('data-bs-target', '#exampleModal');
    eventtag.setAttribute('data-bs-toggle', 'modal')
}
*/
