#!/usr/bin/env node

function Person(first, last) {
  this.first = first;
  this.last = last;
}
var you = new Person('you', 44)
console.log(you)
console.log(you.first)

let x = parseInt("999")
console.log(x)
console.log(Number.isNan(NaN))
