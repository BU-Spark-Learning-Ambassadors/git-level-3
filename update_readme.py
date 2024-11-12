from datetime import datetime

readme_path = "README.md"

# Get current date
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(readme_path, "r") as file:
    content = file.readlines()

for i, line in enumerate(content):
    if line.startswith("Last updated:"):
        content[i] = f"Last updated: {current_datetime}\n"
        break
else:
    content.append(f"\nLast updated: {current_datetime}\n")

with open(readme_path, "w") as file:
    file.writelines(content)