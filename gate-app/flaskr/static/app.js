
v = document.querySelector("#vehicle")
p = document.querySelector("#pedestrian")

v.addEventListener('click', () => {
   fetch('/open_gate')
	.then(response => response.json())
	.then(data => console.log(data))
	.catch((error) => console.error('Error:', error))
});

p.addEventListener('click', () => {
   fetch('/open_pedestrian_gate')
	.then(response => response.json())
	.then(data => console.log(data))
	.catch((error) => console.error('Error:', error))
});

    
// p.addEventListener('click', () => console.log("pedestrian clicked") )

// add function call to activate gate
