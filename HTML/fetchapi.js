function displayData(country) {
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
                <h3>${(item.population / 1000000).toFixed(2)} M People</h3>
                <h4>${item.region}</h4>
                </div>
            </div>
        </div>`;
        let output = document.getElementById("output");
        // output.innerHTML = eachcountry;
    }
    document.getElementById('output').insertAdjacentHTML('beforeend', eachcountry);

}



function getCountryData() {
    fetch('https://restcountries.com/v3.1/name/bharat').then
        ((respone) => {
            return respone.json()
        }).then((data) => {
            displayData(data)
            return fetch('https://restcountries.com/v3.1/name/usa')
        }).then((respone) => {
            return respone.json()
        }).then((data) => {
            displayData(data)
            return fetch('https://restcountries.com/v3.1/name/uk')
        }).then((respone) => {
            return respone.json()
        }).then((data) => {
            displayData(data)


        })


        .catch((err) => {
            console.error(err)
        })
}
getCountryData();