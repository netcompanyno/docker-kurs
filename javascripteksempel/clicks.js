function imageClicked() {
    sendClick().then(() => updateClicks());
}

function updateClicks() {
    fetchClicks().then(count =>
        document.getElementById("clickCountText").innerText = 'Bildet har blitt klikket på ' + count + ' ganger!'
    );
}

function fetchClicks() {
    console.log("fetch");
    return fetch('http://localhost:8080')
        .then(res => res.text())
}

function sendClick() {
    console.log("send")
    return fetch('http://localhost:8080', {method: 'POST'})
        .then(res => res.text());
}

