const ws = new WebSocket('wss://192.168.1.79:3333/');
let gyroscopeData = { x: '', y: '', z: '' }
let accelerometerData = { x: '', y: '', z: '' }

function initSensors() {
  const gyroscope = new Gyroscope({ frequency: 60 });
  const accelerometer = new Accelerometer({ frequency: 60 });

  gyroscope.addEventListener('reading', e => {
    gyroscopeData.x = gyroscope.x;
    gyroscopeData.y = gyroscope.y;
    gyroscopeData.z = gyroscope.z;
  });

  accelerometer.addEventListener('reading', e => {
    accelerometerData.x = accelerometer.x;
    accelerometerData.y = accelerometer.y;
    accelerometerData.z = accelerometer.z;
  });

  gyroscope.start();
  accelerometer.start();
}

window.onload = function () {
  initSensors();
  document.body.addEventListener('touchstart', e => {
    document.body.classList.add('touched');
    interval = setInterval(() => {
      ws.send(`${accelerometerData.x} ${accelerometerData.y} ${accelerometerData.z} ${gyroscopeData.x} ${gyroscopeData.y} ${gyroscopeData.z}`)
    }, 10);
  })

  document.body.addEventListener('touchend', e => {
    document.body.classList.remove('touched');
    ws.send('end')
    clearInterval(interval);
  });
}

ws.onmessage = e => {
  console.log('Message from server:', e.data)
};