
let p = new Promise(function (resloved, rejected) {
    let country=prompt("Enter country")
    let xhr = new XMLHttpRequest()
    console.log("loaded")
    xhr.open('GET', `https://restcountries.com/v3.1/name/${country}`)
    xhr.send()
    xhr.onload =()=>
    {
        if (xhr.statusText === "OK") {
            console.log(xhr.responseText)
            resloved(xhr.responseText)
        }
        else {
            rejected("WRONG LINK")
        }
    }
});

p.then((data) => {
    let country = JSON.parse(data);
    console.log("onload")
    console.log(country)

    let eachcountry = ``;
    for (let item of country) {
        eachcountry += ` <div class="col-md-3">
            <div class="card" >
                <div class="cardheader">
                    <img src=${item.flags.png} alt="not found" class="">
                </div>
                <div class="cardbody text-center">
                <h3>${item.name.common}</h3>
                <h5>${item.capital[0]}</h5>
                <h3>${(item.population/1000000).toFixed(2)} M People</h3>
                <h4>${item.region}</h4>
                </div>
            </div>
        </div>`;
        let output = document.getElementById("output");
   // output.innerHTML = eachcountry;
    }
    document.getElementById('output').insertAdjacentHTML('beforeend',eachcountry);

}).catch((err) => {
    console.log(err)
})

