let total = 0
let subtotal = 0
let numStrHolder = []
let currentDisplay = ""
let isAdding = false
let isSubtracting = false
let isMultiplying = false
let isDividing = false

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
document.querySelector(".subtract").addEventListener("click", subtract)
document.querySelector(".multiply").addEventListener("click", multiply)
document.querySelector(".divide").addEventListener("click", divide)
document.querySelector(".equal").addEventListener("click", equalNum)

function equalNum() {
  numStrHolder.push(parseInt(currentDisplay))

  for (let i = 0; i < numStrHolder.length; i++) {
    if (isAdding) {
      total += numStrHolder[i]
      console.log(total, "total")
    } else if (isSubtracting) {
      if (i === 0) {
        total += numStrHolder[0]
      } else {
        total -= numStrHolder[i]
      }
    } else if (isMultiplying) {
      if (total === 0) {
        total = 1
      }
      total *= numStrHolder[i]
      console.log(total, "total")
    } else if (isDividing) {
      if (total === 0 && i == 0) {
        total = numStrHolder[0]
      } else {
        total /= numStrHolder[i]
      }
    }
  }
  document.querySelector("#placeToPutResult").innerText = total

  isAdding = false
  isSubtracting = false
  isMultiplying = false
  isDividing = false
  currentDisplay = ""
  numStrHolder = []
}

function add() {
  numStrHolder.push(parseInt(currentDisplay))
  isAdding = true
  isSubtracting = false
  currentDisplay = ""
  document.querySelector("#placeToPutResult").innerText = 0
  console.log(numStrHolder, "numStrHolder", isAdding, typeof numStrHolder[0])
}

function subtract() {
  numStrHolder.push(parseInt(currentDisplay))
  isSubtracting = true
  isAdding = false
  currentDisplay = ""
  document.querySelector("#placeToPutResult").innerText = 0
  console.log(
    numStrHolder,
    "numStrHolder",
    isSubtracting,
    typeof numStrHolder[0],
  )
}

function multiply() {
  numStrHolder.push(parseInt(currentDisplay))
  isMultiplying = true
  isDividing = false
  currentDisplay = ""
  document.querySelector("#placeToPutResult").innerText = 0
  console.log(numStrHolder, "multiply")
}

function divide() {
  numStrHolder.push(parseInt(currentDisplay))
  isMultiplying = false
  isDividing = true
  currentDisplay = ""
  document.querySelector("#placeToPutResult").innerText = 0
  console.log(numStrHolder, "divide")
}

function makeZero() {
  numStrHolder.length = 0
  currentDisplay = ""
  total = 0
  isAdding = false
  isSubtracting = false
  document.querySelector("#placeToPutResult").innerText = 0
}

function displayValue() {
  currentDisplay += this.innerText
  document.querySelector("#placeToPutResult").innerText = currentDisplay
  console.log(currentDisplay)
}
