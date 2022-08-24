var p = document.getElementById("favorites");
p.onclick = function(event) {
	let body = document.body;
	if (body.style['background'] != 'red') {
        body.style['background'] = 'red';
	}
	else {
	    body.style['background'] = 'green';
	}

}
console.log('dsdsd')