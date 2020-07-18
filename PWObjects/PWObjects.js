// var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];
// for(name in users, age in users)
//     console.log(users + '- ' + age[name]);



// print:
// Michael - 37
// John - 30
// David - 27

var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];

console.log(users[1].age);
console.log(users[0].name);

for (var i = 0; i < users.length; i++){
    console.log(users[i].name, "-", users[i].age);
}