const ws = new WebSocket('wss://192.168.1.79:3333/');
const messages = document.createElement('ul');

const msg = 'Hello server';

// Connection opened
ws.onopen = () => {
  setInterval(() => {
    ws.send(msg);
  }, 5000);
}

// Listen for messages
ws.onmessage = e => {
  console.log('Message from server:', e.data)
  // const messages = document.getElementsByTagName('ul')[0],
  //   message = document.createElement('li'),
  //   content = document.createTextNode(event.data);
  // message.appendChild(content);
  // messages.appendChild(message);
};
// document.body.appendChild(messages);