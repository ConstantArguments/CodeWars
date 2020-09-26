// The new "Avengers" movie has just been released! There are a lot of
// people at the cinema box office standing in a huge line. Each of them
// has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25
// dollars.

// Vasya is currently working as a clerk. He wants to sell a ticket to
// every single person in this line.

// Can Vasya sell a ticket to every person and give change if he initially
// has no money and sells the tickets strictly in the order people queue?

// Return YES, if Vasya can sell a ticket to every person and give change
// with the bills he has at hand at that moment. Otherwise return NO.

// Examples:
//  tickets([25, 25, 50])
//      => YES
//  tickets([25, 100])
//      => NO. Vasya will not have enough money to give change to 100
//          dollars
//  tickets([25, 25, 50, 50, 100])
//      => NO. Vasya will not have the right bills to give 75 dollars of
//          change (you can't make two bills of 25 from one of 50)

// Global variables
var register = [];
var result = false;

// Takes money form person, calculates change needed, sends to makeChange()
// Returns "YES" or "NO" if change can be given.
function tickets(peopleInLine) {
  for (let i = 0; i < peopleInLine.length; i++) {
    // console.log("Person " + i);
    register.push(peopleInLine[i]);
    // console.log("register received " + peopleInLine[i]);
    // console.log("register now contains " + register);
    let change = peopleInLine[i] - 25;
    makeChange(change);
    // console.log("result is " + result);
    if (result == true) {
      // console.log("Correct Change Given");
      // console.log("Next Person");
      continue;
    } else {
      register = [];
      result = false;
      // console.log("Cannot Give Change !!!!!");
      return "NO";
    }
  }
  register = [];
  result = false;
  // console.log("All change given to all in line");
  return "YES";
}

// Recursive
// Makes change from register drawer. Uses big $50s first.
function makeChange(change) {
  //console.log("Change owed is " + change);
  if (change == 0) {
    // console.log("0 change given");
    // console.log("register now contains " + register);
    result = true;
    return;
  }
  if (change >= 50) {
    let index = register.indexOf(50);
    if (index != -1) {
      // console.log("50 found in register");
      change = change - 50;
      // console.log(index50);
      register.splice(index, 1);
      // console.log("50 change given");
      // console.log("register now contains " + register);
    } else {
      // console.log("No 50 found in register");
    }
  }
  if (change >= 25) {
    let index = register.indexOf(25);
    if (index != -1) {
      // console.log("25 found in register");
      change = change - 25;
      // console.log(index);
      register.splice(index, 1);
      // console.log("25 change given");
      // console.log("register now contains " + register);
    } else {
      // console.log("No 25 found in register");
      // console.log("Change not found");
      result = false;
      return;
    }
  }
  makeChange(change);
}

console.log(tickets([25, 25, 50, 50]), "YES");
console.log(tickets([25, 100]), "NO");
console.log(
  tickets([25, 50, 25, 100, 25, 50, 25, 100, 25, 25, 25, 100]),
  "YES"
);
