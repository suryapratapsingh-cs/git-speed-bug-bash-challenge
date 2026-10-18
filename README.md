# 🚀 Git Speed Round & Bug Bash Challenge

[![Auto-Grader Status](https://github.com/suryapratapsingh-cs/git-speed-bug-bash-challenge/actions/workflows/python-test.yml/badge.svg)](https://github.com/suryapratapsingh-cs/git-speed-bug-bash-challenge/actions/workflows/python-test.yml)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Git](https://img.shields.io/badge/Git-Ready-F05032.svg)

> **"Code breaks. Bugs hide. Legends fix."**
> 
> Welcome to the ultimate Bug Bash challenge. Your mission is to clone this repository, hunt down the logic flaws, and restore the codebase to a 100% passing state. Speed, accuracy, and clean Git history are your weapons.

---

## 🎯 The Mission
The core application (`app.py`) is failing its automated test suite. We have intentionally injected logical bugs, typos, and edge-case failures. Your job is to debug it.

## 🛠️ Phase 1: Local Setup & Intel

Fire up your terminal and execute the following commands to get your local environment ready:

```bash
# 1. Clone the repository
git clone [https://github.com/suryapratapsingh-cs/git-speed-bug-bash-challenge.git](https://github.com/suryapratapsingh-cs/git-speed-bug-bash-challenge.git)

# 2. Navigate to the project directory
cd git-speed-bug-bash-challenge

# 3. Run the initial test suite (Watch it fail)
python -m unittest discover -s . -p "test_*.py"
```
⚔️ Phase 2: Rules of Engagement   To conquer this challenge and secure your points, you must strictly follow industry-standard Git workflows:   
1. Isolate Your Work   Never work directly on the main branch. Create a dedicated feature branch for your team. 
```bash
git checkout -b fix-<your-team-name>
```
2. Hunt & Patch   Analyze app.py. Find the deliberate flaws and patch them until running the tests locally yields absolute success:
```bash
python -m unittest discover -s . -p "test_*.py"
# Goal: OK (Passed all tests)
```
3. Professional Commits   Commit your fixes with precise, professional messages.
```bash
git commit -m "fix: resolved logical error in check_access function"
```
(Warning: Vague messages like git commit -m "fixed" or git push --force will incur severe penalty points).
4. Deploy & Report (Pull Request)   Push your branch to GitHub and open a Pull Request (PR) against the main branch.
```bash
git push origin fix-<your-team-name>
```
⚖️ Automated Evaluation (Live Scoreboard)
Once your PR is open, our CI/CD pipeline (GitHub Actions) will instantly execute the tests against your code.

🟢 Green Check: All bugs neutralized. Maximum points awarded!

🔴 Red Cross: Tests failed. Return to your editor, find the missed bug, and push again.

Good luck, developers. May the fastest and cleanest code win. 💻🔥
