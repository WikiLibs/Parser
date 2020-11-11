# Git cheatsheet

## Commit operations

### 1. Reset changes in file
```
git checkout -- file
```

### 2. Reset changes
**Options :**
* *mixed* (default): files are preserved but not marked for commit (need to git add)
* *soft*: unstages all modified files (but files are added)
* *hard*: removes all modifications

```
git reset --[option] HEAD~1
```

### 3. Ammend current commit
If you need to modify the last commit (that wasn't pushed), to change the message or add files:
```
git commit --amend  # add -m "message" to change the message
```

If you **modify a commit that is already pushed**, you'll face problems when you'll need to push again.
If that happens, contact someone who knows what to do, you might destroy the commit history (I'm looking at you --force).

### 4. Modify old commits
If you need to modify an older commit, prepare to do some git f\*ckery tricks, using *git rebase*.

**WARNING: be sure of what you are doing**

* To begin, you need to use *git log* to count how many commits you need to get back, write it somewhere
* Next, use the *git rebase* command. Here, we say that we want to get back the 4th older commit from HEAD, while allowing modifications:
```
git rebase -i HEAD~4
```
* Now, your prefered text editor should have been opened with all the commits selected at the top. Here, you should replace *'pick'* by one of the following options (if you don't, rebase will just run through all your commits without stopping)
    * *'edit'*: allows modifications at this commit
    * *'reword'*: allows to change only the commit message
    * *'squash'*: merge this commit with the previous one (might be useful you committed the same message twice in a row)
    * *'drop'*: remove commit
* When you've finished modify this, exit the text editor
* Now, git should've stopped at the first commit marked with *'edit'*
    * Modify what you need to modify
    * `git commit --ammend` (check the usage the 3.)
    * `git rebase --continue` (will resume rebasing and go through commits until a new *'edit'* is found)
* When the rebase is done, you might not be able to push (as the history of the branch has changed)

**If you can't push, you'll need to use push --force and it's a bad evil command. Please ask someone before doing this**


## Branch operations

### 1. Delete branch
```
git branch -D branch_name
```

### 2. Rename branch
* If already on the branch
```
git branch -m new_name
```
* If not on branch
```
git branch -m branch_to_rename new_name
```

## Conflicts

### 1. Merge conflict

If you have a conflict after a merge, follow these steps:
* Open VS Code
    * Go into the files that need attention
    * Solve the conflicts by either accepting, refusing or mixing incoming changes
* Add the modified files (*git add*)
* Commit the changes using the command bellow
* Push the changes
```
git add --all  # or add the files individualy
git commit  # without options, to keep the merge message
git push [remote] [branch]  # ex: git push origin master
```