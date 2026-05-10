import subprocess
import os
import pyperclip
from datetime import datetime

# ✏️ CHANGE THIS PATH to your repo folder
repo_folder = r" C:\Users\adipa\OneDrive\Desktop\Basics"

# Get solution from clipboard
solution = pyperclip.paste()

# Ask problem details
print("🔥 LeetCode Auto Pusher")
print("------------------------")
day = input("Day number (e.g. 01): ")
problem = input("Problem name (e.g. two_sum): ")
difficulty = input("Difficulty (easy/medium/hard): ")

# Create filename
filename = f"day{day}_{problem}.py"
filepath = os.path.join(repo_folder, "leetcode", filename)

# Create leetcode folder if not exists
os.makedirs(os.path.join(repo_folder, "leetcode"), exist_ok=True)

# Save file with template
with open(filepath, "w") as f:
    f.write(f"# Problem: {problem.replace('_', ' ').title()}\n")
    f.write(f"# Difficulty: {difficulty}\n")
    f.write(f"# Date: {datetime.now().strftime('%Y-%m-%d')}\n")
    f.write(f"# LeetCode Day: {day}\n\n")
    f.write(solution)

print(f"\n✅ File created: {filename}")

# Auto push to GitHub
os.chdir(repo_folder)
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Day {day}: solved {problem} ({difficulty})"])
subprocess.run(["git", "push"])

print(f"\n🚀 Pushed to GitHub successfully!")