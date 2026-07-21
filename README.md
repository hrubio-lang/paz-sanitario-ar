# QR+AR — Proyecto PAZ Sanitario

Modelo: **MKA_SAN_3D_W_XX** · La Paz, BCS · 12 Niveles

Escanea el QR → abre el modelo 3D en el celular → botón "Ver en AR" para proyectarlo en la mesa, escritorio o en obra.

---

## Flujo completo

### Paso 1: Exportar FBX desde Revit
1. En Revit, abre el modelo `MKA_SAN_3D_W_XX`
2. Abre la vista 3D `{3D - h.rubio45KQZ}` (ID: 1825054)
3. **File → Export → FBX**
4. Guarda como `PAZ_SAN_3D.fbx` en `C:\Users\SOHERSA\Desktop\`

### Paso 2: Convertir .FBX a .GLB
El visor AR necesita formato **glTF 2.0 (.GLB)**.

**Opción A — Blender (recomendada, gratis):**
```
1. Abre Blender → File → Import → FBX (.fbx)
2. Selecciona PAZ_SAN_3D.fbx → Import
3. File → Export → glTF 2.0 (.glb/.gltf)
4. Formato: glTF Binary (.glb)
5. Guarda como modelo.glb en esta carpeta (qr_ar_paz/)
```

**Opción B — fbx2gltf (línea de comandos):**
```
npm install -g fbx2gltf
fbx2gltf --binary -i PAZ_SAN_3D.fbx -o modelo.glb
```

**Opción C — Servicio online:**
- https://products.aspose.app/3d/conversion/fbx-to-glb (gratis, sin registro)
- Sube el FBX, descarga el GLB, renómbralo a `modelo.glb`

> ⚠️ **Archivos grandes**: Si el GLB pesa >50MB, usa Blender para simplificar la geometría (Decimate modifier) o exporta solo elementos visibles.

### Paso 3: Publicar en GitHub Pages (HTTPS requerido para AR)
```bash
# Desde esta carpeta (qr_ar_paz/)
git init
git add .
git commit -m "QR+AR Proyecto PAZ Sanitario"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/paz-sanitario-ar.git
git push -u origin main

# En GitHub → Settings → Pages:
#   Source: Deploy from branch
#   Branch: main  /root
#   Save
```

URL final: `https://TU_USUARIO.github.io/paz-sanitario-ar/`

### Paso 4: Generar QR
```bash
pip install qrcode[pil]
py -3 generar_qr.py "https://TU_USUARIO.github.io/paz-sanitario-ar/"
```

### Paso 5: Insertar QR en plano de Revit
1. Abre `MKA_SAN_3D_W_XX` en Revit
2. Sheet PORTADA (ID: 173066) u hoja designada
3. **Insert → Image** → selecciona `QR_PAZ_SANITARIO_AR.png`
4. Tamaño recomendado: 2×2 cm (como los QR previos del proyecto)

### Paso 6: Probar
1. Escanea el QR con la cámara del celular
2. Debe abrirse el visor 3D en Chrome/Safari
3. Gira, haz zoom con los dedos
4. Toca el botón **"Ver en AR 🥽"**
5. Apunta la cámara al piso/mesa → el modelo aparece en tu espacio

---

## Archivos

| Archivo | Descripción |
|---|---|
| `index.html` | Visor 3D + AR (modelviewer.dev de Google) |
| `modelo.glb` | Modelo 3D en formato glTF (generado en Paso 2) |
| `generar_qr.py` | Script para generar el código QR |
| `QR_PAZ_SANITARIO_AR.png` | QR generado (se inserta en el plano) |

---

## Compatibilidad AR

| Dispositivo | AR | Requisito |
|---|---|---|
| Android | ✅ Scene Viewer | Chrome 81+ + ARCore |
| iPhone/iPad | ✅ Quick Look | Safari + iOS 12+ |
| Desktop | ❌ Solo 3D | Cualquier navegador moderno |

---

## Referencias
- [modelviewer.dev](https://modelviewer.dev/) — Google, gratuito, open source
- [AR Requirements](https://modelviewer.dev/docs/ar.html) — Requisitos para AR