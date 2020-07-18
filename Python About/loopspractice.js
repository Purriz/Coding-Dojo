// prints odd numbers in console
// for(var i=1; i<=20; i++){
//     if((i % 2) !== 0){
//     console.log(i);
//     }
// }



var sum = 0;

//everything in curly braces is looped
// ++ is add 1. Current = current +1
for(var current=1; current<=5; current++){
    // sum = sum + current
    sum += current
    console.log("Num:", current, "Sum:", sum);
}