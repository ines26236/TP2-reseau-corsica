async function updateCounter(action) {
  const response = await fetch(`/counter/${action}`, { method: "POST" });
  const data = await response.json();
  document.getElementById("counter").innerText = data.counter;
}

async function getCounter() {
  const response = await fetch("/counter");
  const data = await response.json();
  document.getElementById("counter").innerText = data.counter;
}

document.getElementById("inc").onclick = () => updateCounter("inc");
document.getElementById("dec").onclick = () => updateCounter("dec");

getCounter();
