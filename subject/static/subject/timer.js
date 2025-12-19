let timer;
let totalSeconds = 0;
let isRunning = false;

function formatTime(sec) {
  let h = Math.floor(sec / 3600);
  let m = Math.floor((sec % 3600) / 60);
  let s = sec % 60;

  return `${String(h).padStart(2, "0")}:${String(m).padStart(2, "0")}:${String(
    s
  ).padStart(2, "0")}`;
}

function startTimer() {
  if (!isRunning) {
    isRunning = true;
    timer = setInterval(() => {
      totalSeconds++;
      document.getElementById("display").innerText = formatTime(totalSeconds);
    }, 1000);
  }
}

function pauseTimer() {
  if (isRunning) {
    clearInterval(timer);
    isRunning = false;
  }
}

function stopAndSave() {
  pauseTimer();
  document.getElementById("timeInput").value = totalSeconds;
}
