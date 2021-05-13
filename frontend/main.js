//не понятно пока
eel.expose(say_hello_js); // Expose this function to Python


function say_hello_js(x) {
    console.log("Hello from " + x);
}

say_hello_js("js - say_hello_js");

eel.say_hello_py("js - eel.say_hello_py"); // Call a Python function


