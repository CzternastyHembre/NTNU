// Part 1
// I Usually put it at the bottom of the body because html reads from top to bottom and then the
// site will be loaded as fast ass possible, and if you arent doing things that should load
// before (i.e. database and something else) its smart the show the site fast
/* Part 2 */
console.log('PART 2')

for (let i = 1; i < 21; i++) {
  console.log(i);
}

/* Part 3 */
console.log('PART 3')

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for (var numb of numbers) {
  if (numb % (3*5) == 0) {
    console.log('eplekake');
  }else if (numb % 3 == 0) {
    console.log('eple');
  }else if (numb % 5 == 0) {
    console.log('kake');
  }
  else {
    console.log(numb);
  }
}

/* Part 4 */
const header = document.querySelector('#title')
title.innerText = 'Hello, JavaScript'

/* Part 5 */

const box = document.querySelector('#magic')
const div_btn = document.querySelector('.buttons')
const btns = div_btn.querySelectorAll('button')

btns[0].addEventListener('click',changeDisplay)
btns[1].addEventListener('click',changeVisibility)
btns[2].addEventListener('click',reset)

function changeDisplay () {
  box.style.display = 'None'
}

function changeVisibility () {
  box.style.visibility = 'Hidden'
}

function reset () {
  box.style.display = 'Block'
  box.style.visibility = 'Visible'
}

/* Part 6 */
const technologies = [
    'HTML5',
    'CSS3',
    'JavaScript',
    'Python',
    'Java',
    'AJAX',
    'JSON',
    'React',
    'Angular',
    'Bootstrap',
    'Node.js'
];

const ul = document.querySelector('#tech')

for (var techs of technologies) {
  let liste = document.createElement('Li')
  liste.innerText = techs
  ul.appendChild(liste)
}
