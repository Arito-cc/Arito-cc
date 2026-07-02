import json
from pathlib import Path

GOAL = 150
MILESTONES = [25, 50, 100, 150]


def milestone_badge(total, milestone):
    if total >= milestone:
        color = "success"
        label = "Completed"
    elif milestone == min([m for m in MILESTONES if m > total], default=milestone):
        color = "orange"
        label = "In Progress"
    else:
        color = "lightgrey"
        label = "Locked"

    if milestone == GOAL and total >= GOAL:
        label = "Legendary"
        color = "gold"

    return (
        f"![{milestone}]"
        f"(https://img.shields.io/badge/{milestone}-{label.replace(' ', '%20')}-{color}"
        f"?style=for-the-badge)"
    )


def generate_leetcode_section():
    with open("stats.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    lc = data.get("leetcode", {})

    easy = lc.get("easy", 0)
    medium = lc.get("medium", 0)
    hard = lc.get("hard", 0)
    total = lc.get("solved", 0)

    percentage = int((total / GOAL) * 100) if GOAL else 0
    remaining = max(0, GOAL - total)

    filled = min(20, percentage // 5)
    progress_bar = "█" * filled + "░" * (20 - filled)

    badges = "\n".join(
        milestone_badge(total, milestone)
        for milestone in MILESTONES
    )

    return f"""
## 🧠 LeetCode Journey

| Total | Easy | Medium | Hard |
|------:|-----:|-------:|-----:|
| **{total}** | 🟢 {easy} | 🟡 {medium} | 🔴 {hard} |

### 🎯 Goal: {GOAL} Problems

```text
{progress_bar} {percentage}%

{total} / {GOAL} Problems Solved
{remaining} Remaining
````

### 🏆 Milestones

{badges}

### 🔗 Coding Profiles

* 💻 GitHub: [https://github.com/Arito-cc](https://github.com/Arito-cc)
* 🧩 LeetCode: [https://leetcode.com/u/Arito-cc/](https://leetcode.com/u/Arito-cc/)
* 📚 LeetCode Solutions: [https://github.com/Arito-cc/LeetCode-Solutions](https://github.com/Arito-cc/LeetCode-Solutions)
* 💼 LinkedIn: [https://linkedin.com/in/abhishekchaudharycc](https://linkedin.com/in/abhishekchaudharycc)
  """.strip()

def main():
template_path = Path("profile_template.md")
readme_path = Path("README.md")

```
template = template_path.read_text(encoding="utf-8")

leetcode_section = generate_leetcode_section()

final_readme = template.replace(
    "<!-- LEETCODE_SECTION -->",
    leetcode_section
)

readme_path.write_text(final_readme, encoding="utf-8")

print("README.md updated successfully!")
```

if **name** == "**main**":
main()

````


