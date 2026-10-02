## 1. What is Git and Github ?
   Git is version control system, that keeps track of your code, maintains the log, and stores all the versions of your code locally. Github is a cloud service, where you upload your code, and can access it from anywhere, can collabarate with anyone.


## Useful Commands:
* git config --global user.email "you@example.com"
* git config --global user.name "Your Name"
* git --version => to check the version of git installed
* git status => shows the status of the curent repo(tells you what is happening NOW, like is it Tracked, Untracked, Modified)
* git log => shows the commit history(tells you what happened BEFORE)
* git rm --cached <filename> => unstage the file
* git log --oneline => list the commits in one line 
* .gitignore => used to store the impo things like apikeys, .env
* git switch <filename> => switch the head to specified filename
* git diff <commit1> <commit2> => shows the difference btw two commits


## Other useful commands
* cd filename => change directory 
* cd .. => jumps to previous directory
* pwd => print working directory
* ls -Force => just hidden and non-hidden files in the folders(ls => long listing)
* ni hello.txt => creates a new file


## Sequence of git commands
* git init => starts to track the repo and creates hidden folder called as .git(stores internal info and history)
* git add file => stages that particular file(note down my changes)
* git commit -m "message" => creates a commit with author id, message and other details of the commit, keep the -m in present/past tense
* 
