function safelyPlay(funcName) {
  try {
    if (typeof window[funcName] === "function") {
      window[funcName]();
    } else if (funcName === 'playClick') {
      console.log("Click sound skipped (function not defined).");
    } else if (funcName === 'playWin') {
      console.log("Win sound skipped (function not defined).");
    } else if (funcName === 'showConfetti') {
      console.log("Confetti effect skipped (function not defined).");
    }
  } catch(e) {
    console.warn("Effect error:", e);
  }
}

/* ==================== NUMBER GUESSING GAME ==================== */
async function startGame(){
  safelyPlay('playClick');
  let level = document.getElementById("level").value;

  try {
    let res = await fetch("/start", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({level: level})
    });

    let data = await res.json();
    let msgBox = document.getElementById("msg");
    msgBox.innerText = data.msg;
    msgBox.style.color = "#00f0ff"; // Reset to Neon Cyan

    document.getElementById("range").innerText = "Range: " + data.range;
    document.getElementById("attempts").innerText = "Attempts left: " + data.left;
  } catch (error) {
    console.error("Error starting game:", error);
    alert("Could not connect to the backend server. Make sure Python is running!");
  }
}

async function sendGuess(){
  safelyPlay('playClick');
  let guessInput = document.getElementById("guess");
  let guess = guessInput.value;

  if(guess === ""){
    alert("Please enter a number!");
    return;
  }

  try {
    let res = await fetch("/guess", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({guess: guess})
    });

    let data = await res.json();
    let msgBox = document.getElementById("msg");
    msgBox.innerText = data.msg;

    // Color code responses dynamically
    if(data.msg.includes("Higher") || data.msg.includes("Lower")){
      msgBox.style.color = "#00f0ff"; // Cyan
    }
    else if(data.msg.includes("Close") || data.msg.includes("there")){
      msgBox.style.color = "#ffb700"; // Gold
    }
    else if(data.msg.includes("won")){
      msgBox.style.color = "#39ff14"; // Green
      safelyPlay('playWin');
      safelyPlay('showConfetti');
    }
    else {
      msgBox.style.color = "#ff007f"; // Magenta/Red
    }

    if(!data.end){
      document.getElementById("attempts").innerText = "Attempts left: " + data.left;
    } else {
      document.getElementById("attempts").innerText = "Game Over";
    }
  } catch (error) {
    console.error("Error sending guess:", error);
  }
}

// /* ==================== MIND READING GAME ==================== */
// // Using local scopes so they don't conflict or get wiped out
 window.mindGame = {
   minRange: 1,
   maxRange: 100,
   currentGuess: 50,
   isActive: false
 };

 function startMindGame() {
   safelyPlay('playClick');
   window.mindGame.minRange = 1;
   window.mindGame.maxRange = 100;
   window.mindGame.currentGuess = Math.floor((window.mindGame.minRange + window.mindGame.maxRange) / 2);
  window.mindGame.isActive = true;
  
   let msgBox = document.getElementById("msg");
   msgBox.innerText = "Is your number " + window.mindGame.currentGuess + "?";
   msgBox.style.color = "#ff007f";
 }

 function mindFeedback(feedback) {
   safelyPlay('playClick');
  let msgBox = document.getElementById("msg");

   if (!window.mindGame.isActive) {
     msgBox.innerText = "Please click 'Start Mind Reading' first!";
     return;
   }

   if (feedback === 'correct') {
      msgBox.innerText = "🎉 Awesome! I read your mind!";
     msgBox.style.color = "#39ff14";
     safelyPlay('playWin');
     safelyPlay('showConfetti');
     window.mindGame.isActive = false;
     return;
   }

   if (feedback === 'high') {
     window.mindGame.maxRange = window.mindGame.currentGuess - 1;
   } else if (feedback === 'low') {
     window.mindGame.minRange = window.mindGame.currentGuess + 1;
  }

  if (window.mindGame.minRange > window.mindGame.maxRange) {
    msgBox.innerText = "Wait, are you sure? Check your hints!";
    msgBox.style.color = "#ffb700";
    window.mindGame.isActive = false;
    return;
   }

  window.mindGame.currentGuess = Math.floor((window.mindGame.minRange + window.mindGame.maxRange) / 2);
   msgBox.innerText = "Is your number " + window.mindGame.currentGuess + "?";
 }
