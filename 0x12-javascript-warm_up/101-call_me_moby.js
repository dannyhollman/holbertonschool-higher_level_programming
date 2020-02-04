#!/usr/bin/node

function callMeMoby (number, func) {
  for (let i = 0; i < number; i++) {
    func();
  }
}

exports.callMeMoby = callMeMoby;
