#!/usr/bin/env node

text = "something"

// start stdin block
var stdin = require('mock-stdin').stdin()
process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = ""
process.stdin.on("data", function (input) {
  _input += input
});
process.stdin.on("end", function() {
  main(_input)
})

function readLine() {
}
// end stdin block

function main(i) {
  console.log(i)
  //console.trace('tracing')
}

stdin.send(text)
stdin.send(null)
