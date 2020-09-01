// Given an array of integers, find the one that appears an odd number
// of times.
// There will always be only one integer that appears an odd number of
// times.

function findOdd(array) {
  let count = 0;
  // Iterate through each array index
  for(let i = 0; i<array.length; i++){
    // For each array index value, compare to every other array index value.
    for(let j = 0; j<array.length; j++){
      // If a match is found, count increments.
      if(array[i] == array[j]){
        count++;
      }
    }
    // After each array index is compared, count will remain even unless the
    // odd value is found.
    if(count % 2 != 0 ){
      // The value of that current array index is returned.
      return array[i];
    }
  }
}

function doTest(a, n) {
  console.log("A = ", a);
  console.log("n = ", n);
  console.log(findOdd(a), n);
}

doTest([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5], 5);
doTest([1,1,2,-2,5,2,4,4,-1,-2,5], -1);
doTest([20,1,1,2,2,3,3,5,5,4,20,4,5], 5);
doTest([10], 10);
doTest([1,1,1,1,1,1,10,1,1,1,1], 10);
doTest([5,4,3,2,1,5,4,3,2,10,10], 1);