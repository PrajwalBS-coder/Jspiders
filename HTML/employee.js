let employees = [{ "id": 1, "first_name": "Wendye", "last_name": "Somerled", "email": "wsomerled0@amazon.co.jp", "gender": "Female", "country": "Thailand" },
{ "id": 2, "first_name": "Chas", "last_name": "Kermit", "email": "ckermit1@soup.io", "gender": "Male", "country": "Indonesia" },
{ "id": 3, "first_name": "Pauli", "last_name": "Tracey", "email": "ptracey2@chron.com", "gender": "Female", "country": "Brazil" },
{ "id": 4, "first_name": "Perle", "last_name": "Abbyss", "email": "pabbyss3@nytimes.com", "gender": "Female", "country": "Poland" },
{ "id": 5, "first_name": "Nicolai", "last_name": "Muskett", "email": "nmuskett4@ning.com", "gender": "Male", "country": "Japan" },
{ "id": 6, "first_name": "Anselm", "last_name": "Brandel", "email": "abrandel5@dagondesign.com", "gender": "Male", "country": "Poland" },
{ "id": 7, "first_name": "Nissie", "last_name": "Sinnie", "email": "nsinnie6@blogs.com", "gender": "Female", "country": "France" },
{ "id": 8, "first_name": "Trix", "last_name": "O'Spillane", "email": "tospillane7@unblog.fr", "gender": "Female", "country": "United States" },
{ "id": 9, "first_name": "Celka", "last_name": "Fanshawe", "email": "cfanshawe8@hibu.com", "gender": "Female", "country": "Malaysia" },
{ "id": 10, "first_name": "Sloane", "last_name": "Coneybeer", "email": "sconeybeer9@springer.com", "gender": "Male", "country": "Macedonia" }];


//Display Employees

function displayEmployees(emps) {
    if (emps.length >= 1) {
        let eachEmp = ``;
        emps.forEach((emp) => {
            eachEmp += `<tr>
            <td>${emp.id}</td>
            <td>${emp.first_name}</td>
            <td>${emp.last_name}</td>
            <td>${emp.email}</td>
            <td>${emp.gender}</td>
            <td>${emp.country}</td>
        </tr>`;
        });

        document.querySelector('#display').innerHTML = eachEmp;
    }
}


let allEmpsBtn = document.querySelector('#all-emps');
allEmpsBtn.addEventListener('click', () => {
    displayEmployees(employees);
})


let MlEmpsBtn = document.querySelector('#Ml-Emps');
MlEmpsBtn.addEventListener('click', () => {
    let MaleEmployees = employees.filter(emp => emp.gender === 'Male');
    displayEmployees(MaleEmployees);
})


let FmlEmpsBtn = document.querySelector('#Fml-Emps');
FmlEmpsBtn.addEventListener('click', () => {
    let FemaleEmployees = employees.filter(emp => emp.gender === 'Female');
    displayEmployees(FemaleEmployees);
});



//Search by name
let searchbyname = document.getElementById('SrchByFstName')
searchbyname.addEventListener('keyup', function () {
    let val = searchbyname.value;
    let filterednames = displaysearch(val, employees)
    console.log(val)

    if (val.length == ' ') {
        //document.querySelector('#display').innerHTML = "NO ROWS ";
        displaynullEmployees();

    }
    else {
        displayEmployees(filterednames)

    }


});
function displaysearch(v, emp) {
    v = v.toUpperCase().trim();
    let original_name = '';
    let filtered_names = [];

    for (let e of emp) {
        original_name = e.first_name.toUpperCase().trim();

        if (original_name.includes(v)) {
            filtered_names.push(e);
        }
        else
        {
            displaynullEmployees();
        }
    }
    return filtered_names;

}

//using filter functions
//let searchusingfilter=document.getElementById('search');




//using startswith
let searchusingstartswith = document.getElementById('search');
searchusingstartswith.addEventListener('keyup', function () {
    let val = searchusingstartswith.value;
    let filterednames = displaysearch_bystartswith(val, employees)
    console.log(val)

    if (val.length == ' ') {
        //document.querySelector('#display').innerHTML = "NO ROWS ";
        displaynullEmployees();

    }
    else {
        displayEmployees(filterednames)

    }


});
function displaysearch_bystartswith(v, emp) {
    v = v.toUpperCase().trim();
    let original_name = '';
    let filtered_names = [];

    for (let e of emp) {
        original_name = e.first_name.toUpperCase().trim();

        if (original_name.startsWith(v)) {
            filtered_names.push(e);
        }
        else {
            //document.querySelector('#display').innerHTML = "NO ROWS ";
            displaynullEmployees();

        }
    }
    return filtered_names;

}

function displaynullEmployees() {
    eachEmp=``;
   
            eachEmp += `<tr>
            <td>no data</td>
            <td>no data</td>
            <td>no data</td>
            <td>no data</td>
            <td>no data</td>
            <td>no data</td>
        </tr>`;
        

        document.querySelector('#display').innerHTML = eachEmp;
}
    
