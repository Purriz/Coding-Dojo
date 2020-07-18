var testArr = [6,3,5,1,2,4];

// I copied this from the solution because I was very lost. I got help with understanding though
var sum=0;
for(let i=0; i<testArr.length; i++){
    sum+=testArr[i];
    console.log('val:', testArr[i], 'sum:', sum);
}

for(let i=0; i<testArr.length; i++){
    testArr[i] = testArr[i] * i;
}
console.log(testArr);