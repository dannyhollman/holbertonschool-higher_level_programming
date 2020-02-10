#!/usr/bin/node

exports.esrever = function (list) {
  let right = list.length - 1;
  for (let left = 0; left < list.length / 2; left++, right--) {
    const temp = list[left];
    list[left] = list[right];
    list[right] = temp;
  }
  return list;
};
