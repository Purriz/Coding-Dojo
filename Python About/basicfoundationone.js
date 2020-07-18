// write a function
// create an empty array
// forloop from 1 to 255
// push every value into empty array
// return array


// function banana(){
//     var myArray = []
//     for (var i = 1; i<255; i++){
//         myArray.push (i)
//     }
//     return myArray
// }
// console.log (banana())

// My failed attempt lol
// var sum = 0;

// for(var current=1; current<=1000; current++){
//     // sum = sum + current
//     sum += current
//     console.log("Num:", current, "Sum:", sum);
// }

// function getSum(){
//     var sum = 0;
//     for (var i = 1; i <= 1000; i++){
//         if (i % 2 == 0){
//             sum = sum + i;
//         } 
//     }
//     return sum;
// }
// console.log(getSum());

// function getSumOdd(){
//     var sum = 0;
//     for (var i = 1; i <= 5000; i+=2){
//         if (i % 2 == 1){
//             sum = sum + i;
//             console.log(i);
//         }
//     }
//     return sum;
// }
// console.log(getSumOdd());

// function iterate(numArr){
//     var sum = 0;
//     for (var i = 0; i < numArr.length; i++){
//         sum = sum + numArr[i];
//     }
//     return sum;
// }
// console.log(iterate([1,2,4]));


// function findMax(numArr){
//     var max = numArr[0]; // sets the maximum to the first value in the array
//     for (var i = 0; i < numArr.length; i++){ // for loop to examine each value in the array
//         // see if the next value is bigger than the maximum
//         if (numArr[i] > max){
//             // if it is, make it the new max
//             max = numArr[i];
//         }
//     }
//     return max;
// }
// console.log(findMax([-3,-5,-6,-2]));

// function findAvg(numArr){
//     var sum = 0;
//     var avg = 0;
//     for (var i = 0; i < numArr.length; i++){
//         sum = sum + numArr[i];
//     }
//     avg = sum / numArr.length;
//     return avg;
// }
// console.log(findAvg([1,3,5,7,20]));

// I'm having a really hard time with these