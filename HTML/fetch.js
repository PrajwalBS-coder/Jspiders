getbutton = document.getElementById("data")
//console.log(getbutton.innerText)
display = document.getElementById("display")
display.addEventListener("click", getdata);

function getdata() {
    let xhr = new XMLHttpRequest()

    xhr.open('GET', 'product.json', true)
    xhr.send()

    xhr.onprogress = setTimeout(function () {
        let load = document.getElementById("load");
        load.innerText = "DATA loading"
    });


    xhr.onload =setTimeout( function () {

        let load = document.getElementById("load");
        load.innerText = ""
        let produc = JSON.parse(xhr.responseText);
        let { products } = produc
        //console.log(produc)

        let product = ``;
        for (let item of products) {
            product += ` <div class="col-md-3">
                <div class="card" >
                    <div class="cardheader">
                        <img src=${item.img} alt="not found" class="">
                    </div>
                    <div class="cardbody text-center">
                        <h3>${item.name}</h3>
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum, sit?</p>
                        <h6>${item.cost}</h6>
                        <i class="fa fa-minus-circle" onclick="dec(${item.id},${item.quantity})"></i>
                        
                        <span id="qty">${item.quantity}</span>
                
                        <i  class="fa fa-plus-circle btn-dark" onclick="inc(${item.id})"></i><br>
                        <small style="color: limegreen;">Availabel</small>
                    </div>
                </div>
            </div>`;
        }
        let output = document.getElementById("output");
        output.innerHTML = product;
    },2000)

}


