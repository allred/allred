#!/usr/bin/env node
var stdin = require('mock-stdin').stdin()
text = "abba"

// start hr
// heap's permutation
function processData(input) {
  var chars = input.split('')
  var words = {}
  chars.forEach(function(char, index) {
    chars.forEach(function(c2, index) {
      words[char + c2] = 1
    })
  })
  console.log(Object.keys(words).length)
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = ""
process.stdin.on("data", function (input) {
  _input += input
});

process.stdin.on("end", function() {
  processData(_input)
})
// end hr

stdin.send(text)
stdin.send(null)
