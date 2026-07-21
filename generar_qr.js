const QRCode = require('qrcode');

const url = 'https://cdn.jsdelivr.net/gh/hrubio-lang/paz-sanitario-ar@main/index.html';
const output = 'QR_PAZ_SANITARIO_AR.png';

QRCode.toFile(output, url, {
    color: { dark: '#1a1a2e', light: '#ffffff' },
    width: 600,
    margin: 2
})
.then(() => {
    console.log('QR generado: - generar_qr.js:12' + output);
    console.log('URL: - generar_qr.js:13' + url);
})
.catch(err => console.error('Error: - generar_qr.js:15', err));