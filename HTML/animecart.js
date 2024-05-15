let likes = document.getElementById('likes');
let dislikes = document.querySelector('#dislikes')
let total_likes = document.querySelector('#total')
let likesbtn = document.getElementById('likes-btn');
let dislikesbtn = document.querySelector('#dislikes-btn')

let like = 0
let dislike = 0
let total = 0
likes.textContent = like;
dislikes.textContent = dislike;
total_likes.textContent = total;

likesbtn.addEventListener("click", function () {
    console.log(likes.textContent)
    like++;
    console.log("clicked", like)
    likes.textContent = like;
    ++total
    total_likes.textContent = total;

})
dislikesbtn.addEventListener("click", function () {
    console.log(dislikes.textContent)
    dislike++;
    console.log("clicked", dislike)
    dislikes.textContent = dislike;
    ++total
    total_likes.textContent = total;

})
