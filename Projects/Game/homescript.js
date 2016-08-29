$(document).ready( function() {
	var canvasWidth = 1600;
	var canvasHeight = 600;
	var FPS = 40;

	$('#gameCanvas').attr('width', canvasWidth);
	$('#gameCanvas').attr('height', canvasHeight);

	var keysDown = {};

	$('body').bind('keydown', function(e) {
		keysDown[e.keyCode] = true;
	})

	$('body').bind('keyup', function(e) {
		keysDown[e.keyCode] = false;
	})
	// document.body.addEventListener("keydown", function (e) {
    //    	keysDown[e.keyCode] = true;
	// });
	// document.body.addEventListener("keyup", function (e) {
    //    	keysDown[e.keyCode] = false;
	// });

	var state = 1;
	var canvas = $('#gameCanvas')[0].getContext('2d');

	// Hero
	var hero = new Image();
	hero.src = "SmileJust.png";
	hero.alive = true;
	hero.X = (canvasWidth/2)-(hero.width/2);
	hero.Y = (canvasHeight/2)-(hero.height/2);

	// Angry Smile
	var angry = new Image();
	angry.src = "SmileAngry.png";
	angry.alive = true;
	angry.dizzy = false;
	angry.X = Math.floor(Math.random() * (canvasWidth-100));
	angry.Y = Math.floor(Math.random() * (canvasHeight-100));

	// Heart
	var heart = new Image();
	heart.src = "BlackHeart.png";
	heart.alive = true;
	heart.X = Math.floor(Math.random() * (canvasWidth-100));
	heart.Y = Math.floor(Math.random() * (canvasHeight-100));

	// Girl
	var girl = new Image();
	girl.src = "SmileGirl.png";
	girl.alive = true;
	girl.X = 1;
	girl.Y = Math.floor(Math.random() * (canvasHeight-100));	

	// Bomb
	var bomb = new Image();
	bomb.src = "SmileBomb.png";
	bomb.alive = false;

	setInterval(function() {
		update();
		draw();
	}, 1000/FPS);

	function update() {
		// Hero behavior
		if (keysDown[32] && keysDown[37]) {		
			bomb.X = hero.X;// - bomb.width/2;
			bomb.Y = hero.Y;// - bomb.height/2;
			bomb.alive = true;
			bomb.direction = -1;
			
		}
		if (keysDown[32] && keysDown[39]) {
			bomb.X = hero.X + hero.width;
			bomb.Y = hero.Y;// - bomb.height/2;
			bomb.alive = true;
			bomb.direction = 1;
		}
		if (keysDown[37]) {
			hero.X -= 10;
		}
		if (keysDown[38]) {
			hero.Y -= 10;
		}
		if (keysDown[39]) {
			hero.X += 10;
		}
		if (keysDown[40]) {
			hero.Y += 10;
		}
		if (keysDown[49]) {
			hero.src = "SmileJust.png";
			state = 1;
		}
		if (keysDown[50]) {
			hero.src = "SmileBiggrin.png";
			state = 2;
		}
		if (keysDown[51]) {
			hero.src = "SmileGrimace.png";
			state = 3;
		}
		if (keysDown[52]) {
			hero.src = "SmileConfused.png";
			state = 4;
		}
		if (keysDown[53]) {
			hero.src = "SmileWhat.png";
			state = 5;
		}


		hero.X = clamp(hero.X, 0, canvasWidth - hero.width);
		hero.Y = clamp(hero.Y, -70, canvasHeight - hero.height + 70);

		// Angry behavior
		if (state == 0) {					// state == 0, hero death
			// angry.X += 1;
			// angry.Y += 1;
			location.reload();
		}
		else if (state == 3) {
			angry.X += (hero.X-angry.X)/8;
			angry.Y += (hero.Y-angry.Y)/8;
		}
		else if (state == 2) {
			angry.X -= (hero.X-angry.X)/8;
			angry.Y -= (hero.Y-angry.Y)/8 ;
		}
		else {
			// var where = Math.random();
			// if (where > 0.2) {
				// var randomX = Math.random();
				// angry.X = randomX > 0.4 ? angry.X+30 : angry.X-30;
			// angry.X = angry.X + Math.sin(angry.X+0.1)*10;
			
			// }
			// else {
			// 	var randomY = Math.random();
			// 	angry.Y = randomY > 0.5 ? angry.Y+30 : angry.Y-30;
			// }
			// if (angry.dizzy) {

			// }
			// else {
			angry.X += 1;
			angry.Y = angry.Y + Math.sin(0.05*angry.X)*5;	
			// }
		}

		// angry.X = clamp(angry.X, 0, canvasWidth - angry.width);
		// angry.Y = clamp(angry.Y, 0, canvasHeight - angry.height);

		// Girl behavior
		girl.X += 1;
		girl.Y += 0;//girl.Y + Math.sin(0.05*girl.X)*5;
		// girl.X = clamp(girl.X, 0, canvasWidth - girl.width);
		// girl.Y = clamp(girl.Y, 0, canvasHeight - girl.height);

		// Collision
		if ((Math.abs(hero.X-angry.X)<30) && (Math.abs(hero.Y-angry.Y)<30)) {
			hero.src = "explosion.png";
			// angry.alive = false;
			// angry.X += 50;
			// angry.Y = 0;
			state = 0;
			// clearInterval(intervalHandler);

			// canvas.clearRect(angry.X, angry.Y, angry.width, angry.height);
			// delete angry;
			// angry.src = "smileLaughing.png";
		}

		// Heart interaction
		if ((Math.abs(hero.X-heart.X)<150) && (Math.abs(hero.Y-heart.Y)<150)) {
			if (!angry.dizzy) {
				angry.X += (hero.X-angry.X)/2;
				angry.Y += (hero.Y-angry.Y)/2;
			}
		}

		// Heart interaction
		if ((Math.abs(hero.X-heart.X)<30) && (Math.abs(hero.Y-heart.Y)<30)) {
			hero.src = "SmileCocktail.png";
			heart.X = Math.floor(Math.random() * (canvasWidth-100));
			heart.Y = Math.floor(Math.random() * (canvasHeight-100));
		}

		// Girl interaction
		if ( ((Math.abs(girl.X-hero.X)<200) && (Math.abs(girl.Y-hero.Y)<200) )||
			 ((Math.abs(girl.X-angry.X)<200) && (Math.abs(girl.Y-angry.Y)<200) )) {
				hero.src = "SmileLove.png";
				angry.src = "SmileBlushing.png";
				angry.dizzy = true;

				angry.X += (girl.X-angry.X)/10;
				angry.Y += (girl.Y-angry.Y)/10;
				hero.X += (girl.X-hero.X)/10;
				hero.Y += (girl.Y-hero.Y)/10;
		}

		// Bomb interaction
		if (bomb.alive) {
			bomb.X = bomb.X + 5*bomb.direction;
			// bomb.Y = bomb.Y + Math.sin(0.1*bomb.X);//-(bomb.X)^2 + 5*bomb.X + 1;
			if ((Math.abs(bomb.X-angry.X)<20) && (Math.abs(bomb.Y-angry.Y)<20)) {
				bomb.alive = false;
				angry.src = "explosion.png";
				angry.dizzy = true;
			}
		}


	}

	function clamp(x, min, max) {
		return x < min ? min : (x > max ? max : x);
	}

	function draw() {
		canvas.clearRect(0, 0, canvasWidth, canvasHeight);
		canvas.strokeRect(0, 0, canvasWidth, canvasHeight);
		if (hero.alive) { canvas.drawImage(hero, hero.X, hero.Y); }
		if (angry.alive) { canvas.drawImage(angry, angry.X, angry.Y); }
		if (heart.alive) { canvas.drawImage(heart, heart.X, heart.Y); }
		if (bomb.alive) { canvas.drawImage(bomb, bomb.X, bomb.Y); }
		if (girl.alive) { canvas.drawImage(girl, girl.X, girl.Y); }
		// canvas.fillStyle = "#FF0000";
		// canvas.fillRect(0,0,150,75);
		// canvas.moveTo(heroX, heroY);
		// canvas.lineTo(heroX, heroY);
		// canvas.stroke();

	}


	// $(hero).load(function() {
	// 	canvas.drawImage(hero,
	// 					 (canvasWidth/2)-(hero.width/2),
	// 	 				 (canvasHeight/2)-(hero.height/2));	
	// })
	
})
