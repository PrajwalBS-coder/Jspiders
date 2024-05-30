getbutton = document.getElementById("data")
//console.log(getbutton.innerText)
display = document.getElementById("display")
//display.addEventListener("click", getdata);

function getdata(c) {
    let xhr = new XMLHttpRequest()
    console.log("loaded")
    xhr.open('GET', `https://dog.ceo/api/breed/${c}/images/random`, true)
    xhr.send()
    xhr.addEventListener("load", function () {
        let country = JSON.parse(xhr.responseText);
        console.log("onload")
        console.log(country)

        let eachcountry = ``;
        
            eachcountry += ` <div class="col-md-3">
                <div class="card" >
                    <div class="cardheader">
                        <img src=${country.message} alt="${country.message}" class="">
                    </div>
                    
                </div>
            </div>`;
            let output = document.getElementById("output");
       // output.innerHTML = eachcountry;
        
        document.getElementById('output').insertAdjacentHTML('beforeend',eachcountry);
        
    })

}
getdata(prompt("Enter Dog Breed"))
