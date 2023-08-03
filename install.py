import launch

# TODO: add pip dependency if need extra module only on extension

# if not launch.is_installed("insightface"):
#     launch.run_pip("install insightface==0.7.3", "requirements for face-detection-extension")

# if not launch.is_installed("onnxruntime"):
#     launch.run_pip("install onnxruntime", "requirements for face-detection-extension")


needs_install = True
if needs_install:
    import launch
    import os
    import pkg_resources

    req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

    with open(req_file) as file:
        for package in file:
            try:
                package = package.strip()
                if '==' in package:
                    package_name, package_version = package.split('==')
                    if not launch.is_installed(package_name):
                        launch.run_pip(f"install {package}", "requirements for face-detection-extension")
                    else:
                        installed_version = pkg_resources.get_distribution(package_name).version
                        if installed_version != package_version:
                            launch.run_pip(f"install {package}", f"face-detection-extension requirement: changing {package_name} version from {installed_version} to {package_version}")
                elif not launch.is_installed(package):
                    launch.run_pip(f"install {package}", f"face-detection-extension requirement: {package}")
            except Exception as e:
                print(e)
                print(f'Warning: Failed to install {package}, some preprocessors may not work.')