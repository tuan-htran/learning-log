# Practicing Git branching workflow
# Day 3: Git Workflow Practice - Branches, Commits, Merging
#
# Steps I practiced:
# 1. Created a new branch: git checkout -b practice-branch
# 2. Made this file and committed it ON the branch:
#    git add .
#    git commit -m "Test commit on practice-branch"
# 3. Switched back to main: git checkout main
#    -> this file did NOT show up here, since the commit only existed
#       on practice-branch, not on main yet
# 4. Merged the branch into main: git merge practice-branch
#    -> after merging, the file appeared in main
# 5. Pushed to GitHub: git push
# 6. Deleted the now-merged branch: git branch -d practice-branch
#
# Key takeaway: a branch lets you make changes in isolation, without
# affecting main, until you're ready to merge them in. In a team setting,
# this is usually done through a pull request, so others can review the
# changes before they're merged into main.

print("Hello from a branch!")