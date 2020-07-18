// console.log("test");
// document.getElementById('head');.innerHTML

// Data Types

// Numbers

// var num = 10;

// Strings: measurement away from the start

// var str = "anything I want";
// var another_str = "Another string";

// var both_strings = str + ' ' + another_str;

// console.log(both_strings)

// console.log(str, "This is another string")

// console.log(str[9], "This is the 9th index of str");

// Arrays: wrapped in square brackets


// var arr = [2, 3, 4, "hello", "hi", [2, 3]];
// console.log(arr[5] [0], 'I looked into a nested array!')


// Objects: curly brackets

// var obj = {
//     'key': 'value',
//     'another_key': 10
// }

// console.log(obj['another_key'])

// Operators

// console.log(num + 100);

// == is, used for comparison
// === used for comparison, takes type into account
// !== BANG operator, not
// % returns remainder from division

// if 1 % 1 == 0 

// num = 20

// if (num != 10){
//     console.log("num isn't ten")
// }

// if(10 == '10'){
//     console.log("They're the same")
// }
// if(10 === '10'){
//     console.log("They're the same. with triple equals!")
// }



// if (email !== email){
//     don't log them in
// }
// else {
//     log them in
// }

var score = 50;

if(score < 50){
    console.log("You can do better than that");
}
else if(score < 400){
    console.log("Really...that's all you got?")
}
else if(score < 500){
    console.log("Wow.. don't play anymore")
} else if(score > 1000){
    console.log("Great work.")
}

// Loops

// for, while

// for(Start, end, itterating)

// print all numbers from 0 to 100

for(var i=0; i<=100; i++){
    if(i % 2 == 0){
        console.log(i);
    }
}

var arr = [2, 3, 4, "hello", "hi", [2, 3]];

for(var i=0; i<arr.length; i++){
    console.log(arr[i]);
}

str = "H";

while(str.length < 20){
    str += "i"
}

console.log(str);