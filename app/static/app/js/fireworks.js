initFireWorks()
initCountDown()

function initFireWorks(){
  const containers = document.querySelectorAll('.fireworks-container')
  containers.forEach((container,index) => {
    index+=1;
    const fireworks = new Fireworks(container, {
      hue: { min: 0, max: 360 },
      delay: { min: 50/index, max: 100/index },
      brightness: {min: 80, max: 100},
      rocketsPoint: 50,
      opacity: 1,
      speed: 1/index,
      acceleration: 1.05,
      friction: 0.97,
      gravity: 2,
      particles: 200/index,
      trace: 4/index,
      explosion: 40/index,
    })
    fireworks.start()
  })
}
function initCountDown() {
  const countdown = setInterval(() => {
    const nextYear = new Date().getFullYear() + 1;
    const nextYearDate = new Date(nextYear, 0, 1);
    const diff = countDownDate(nextYearDate);

    Object.keys(diff).forEach(key => {
      document.querySelector("." + key).textContent = diff[key];
    })

    document.querySelectorAll('.yeardigit').forEach((digit, index) => {
      digit.textContent = String(nextYear)[index];
    })
  }, 1)
}

function countDownDate(date_future) {
  const date_now = new Date();
  let seconds = Math.floor((date_future - (date_now)) / 1000);
  let minutes = Math.floor(seconds / 60);
  let hours = Math.floor(minutes / 60);
  let days = Math.floor(hours / 24);

  hours = hours - (days * 24);
  minutes = minutes - (days * 24 * 60) - (hours * 60);
  seconds = seconds - (days * 24 * 60 * 60) - (hours * 60 * 60) - (minutes * 60)
  return { days, hours, minutes, seconds }
}
