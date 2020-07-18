// write a function
// create an empty array
// forloop from 1 to 255
// push every value into empty array
// return array


function banana(){
    var myArray = []
    for (var i = 1; i<255; i++){
        myArray.push (i)
    }
    return myArray
}
console.log (banana())