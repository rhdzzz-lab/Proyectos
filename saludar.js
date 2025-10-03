const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("¿Cuál es tu nombre? ", (nombre) => {
  if (nombre) {
    console.log("¡Hola, " + nombre + "! Bienvenido a JavaScript 😃");
  } else {
    console.log("No escribiste tu nombre 😅");
  }
  rl.close();
});
