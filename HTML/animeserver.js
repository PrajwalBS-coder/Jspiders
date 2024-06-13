getbutton = document.getElementById("data")
//console.log(getbutton.innerText)
display = document.getElementById("display")
//display.addEventListener("click", getdata);

function getdata(c) {
    let xhr = new XMLHttpRequest()
    console.log("loaded")
    xhr.open('GET', `https://api.jikan.moe/v4/anime?q=naruto&sfw`, true)
    xhr.send()
    xhr.addEventListener("load", function () {
        let anime = JSON.parse(xhr.responseText);
        console.log("onload")
        console.log(anime)

        let eachcountry = ``;
        
            eachcountry += ` <div class="col-md-3">
                <div class="card" >
                    <div class="cardheader">
                        <img src=${anime.data[c].images.jpg.image_url} alt="move aover" class="">
                    </div>
                    <div class="cardbody text-center">
                    <h2> Aired On ${anime.data[c].aired.string}</h2>
                    
                    </div>

                    
                </div>
            </div>`;
            let output = document.getElementById("output");
       // output.innerHTML = eachcountry;
        
        document.getElementById('output').insertAdjacentHTML('beforeend',eachcountry);
        
    })

}
getdata(0)
getdata(1)
getdata(3)

