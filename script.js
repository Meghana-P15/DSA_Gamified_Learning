async function startGame(){

  let level = document.getElementById("level").value;

  let res = await fetch("/start", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({level: level})
  });

  let data = await res.json();

  document.getElementById("msg").innerText = data.msg;

  // RANGE
  document.getElementById("range").innerText =
    "Range: " + data.range;

  // ATTEMPTS
  document.getElementById("attempts").innerText =
    "Attempts left: " + data.left;
}


async function sendGuess(){

  let guess = document.getElementById("guess").value;

  if(guess === ""){
    alert("Enter number!");
    return;
  }

  let res = await fetch("/guess", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({guess: guess})
  });

  let data = await res.json();

  document.getElementById("msg").innerText = data.msg;

  if(!data.end){
    document.getElementById("attempts").innerText =
      "Attempts left: " + data.left;
  } else {
    document.getElementById("attempts").innerText =
      "Game Over";
  }
}