let ws = new WebSocket("ws://" + location.host + "/ws");

ws.onmessage = e => {
    const data = JSON.parse(e.data);
    document.getElementById("counter").innerText = data.counter;
};

function updateCounter(i) {
    const current = parseInt(document.getElementById("counter").innerText);
    const newCounter = current + i;
    ws.send(JSON.stringify({ counter: newCounter }));
}

document.getElementById("inc").onclick = () => updateCounter(1);
document.getElementById("dec").onclick = () => updateCounter(-1);
