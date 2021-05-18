async function pick_file() {
    let inputText = document.getElementById("input-box").value;
    let file_div = document.getElementById("file-name");
    // Call into Python so we can access the file system
    // Вызов Python, чтобы мы могли получить доступ к файловой системе
    let random_filename = await eel.pick_file(inputText)();
    file_div.innerHTML = random_filename;
}

function windowResize() {
    window.resizeTo(450, 450)
}