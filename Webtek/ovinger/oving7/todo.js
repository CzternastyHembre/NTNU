//constants
const inp = document.querySelector("#inp")
const btnAdd = document.querySelector("#btnAdd")
const btnRemoveAll = document.querySelector("#btnRemoveAll")
const btnRemoveLast = document.querySelector("#btnRemoveLast")
const ul = document.querySelector("#ul")
const boxStatus = document.querySelector("#boxStatus")

//Empty globaal arrays
let checkboxes = []
let listeElementer = []

//Eventlisteners
btnAdd.onclick = btnRemoveLast.onclick = btnRemoveAll.onclick = write //kaller funksjonen når den klikkes

//Funksjoner
function write(event) {

    if (event.target == btnRemoveAll) { //Hvis det er sletteknappen sletter jeg alt i arrayene og sletter det inni ul
        checkboxes = []
        listeElementer = []
    } else if (event.target == btnRemoveLast) { //Hvis det er sletteknappen sletter jeg alt i arrayene og sletter det inni ul
        checkboxes.pop()
        listeElementer.pop()
    } else if (inp.value == "") { //Sjekker om det faktsik er noe i feltet, hvis ikke returner funksjonen
        return
    } else {
        addTask() //Kjører addtask
    }

    changeStatus()

    ul.innerHTML = ""
    for (let i = listeElementer.length - 1; i >= 0; i--) { //appender listene i arrayet men starter på slutten og ender på starten for å skrive ut i riktig rekkefølge
        ul.appendChild(listeElementer[i])
    }
}

function addTask() {
    //Lager forskjellige elementer som tilslutt legges i ul
    let liste = document.createElement("li")
    let h2 = document.createElement("h2")
    let i = document.createElement("i")
    let chk = document.createElement("input")
    let totalTime = fetchTime() //Henter tiden til når den lages

    //Legger til egenskaper på elementene
    chk.type = "checkbox"
    chk.className = "chk"
    chk.checked = false
    checkboxes.push(chk)
    chk.onclick = changeStatus

    h2.innerHTML = inp.value

    i.innerHTML = 'Dato: ' + totalTime

    //legger elementene i det nye liste-elementet
    liste.appendChild(chk)
    liste.appendChild(h2)
    liste.appendChild(i)

    //Legger listen inn i listeelementer-arrayet
    listeElementer.push(liste)
}

function changeStatus() { //funksjon som endrer statusen og hvor mange bokser som er sjekket
    let boxesChecked = 0

    for (let i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            boxesChecked++
            listeElementer[i].className = 'done' //klassen "done" gir stilen; text-decoration: line-through;
        } else {
            listeElementer[i].className = ''
        }
    }
    boxStatus.innerHTML = 'Finnised:' + boxesChecked + '/' + checkboxes.length
}

function fetchTime() { //funksjon som henter tiden
    let d = new Date()

    let seconds = String(d.getSeconds()) //Kanskje unødviendig å ha så nøyaktig, menmen
    let minutes = String(d.getMinutes())
    let hours = String(d.getHours())
    let day = String(d.getDate())
    let month = String(d.getMonth() + 1) //merk at Jan=0, Dec=11 (idk hvorfor)
    let year = String(d.getFullYear())

    let timeArray = [seconds, minutes, hours, day, month, year]
    for (let i = 0; i < timeArray.length; i++) { //Sjekker om lengden strengene på tidene ikke er 1 for å gjøre om feks: 9:5:2 => (09:05:02)
        if (timeArray[i].length <= 1) {
            timeArray[i] = '0' + timeArray[i]
        }
    }
    let clock = timeArray[2] + ':' + timeArray[1] + ':' + timeArray[0]
    let dato = timeArray[3] + '/' + timeArray[4] + '/' + timeArray[5]

    return [clock, dato] //Returnerer klokken og datoen i ett array
}