
// anon function prevents user from console.log(pin)
(function(pin) {
  console.log(pin);

  let shot = pin-7;
  let feedbackStr = "";

  // the only way to get out of the while looping is guessing the correct pin
  while (!(shot === pin)) {
    shot = prompt(`${feedbackStr}Please enter a numeric PIN: \t(${pin})`);

    shot = shot.trim(); // remove inconveniently placed spaces
    if (shot === "") {  /*  its necessary to validate emtpy shot since it could turn shot 
                            to 0 when casted into Number */
      feedbackStr = "Enter numeric values on the prompt!\n\n";
      continue;
    }

    if (/^[0-9]*$/.test(shot)) {  // regex filters for strictly digits input 
      shot = Number(shot);
      if (shot > pin || shot < pin) feedbackStr = getFeedbackParameters(pin, shot);
    } else {
      feedbackStr = "Your PIN is a number of variable length.\n"+
                    "Make sure to next time input digits only!\n\n";
    }
  }
  
  congrats(shot);
})(Math.floor(Math.random()*7777)); // calls the anon function

function congrats(shot) {
  document.getElementById("pin").innerText = "Congratulations for guessing right! \nYour PIN ::: " + shot;
}

function getFeedbackParameters(pin, shot) {
  let value = "";
  if (shot > pin) value = "lower";
  else if (shot < pin) value = "higher";

  if (shot/2 >= pin) value = "much lower";
  else if (shot <= pin/2) value = "much higher";

  return `Your next shot should be ${value} than the last one!\n\n`;
}
