let total = 0
let numHolder = []
let numStrHolder = []
let numStr
let numToAdd
let isAdding = false
let isSubtracting = false
let isMultiplying = false
let isDividing = false
// let numOne = document.querySelector(".one").innerText

document.querySelector(".one").addEventListener("click", displayValue)
document.querySelector(".two").addEventListener("click", displayValue)
document.querySelector(".three").addEventListener("click", displayValue)
document.querySelector(".four").addEventListener("click", displayValue)
document.querySelector(".five").addEventListener("click", displayValue)
document.querySelector(".six").addEventListener("click", displayValue)
document.querySelector(".seven").addEventListener("click", displayValue)
document.querySelector(".eight").addEventListener("click", displayValue)
document.querySelector(".nine").addEventListener("click", displayValue)
document.querySelector(".zero").addEventListener("click", displayValue)

document.querySelector(".clear").addEventListener("click", makeZero)
document.querySelector(".add").addEventListener("click", add)

function add() {
  //   document.querySelector("#placeToPutResult").innerText = 0
  isAdding = true
  numStrHolder.push(numStr)
  console.log(numStrHolder, "numStrHolder")
}

function displayValue() {
  let value = this.innerText
  if (!isAdding) {
    numHolder.push(value)
    numStr = parseInt(numHolder.join(""))
    document.querySelector("#placeToPutResult").innerText = numStr
    console.log(typeof numStr, numStr)
  } else {
    numHolder.push(value)
    console.log(numHolder, "numHolder")
    numStr = parseInt(numHolder.join(""))
    document.querySelector("#placeToPutResult").innerText = numStr
    console.log(typeof numStr, numStr)
  }
}
// clears out the results and sets to 0
function makeZero() {
  numHolder = []
  document.querySelector("#placeToPutResult").innerText = numHolder.length
  console.log("makezero")
}

function subtract() {
  total = total + 9
  document.querySelector("#placeToPutResult").innerHTML = total
}
