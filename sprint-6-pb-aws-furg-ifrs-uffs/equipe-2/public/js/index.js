const botaoV1 = document.querySelector(".web-button-v1");
const botaoV2 = document.querySelector(".web-button-v2");
const botaoV3 = document.querySelector(".web-button-v3");
const route = "https://bamhh6pajl.execute-api.us-east-1.amazonaws.com/";

botaoV1.addEventListener("click", function () {
  try {
    var valor = this.querySelector("img").getAttribute("value");
    var phrase = document.getElementById("phrase").value;
    if (validarInput()) {
      fetch(`${route}${valor}/tts`, {
        method: "POST",
        body: JSON.stringify({ phrase: phrase }),
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
      })
        .then((response) => response.text())
        .then((data) => pegarDados(JSON.parse(data)));
    }
  } catch (error) {
    console.error(error);
  }
});

botaoV2.addEventListener("click", function () {
  try {
    var valor = this.querySelector("img").getAttribute("value");
    var phrase = document.getElementById("phrase").value;
    if (validarInput()) {
      fetch(`${route}${valor}/tts`, {
        method: "POST",
        body: JSON.stringify({ phrase: phrase }),
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
      })
        .then((response) => response.text())
        .then((data) => pegarDados(JSON.parse(data)));
    }
  } catch (error) {
    console.error(error);
  }
});

botaoV3.addEventListener("click", function () {
  try {
    var valor = this.querySelector("img").getAttribute("value");
    var phrase = document.getElementById("phrase").value;
    if (validarInput()) {
      fetch(`${route}${valor}/tts`, {
        method: "POST",
        body: JSON.stringify({ phrase: phrase }),
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
      })
        .then((response) => response.text())
        .then((data) => pegarDados(JSON.parse(data)));
    }
  } catch (error) {
    console.error(error);
  }
});

function pegarDados(data) {
  document.getElementById(
    "frase-recebida"
  ).innerHTML = `Frase: "${data.received_phrase}"`;

  document.getElementById("url").innerHTML = data.url_to_audio;
  document.getElementById("frase-recebida").style.display = "block";
  document.getElementById("hash").href = data.url_to_audio;
  document.getElementById(
    "data"
  ).innerHTML = `Data da criação: ${data.created_audio}`;

  if (data.unique_id) {
    document.getElementById("hash").innerHTML = `Hash: ${data.unique_id}`;
  }
  document.getElementById("audio_player").src = data.url_to_audio;

  document.getElementById("resposta").style.display = "block";
  document.getElementById("audio_player").style.display = "block";
}

function changeTextColor() {
  var input = document.getElementById("phrase");
  var textColor = input.value ? "#ffa15e" : "black"; // Cor do texto quando há texto digitado

  input.style.color = textColor;
}

function validarInput() {
  var inputFrase = document.getElementById("phrase");
  var valorFrase = inputFrase.value;
  valorFrase = valorFrase.trim();

  if (valorFrase === "") {
    alert("Por favor, digite uma frase válida.");

    return false;
  }

  return true;
}
