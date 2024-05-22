const userDetails = {
    firstName: "Jane",
    lastName: "Daniels",
    userName: "jane.daniels",
    email: "jane.daniels@example.com",
    comapny: "Example Inc.",
    address: "1234 Example Street",
    age : 25,
    hobby: "Singing"
};

let keysArray = Object.keys(userDetails);

console.log(keysArray);

let newarry=keysArray.filter(key=>key.length==5)
console.log(newarry)
