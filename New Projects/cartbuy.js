let products=[
    {
        id:1,
        img:"images/luffy1.webp",
        name:"Shirt",
        cost:1999,
        quantity:0
    },
    {
        id:2,
        img:"images/solo.webp",
        name:"Shirt",
        cost:1999,
        quantity:0
    },
    {
        id:3,
        img:"https://imgs.search.brave.com/BRVI8Xzn4eK58_JWCfCTitX8vKVK14x29B1uIawOdmo/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMudW5zcGxhc2gu/Y29tL3Bob3RvLTE1/MzEyOTc0ODQwMDEt/ODAwMjIxMzFmNWEx/P3E9ODAmdz0xMDAw/JmF1dG89Zm9ybWF0/JmZpdD1jcm9wJml4/bGliPXJiLTQuMC4z/Jml4aWQ9TTN3eE1q/QTNmREI4TUh4elpX/RnlZMmg4TVRWOGZH/eGhjSFJ2Y0h4bGJu/d3dmSHd3Zkh4OE1B/PT0.jpeg",
        name:"Shirt",
        cost:1999,
        quantity:0
    },
    {
        id:4,
        img:"https://imgs.search.brave.com/HL0j5mBIHLgfiQNMHvD15NXo9qHGJ2BUQXzmXkDcY4Y/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMudW5zcGxhc2gu/Y29tL3Bob3RvLTE1/NDIzOTM1NDUtMTBm/NWNkZTJjODEwP3E9/ODAmdz0xMDAwJmF1/dG89Zm9ybWF0JmZp/dD1jcm9wJml4bGli/PXJiLTQuMC4zJml4/aWQ9TTN3eE1qQTNm/REI4TUh4elpXRnlZ/Mmg4TVRCOGZHeGhj/SFJ2Y0NVeU1HTnZi/WEIxZEdWeWZHVnVm/REI4ZkRCOGZId3c.jpeg",
        name:"Shirt",
        cost:1999,
        quantity:0
    },

];

let output=document.getElementById("output");
function display(items){
    if(items.length>=1){
        let product=``;
        for(let item of items){
            product+=` <div class="col-md-3">
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
                    <small style="color: limegreen;">Availabel</small><br>
                    <div id="buttonon">
                    <button class="btn btn-dark" id="on${item.id}" disabled >BUY</button>
                    
                    </div>
                    
                </div>
            </div>
        </div>`;
        }
        output.innerHTML=product;
    }
}
display(products)
//let on=document.getElementById("on");
function inc(id) {
    let items = products.map((item) => {
        if (item.id == id) {
            item.quantity++;
            // Enable the button if quantity is greater than 0
            if (item.quantity > 0) {
                document.getElementById(`on${id}`).disabled = false;
            }
        }
        return item;
    });
    display(items);
}

function dec(id, value) {
    let it = products.map((item) => {
        if (item.id == id) {
            if (value > 0) {
                item.quantity--;
                // Disable the button if quantity becomes 0
                if (item.quantity === 0) {
                    document.getElementById(`on${id}`).disabled = true;
                }
            }
        }
        return item;
    });




    display(it);
}


function updateButtonState(item) {
    let button = document.getElementById(`on${item.id}`);
    if (button) {
        if (item.quantity > 0) {
            button.disabled = false; // Enable button if quantity > 0
        } else {
            button.disabled = true; // Disable button if quantity is 0
        }
    }
}
