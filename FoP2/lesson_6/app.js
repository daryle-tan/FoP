document.querySelector(".add").addEventListener("click", addTask)
// document.querySelector(".delete").addEventListener("click", deleteTask)

const newSpan = document.createElement("span")
newSpan.innerText = value
newSpan.setAttribute("class", "task")

const newDeleteBtn = document.createElement("button")
newDeleteBtn.innerText = "DEL"
newDeleteBtn.setAttribute("class", "button delete")

function addTask() {
  const value = document.querySelector(".inputTask").value

  const newSpan = document.createElement("span")
  newSpan.innerText = value
  newSpan.setAttribute("class", "task")
  newSpan.addEventListener("click", updateTask)
  //   newSpan.addEventListener("click", deleteTask)

  const newDeleteBtn = document.createElement("button")
  newDeleteBtn.innerText = "DEL"
  newDeleteBtn.setAttribute("class", "button delete")
  //   newDeleteBtn.addEventListener("click", deleteTask)

  const divTask = document.querySelector(".taskContainer")

  divTask.appendChild(newSpan)
  divTask.appendChild(newDeleteBtn)

  document.querySelector(".inputTask").value = ""
  console.log(value)
}

function deleteTask() {
  const delTask = document.querySelector(".task")
  const delBtn = document.querySelector(".delete")

  const divTask = document.querySelector(".taskContainer")

  if (divTask.hasChildNodes()) {
    divTask.removeChild(delTask)
    divTask.removeChild(delBtn)
  }

  console.log("trying to delete", current)
}

function updateTask() {
  if (this.style.textDecoration !== "line-through") {
    this.style.textDecoration = "line-through"
  } else {
    this.style.textDecoration = "none"
  }
}
