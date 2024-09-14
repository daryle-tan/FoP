document.querySelector("#check").addEventListener("click", checkDay)

let daysOfWeek = [
  "Sunday",
  "Saturday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
]

function checkDay() {
  const day = document.querySelector("#day").value
  for (let i = 0; i < daysOfWeek.length; i++) {
    if (
      day.toLowerCase() === daysOfWeek[0].toLowerCase() ||
      day === daysOfWeek[1].toLowerCase()
    ) {
      document.querySelector("#placeToSee").innerText = "This is a weekend :)"
      console.log(day)
    } else if (day.toLowerCase() === daysOfWeek[2].toLowerCase()) {
      document.querySelector("#placeToSee").innerText = "This is a week day."
    } else if (day.toLowerCase() == daysOfWeek[3].toLowerCase()) {
      document.querySelector("#placeToSee").innerText = "This is a week day."
    } else if (day.toLowerCase() == daysOfWeek[4].toLowerCase()) {
      document.querySelector("#placeToSee").innerText = "This is a week day."
    } else if (day.toLowerCase() == daysOfWeek[5].toLowerCase()) {
      document.querySelector("#placeToSee").innerText = "This is a week day."
    } else if (day.toLowerCase() == daysOfWeek[6].toLowerCase()) {
      document.querySelector("#placeToSee").innerText = "This is a week day."
    } else {
      document.querySelector("#placeToSee").innerText =
        "This is not a day of the week!"
    }
  }
}
