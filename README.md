# zed_live_mesh
extract 3d mesh in .obj format using zed 2i stereo camera


# ZED Live Mesh Reconstruction

This project uses the ZED 2i stereo camera and the ZED SDK to perform live 3D spatial mapping and generate a mesh of the surrounding environment. The output mesh is saved as an `.obj` file.

---

## 📸 Overview

The script `live_mesh.py` performs the following steps:

1. Opens the ZED camera
2. Enables **positional tracking**
3. Enables **spatial mapping**
4. Captures 3000 frames to reconstruct a 3D map
5. Extracts, filters, and saves the mesh as `mesh.obj`

---

## 🚀 Requirements

- **Hardware**: ZED 2 or ZED 2i stereo camera
- **OS**: Ubuntu 22.04
- **ZED SDK**: v5.0.5 (with CUDA 12.8 + TensorRT 10.9)
- **Python**: 3.6 to 3.10 (Python 3.11+ not supported)
- **Libraries**:
  - `pyzed` (Python API for ZED SDK)

---

## 🛠️ Installation

### 1. Install ZED SDK

Download from:  
👉 [https://www.stereolabs.com/developers/release/](https://www.stereolabs.com/developers/release/)

Install it:

```bash
chmod +x ZED_SDK_Ubuntu22_cuda12.8_tensorrt10.9_v5.0.5.zstd.run
./ZED_SDK_Ubuntu22_cuda12.8_tensorrt10.9_v5.0.5.zstd.run
```

## Run code

```python3 live_mesh.py --frame 500
```
