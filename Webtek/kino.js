/* Lukker dropdown menyen dersom brukeren klikker tenfor den
window.onclick = function(event) {
    if (!event.target.matches('.dropbutton')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
}
*/


const divNav = document.createElement('div')
divNav.className = 'navbar'
divNav.innerHTML = 
    `
    <link rel="stylesheet" href="style/navBar_style.css">


    <div class="navbar">

        <div class="navBarDiv" id="siste">
            <a href="kontakt_oss.html">Kontakt oss</a>
        </div>


        <div class="navBarDiv" id="navBarSkille">
            <b id="nadahover">∣</b>
        </div>


        <div class="navBarDiv">
            <a href="omoss.html">Om oss</a>
        </div>

        <div class="navBarDiv">
            <a href="anbefalinger.html">Anbefalinger</a>
        </div>
        <div class="navBarDiv">
            <a href="billetter.html">Bestilling</a>
        </div>

        <div class="navBarDiv" id ="dropdown">
            <button class="dropbutton"><a href="kinoprogram.html" class="dropbutton">Kinoprogram</a></button>
            <div id="sjangere" class="dropdown-content">
                <a href="kinoprogram.html">Drama</a>
                <a href="kinoprogram.html#superhelterDiv">Superhelter</a>
                <a href="kinoprogram.html#barnefilmerDiv">Barnefilmer</a>
                <a href="kinoprogram.html#scaryDiv">Grøsser</a>
                <a href="kinoprogram.html#romantikkDiv">Romantikk</a>
                <a href="kinoprogram.html#actionDiv">Action</a>
                <a href="kinoprogram.html#sciFiDiv">Sci-fi</a>
                <a href="kinoprogram.html" id="kinoprgrm">Alle filmer</a>
            </div>
        </div>

        <div class="navBarDiv">
            <a href="hovedside.html">Hjem</a>
        </div>
            
        

        <div class="navBarDiv0" id="logoen">

            <a href="hovedside.html">
            <img id="logo" src="img/Filmstrip.png" alt="Logo" title ="Klikk for å komme til hovedsiden" href="#hovedsiden"></a>
            <div class="logoTxt" id="logoTxt1" href="#hovedsiden">GAMLE</div>
            <div class="logoTxt" id="logoTxt2" href="#hovedsiden"> Trondheim kino</div>

            <div class="logoTxt" id="logoTxt3" href="#hovedsiden">G</div>
            <div class="logoTxt" id="logoTxt4" href="#hovedsiden">T</div>
            <div class="logoTxt" id="logoTxt5" href="#hovedsiden">K</div>
        </div>

        <button class="hamButton" onclick="open()"><img src="img/hamburger-icon-white2.png" alt="hamburgermeny" class="hamButton"></button>
        <button id="closeButton" onclick="close()">✕</button>
        <div class="hamburgerDiv">
            <li><button class="dropbutton" class="hamLinks"><a href="kinoprogram.html" class="dropbutton">Kinoprogram</a></button></li>
                <ul id="genres" class="dropdown-content">
                    <li><a href="kinoprogram.html">Drama</a></li>
                    <li><a href="kinoprogram.html#superhelterDiv">Superhelter</a></li>
                    <li><a href="kinoprogram.html#barnefilmerDiv">Barnefilmer</a></li>
                    <li><a href="kinoprogram.html#scaryDiv">Grøsser</a></li>
                    <li><a href="kinoprogram.html#romantikkDiv">Romantikk</a></li>
                    <li><a href="kinoprogram.html#actionDiv">Action</a></li>
                    <li><a href="kinoprogram.html#sciFiDiv">Sci-fi</a></li>
                    <li><a href="kinoprogram.html" id="kinoprgrm">Alle filmer</a></li>
                </ul>
            <li><a href="anbefalinger.html" class="hamLinks">Anbefalinger</a></li>
            <li><a href="bestilling.html" class="hamLinks">Bestilling</a></li>
            <li><a href="omoss.html" class="hamLinks">Om oss</a></li>
            <li><a href="kontaktoss.html" class="hamLinks">Kontakt oss</a></li>
        <div>


    </div>

    `
console.log(divNav);
const body = document.querySelector('body')
body.appendChild(divNav)

let hamB = document.getElementById("hamButton");
let closeB = document.getElementById("closeButton");
let hamD = document.getElementsByClassName("hamburgerDiv")[0];

console.log(hamD);


function open(){
    hamB.style.display = "none";
    closeB.style.display = "block";
    hamD.style.display = "block";
}

function close(){
    closeB.style.display = "none";
    hamB.style.display = "block";
    hamD.style.display = "none";
}