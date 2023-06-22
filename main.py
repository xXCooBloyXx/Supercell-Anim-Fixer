import os

folder_path = './input'

if not os.path.exists('input'):
	os.makedirs('input')

glb_files = []
for file in os.listdir(folder_path):
    if file.endswith(".glb") and "_geo.glb" not in file:
        glb_files.append(file)

for glb_file in glb_files:
	file_path = os.path.join(folder_path, glb_file)
	try:
		with open(file_path, "rb") as f:
			data = f.read()
		data = data.replace(b'"mesh"', b'"shem"')
		with open(file_path, "wb") as f:
			try:
				f.write(data)
				print(f"Succesfully fixed {glb_file}!")
			except Exception as e1:
				print(f"Can't save {glb_file}! Error: {e1}")
				pass
	except Exception as e2:
		print(f"Can't fix {glb_file}! Error: {e2}")
print("Done!")
os.system("pause")
