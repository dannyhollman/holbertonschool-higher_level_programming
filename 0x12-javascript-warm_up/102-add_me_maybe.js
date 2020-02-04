#!/usr/bin/node

function addMeMaybe (number, func) {
  number += 1;
  func(number);
}

exports.addMeMaybe = addMeMaybe;
