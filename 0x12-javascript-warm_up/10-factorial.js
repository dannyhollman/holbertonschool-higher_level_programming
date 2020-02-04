#!/usr/bin/node

function factorial (number) {
  if (number < 0) {
    return (-1);
  } else if (number === 0) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}

if (!process.argv[2]) {
  console.log('1');
} else {
  console.log(factorial(Number(process.argv[2])));
}
