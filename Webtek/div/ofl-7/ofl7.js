const canvas = document.querySelector('#canvas')
const ctx = canvas.getContext('2d')

// ctx.rect(10, 10, 50, 50)
// ctx.stroke()
// ctx.fill()

ctx.lineWidth= 4

// mast
ctx.rect(235,90,15,230)
ctx.fillStyle = "brown"
ctx.fill()
ctx.stroke()


// seil
ctx.beginPath()
ctx.moveTo(250,300)
ctx.lineTo(250,100)
ctx.lineTo(450,200)
ctx.lineTo(250,300)

ctx.fillStyle = 'moccasin'
ctx.fill()

ctx.stroke()


// Hull

ctx.beginPath()
ctx.arc(250,320,175,0,Math.PI)
ctx.lineTo(250+177,320)
ctx.fillStyle = "green"
ctx.fill()
ctx.stroke()