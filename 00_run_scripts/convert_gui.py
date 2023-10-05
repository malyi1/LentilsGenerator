import os
import subprocess

for filename in os.listdir("ui"):
    if filename.endswith(".ui"):
        input_file = os.path.join("ui", filename)
        output_file = os.path.join("ui", f"{os.path.splitext(filename)[0]}_UI.py")
        subprocess.run(["pyuic6", "-x", input_file, "-o", output_file])
