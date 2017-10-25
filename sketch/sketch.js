#!/usr/bin/env node

let list = [8, 3, 11, 9, 6]
let hash = {}
for (let value of list) {
  console.log(value)
}
console.log(hash)
console.log(list[2])
console.log(list.length)

list.forEach(function(currentValue, index, array) {
  console.log({"index": index})
})
