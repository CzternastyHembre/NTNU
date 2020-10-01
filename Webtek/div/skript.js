const btn = document.querySelector("#btn")
const target = document.querySelector(".target")
const countries = ['Norway','Sweden','Denmark','Spain']
btn.addEventListener('click',doSomething)

let i = 0
function doSomething() {
  const countryCycle = countries.filter(count => countries.indexOf(count)== i%countries.length)
  target.innerHTML = countryCycle
  i++
}
doSomething()



//forløkker

for (country in countries) {
  // console.log(country);
}
for (country of countries) {
  // console.log(country);
}
function countryLog(c) {
  // console.log(c);
}

//map

countries.map(countryLog)

// countries.map((country) => {console.log(country);})
function makeCapitalLetters(country) {
  return country.toUpperCase();
}
const allCapCountries = countries.map(makeCapitalLetters)

const oneLine = countries.map(count => count.toUpperCase())

// console.log(allCapCountries);
// console.log(oneLine);

//filter

const someCountries = countries.filter(count => count.length === 6)
const someCountriesCaps = oneLine.filter(count => count.length === 6)

// console.log(someCountries);
// console.log(someCountriesCaps);
