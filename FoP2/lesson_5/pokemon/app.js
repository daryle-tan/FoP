document.querySelector("button").addEventListener("click", getFetch)

async function getFetch() {
  let choice = document.querySelector("input").value
  const shinyCheckBox = document.getElementById("myCheckbox")
  const url = "https://pokeapi.co/api/v2/pokemon/" + choice

  let data = await fetch(url)
  let pokemonInfo = await data.json()

  document.querySelector(
    "h2",
  ).innerText = `Name: ${pokemonInfo.name.toUpperCase()}`
  if (shinyCheckBox.checked) {
    document.querySelector("img").src = pokemonInfo.sprites.back_shiny
  } else {
    document.querySelector("img").src = pokemonInfo.sprites.front_default
  }
  document.querySelector("h3").innerText = `Type: 
    ${pokemonInfo.types[0].type.name.toUpperCase()}`
  console.log(pokemonInfo)
}
