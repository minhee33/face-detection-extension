import launch

# TODO: add pip dependency if need extra module only on extension

if not launch.is_installed("insightface"):
    launch.run_pip("install insightface==0.7.3", "requirements for face-detection-extension")

if not launch.is_installed("onnxruntime"):
    launch.run_pip("install onnxruntime", "requirements for face-detection-extension")