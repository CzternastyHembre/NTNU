const inp = document.querySelector("#inp")
const btn = document.querySelector("#btn")
const ul = document.querySelector("#ul")
const boxStatus = document.querySelector("#boxStatus")

//Empty globaal arrays
let checkboxes = []
let listeElementer = []
let reversListeElementer = []

btn.onclick = write

function sjekk() {
    let boxesChecked = 0
    let total = 0

    for (let i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            boxesChecked++
            listeElementer[i].className = 'active'
        }else{
            listeElementer[i].className = ''
        }

        total++
    }
    boxStatus.innerHTML = 'Finnised:'+boxesChecked+'/'+total
}

function write() {
    if (inp.value == "") {
        return
    }
    addTask()
    console.log(reversListeElementer);
    console.log(listeElementer);
    ul.innerHTML = ""
    for (const list of reversListeElementer) {
        ul.appendChild(list)
    }
    sjekk()
}

function addTask() {
    let liste = document.createElement("li")
    let p = document.createElement("p")
    let i = document.createElement("i")
    let chk = document.createElement("input")
    chk.type = "checkbox"
    chk.className = "chk"
    chk.checked = false
    console.log(chk.value);
    
    let totalTime = fetchTime()[0]+'|'+fetchTime()[1]


    p.innerHTML = inp.value
    i.innerHTML = totalTime
    
    liste.appendChild(p)
    liste.appendChild(i)
    liste.appendChild(chk)
    
    checkboxes.push(chk)
    listeElementer.push(liste)
    reversListeElementer = listeElementer.slice().reverse()

    liste.id = listeElementer.indexOf(liste)

    console.log(liste);
    chk.onclick = sjekk   
}

function fetchTime() {
    let d = new Date()

    let seconds = String(d.getSeconds())
    let minutes = String(d.getMinutes())
    let hours = String(d.getHours())
    let day = String(d.getDate())
    let month = String(d.getMonth()+1) //note that Jan=0, Dec=11 (annoying I know)
    let year = String(d.getFullYear())

    let timeArray = [seconds,minutes,hours,day,month,year]

    for (let i = 0; i < timeArray.length; i++) {
        if (timeArray[i].length <= 1){
            timeArray[i] = '0'+timeArray[i]
        }
    }
    let clock = (timeArray[2]+':'+timeArray[1]+':'+timeArray[0])
    let dato = (timeArray[3]+'/'+timeArray[4]+'/'+timeArray[5]) 

    return [clock,dato]
}