function displayData(country) {
    let eachcountry = ``;
    
        eachcountry += ` <div class="col-md-3">
            <div class="card" >
                <div class="cardheader">
                    <img src=${country.message} alt="not found" class="">
                </div>
                
                </div>
            </div>
        </div>`;
        let output = document.getElementById("output");
        // output.innerHTML = eachcountry;
    
    document.getElementById('output').insertAdjacentHTML('beforeend', eachcountry);

}

function makeAjaxCall(country) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', `https://dog.ceo/api/breeds/image/random`, true);
    xhr.send();
    return xhr;
}

function getCountryData() {
    let req1 = makeAjaxCall('bharat');
    req1.addEventListener('load', function () {
        let data = JSON.parse(req1.responseText);
        displayData(data);

        //Make Ajax Call For Usa
        let req2 = makeAjaxCall('usa');
        req2.addEventListener('load', function () {
            let data = JSON.parse(req2.responseText);
            displayData(data);

            //make Ajax Call For Brazil
            let req3 = makeAjaxCall('brazil');
            req3.addEventListener('load', function () {
                let data = JSON.parse(req3.responseText);
                displayData(data);
            })
        })
    })
}
getCountryData();