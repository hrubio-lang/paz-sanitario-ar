"""
Genera QR para el visor AR del Proyecto PAZ - Sanitario.
Escanea el QR → abre el modelo 3D en el navegador con opción AR.

Uso:
    py -3 generar_qr.py "https://TU_USUARIO.github.io/paz-sanitario-ar/"

Requisitos: pip install qrcode[pil]
"""

import qrcode
import sys
import os

def generar_qr(url: str, salida: str = "QR_PAZ_SANITARIO_AR.png"):
    if not url.startswith("http"):
        print("❌ La URL debe comenzar con http:// o https:// - generar_qr.py:17")
        sys.exit(1)
    
    qr = qrcode.QRCode(
        version=None,  # auto
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # 15% - permite logo
        box_size=12,
        border=3,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="#1a1a2e", back_color="white")
    img.save(salida)
    
    print(f"✅ QR generado: {salida} - generar_qr.py:33")
    print(f"URL: {url} - generar_qr.py:34")
    print(f"Tamaño: {img.size[0]}x{img.size[1]} px - generar_qr.py:35")
    print()
    print("📱 PRUEBA: Escanea este QR con tu celular. - generar_qr.py:37")
    print("Debe abrir el visor 3D con opción 'Ver en AR'. - generar_qr.py:38")
    return salida

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("= - generar_qr.py:43" * 60)
        print("QR AR  Proyecto PAZ Sanitario - generar_qr.py:44")
        print("= - generar_qr.py:45" * 60)
        print()
        print("Uso: - generar_qr.py:47")
        print(f"py 3 {sys.argv[0]} \"URL_DEL_VISOR\" - generar_qr.py:48")
        print()
        print("Ejemplo (GitHub Pages): - generar_qr.py:50")
        print(f'py 3 {sys.argv[0]} "https://TUNOMBRE.github.io/pazsanitarioar/" - generar_qr.py:51')
        print()
        print("Ejemplo (otro hosting): - generar_qr.py:53")
        print(f'py 3 {sys.argv[0]} "https://miapp.vercel.app/" - generar_qr.py:54')
        print()
        print("= - generar_qr.py:56" * 60)
        sys.exit(0)
    
    generar_qr(sys.argv[1])