/* Team cool-crabs Ryan Ma Carlos Hernandez
   SoftDev
   K21 -- Get Scripty - learned how to redo fib + fact
   2021-04-13
*/
let factI = (n) => {
  let prod = 1;
  // for loops like c
  for (let i = 1; i <= n; i++) {
    prod *= i;
  }
  // while (n > 0) {
  //   prod *= n
  //  n--;
  // }
  return prod;
};

console.log(factI(6));

let factR = (n) => {
  // three equals means check type and value
  if (n === 1 || n == 0) {
    return 1;
  } else {
    return factR(n - 1) * n;
  }
};

console.log(factR(6));

let fibI = (n) => {
  if (n < 2) {
    return 0;
  }
  let previous = 0;
  let current = 1;
  let sum = 0;
  for (let i = 2; i < n; i++) {
    sum = previous + current;
    previous = current;
    current = sum;

  }
  return sum;
};

console.log(fibI(5));

let fibR = (n) => {
  if (n === 1) {
    return 0;
  }
  if (n === 2) {
    return 1;
  } else {
    return fibR(n - 1) + fibR(n - 2);
  }
};

console.log(fibR(4));
