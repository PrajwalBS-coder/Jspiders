let users = [
    { name: 'John', age: 25, occupation: 'gardener' },
    { name: 'Lenny', age: 51, occupation: 'programmer' },
    { name: 'Andrew', age: 43, occupation: 'teacher' },
    { name: 'Peter', age: 81, occupation: 'teacher' },
    { name: 'Anna', age: 47, occupation: 'programmer' },
    { name: 'Albert', age: 76, occupation: 'programmer' },
];
var a=[];
for (var i = 0; i < users.length; i++) {
    if (users[i].age > 50 && users[i].occupation==='programmer')
        {
            a.push(users[i]);
        }
}
console.log(a)


let filteredUsers = users.filter((users) => {
    return users.age > 50 && users.occupation === 'programmer';
});

console.log(filteredUsers);

let filteredUserNames = users.filter(user => user.age > 40 && user.occupation === 'programmer')
    .sort((a, b) => a.age - b.age)
    .map(user => user.name);

console.log(filteredUserNames);