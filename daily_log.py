"""
daily_log.py
============
Run this every day after your learning session.
Takes only 2 minutes!

HOW TO USE:
    python daily_log.py

It will ask you 3 simple questions, then:
✅ Save your learning note
✅ Commit to GitHub automatically
✅ Generate your LinkedIn post
"""

import os
import subprocess
from datetime import datetime

def ask(question):
    print(f"\n{question}")
    return input("👉 Your answer: ").strip()

def save_note(date_str, topic, what_learned, code_file):
    """Save daily learning note to notes folder."""
    os.makedirs("notes", exist_ok=True)
    
    note_file = f"notes/{date_str}.md"
    
    content = f"""# 📅 {date_str} — Daily Learning Log

## Topic Studied
{topic}

## What I Learned
{what_learned}

## Code Practiced
{f'See: basics/{code_file}' if code_file else 'No code file today'}

## LinkedIn Post (Copy this 👇)
---
🐍 Day {get_day_count()} of my Python learning journey!

Today I studied: **{topic}**

Key takeaway: {what_learned[:100]}...

Consistency is the key. Learning every single day. 💪

#Python #Learning #100DaysOfCode #OpenToWork
---
"""
    
    with open(note_file, "w") as f:
        f.write(content)
    
    return note_file

def get_day_count():
    """Count how many daily logs exist."""
    if not os.path.exists("notes"):
        return 1
    return len([f for f in os.listdir("notes") if f.endswith(".md")]) + 1

def git_push(files, message):
    """Add, commit and push files to GitHub."""
    for f in files:
        subprocess.run(["git", "add", f])
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push", "origin", "main"])

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    day_num = get_day_count()
    
    print("=" * 50)
    print(f"📚 DAILY LEARNING LOG — Day {day_num}")
    print(f"📅 Date: {today}")
    print("=" * 50)
    print("\nJust answer 3 quick questions! Takes 2 minutes.\n")
    
    # Question 1
    topic = ask("1️⃣  What topic did you study today?\n   (e.g. 'Python loops', 'Functions', 'Lists')")
    
    # Question 2
    what_learned = ask("2️⃣  In 1-2 lines, what did you learn?\n   (e.g. 'Learned how for loops work with range()')")
    
    # Question 3
    code_file = ask("3️⃣  Did you save a code file today? Enter filename or press Enter to skip\n   (e.g. 'loops_practice.py')")
    
    # Save note
    note_file = save_note(today, topic, what_learned, code_file)
    
    print(f"\n✅ Note saved: {note_file}")
    
    # Files to commit
    files_to_push = [note_file]
    if code_file and os.path.exists(f"basics/{code_file}"):
        files_to_push.append(f"basics/{code_file}")
    
    # Git push
    print("\n📤 Pushing to GitHub...")
    commit_msg = f"Day {day_num}: Studied {topic} — {today}"
    git_push(files_to_push, commit_msg)
    
    print("\n" + "=" * 50)
    print("🎉 DONE! Here's your LinkedIn post (copy & paste):")
    print("=" * 50)
    print(f"""
🐍 Day {day_num} of my Python learning journey!

Today I studied: {topic}

Key takeaway: {what_learned}

Consistency is the key. Learning every single day 💪

#Python #Learning #100DaysOfCode #OpenToWork #Fresher
""")
    print("=" * 50)
    print("\n✅ GitHub updated ✅ Note saved ✅ LinkedIn post ready")
    print("Just copy the post above and paste on LinkedIn!")

if __name__ == "__main__":
    main()
