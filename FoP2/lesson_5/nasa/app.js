document.querySelector("button").addEventListener("click", getPhoto)

async function getPhoto() {
  const url =
    "https://api.nasa.gov/planetary/apod?api_key=h20hfqbdwPTCShY9PDWHyHQ9pg6llFgf380a6UAW"

  let data = await fetch(url)
  let nasaInfo = await data.json()
  document.querySelector("img").src = nasaInfo.hdurl
  console.log(nasaInfo)
}
