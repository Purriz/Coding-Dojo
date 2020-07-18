for(var j = 1; j <= 15; j++){
    console.log (j, "j at the beginning of loop")
        if (j % 2 == 0){
            j += 2;
            console.log (j, "I just added two because j was an even number");
        }
        else if (j % 3 == 0){
            j++;
            console.log(j, "Just added 1 to j, it was a divisible by 3");
        }
        console.log (j, "J at the end of the loop");
        console.log ("J++")
}
console.log("loop ended")