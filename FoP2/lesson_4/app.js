let total = 0
let numHolder = []
let numHolderTwo = []
let numOne = document.querySelector("#one").innerText

document.querySelector("#one").addEventListener("click", addToNumHolder)
// document.querySelector("#one").addEventListener("click", add3)
document.querySelector("#zebra").addEventListener("click", add9)
document.querySelector("#cantThinkOfAnything").addEventListener("click", sub2)

function addToNumHolder() {
  // let value = this.innerText
  document.querySelector("#placeToPutResult").innerText = numOne
  console.log("hiß")
  // return total
}

function makeZero() {
  total = 0
  document.querySelector("#display").innerText = total
}

function add() {
  total = total + 3
  document.querySelector("#placeToPutResult").innerText = total
}

function subtract() {
  total = total + 9
  document.querySelector("#placeToPutResult").innerHTML = total
}
