let likes = document.getElementById('likes');
let dislikes = document.querySelector('#dislikes')
let total_likes = document.querySelector('#total')
let likesbtn = document.getElementById('likes-btn');
let dislikesbtn = document.querySelector('#dislikes-btn')

let like = localStorage.getItem("likes")?localStorage.getItem("likes"):0;
let dislike = localStorage.getItem("dislikes");
let total = localStorage.getItem("total");
likes.textContent = localStorage.getItem("likes");
dislikes.textContent = localStorage.getItem("dislikes");
total_likes.textContent = localStorage.getItem("total");


likesbtn.addEventListener("click", function () {
   
    like++;
    console.log("clicked", like)
    localStorage.setItem("likes",like)
    likes.textContent = like;
    ++total
    localStorage.setItem("total",like)
    total_likes.textContent = total;

})
dislikesbtn.addEventListener("click", function () {
    //console.log(dislikes.textContent)
    dislike++;
    console.log("clicked", dislike)
    localStorage.setItem("dislikes",dislike)
    dislikes.textContent = dislike;
    ++total
    localStorage.setItem("total",total)
    total_likes.textContent = total;

})
