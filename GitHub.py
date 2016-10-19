Git (Distributed version control system/rozproszony system kontroli wersji)
Three-tree architecture (working -> staging index -> repository)
##########################################################################################################

git --version
git init 				# Initialize a git repository
git clone 				# Clone existing one

git pull 				# is like git fetch + git merge
git status
git add ./file.py
git add '*.txt'
git add -A              # add new files and modified files to the index
                        # add also removed files
git rm file.py 			# remove from git and from disk (then use commit)
git rm -r --cached file_name/dir_name 	# remove from git but not from disk
git commit -m "message"

# Jeśli są zmiany w masterze wprowadzone przez kogoś innego
git fetch origin
# Jeśli pojawi się informacja: "Your branch and origin/master have diverged"
git rebase origin/master
# i po edycji zmian w plikach
git add .
git rebase --continue
git push


# Branch
git branch 						   # list of branches
git branch -a 					   # show exactly what’s going on with all your branches - local and remote
git branch branch_name 			   # new branch
git checkout master 		   	   # change to master
git checkout -b branch_name		   # create and change to new branch

git branch -d branch_name 		   # delete branch_name
git branch -D branch_name 		   # force delete

git branch -m branch_new_name      # branch rename

# Stash changes from master, and add them to new branch
git stash
git checkout -b branch_name
git stash pop


# Commit
git reset HEAD file_name 		   # removing file from commit

# Back to commit
git checkout commit_id .


# Squashing commits with rebase
git rebase -i HEAD~4               # 4 - number of last commits to squash
# pick or squash commits
# then comment unnecessary comments and id's and put one message
# or
git reset --soft "HEAD^"           # probably have to change commit Id or remove it
git commit --amend


# Informations and settings
git help
git help config

git congig --system 				# configuration for all users in system
git config --global 				# configuration per user
git config 							# configuration per project
git config --list

git config --global user.name "Name"
git config --global user.email email_address
git config --global color.ui true  # pretty command colors
git config --global core.editor "app_name -wl1"

git log
git log -n 5					   			# last 5 commits
git log --since=2016-06-15
git log --until=2016-10-17
git log --author="Joe"
git log --grep="fixes bug" 		   			# search the commit messages

git log gerrit/master              			# commits that's already on server (origin/branch_name)
git log --pretty=oneline --all --graph      # commits tree
git log -10 --all --date-order				# last 10 commits with date order
git ... -i ...                     			# more information with -i

gitg or gitk
git diff                           			# differences

git remote -v 								# more information
git remote set-url gerrit ssh://jacek.karnasiewicz@spinlab-pg.wcss.pl:2222/SpinLabBibliography.git
git remote set-url origin ssh://jacek.karnasiewicz@spinlab-pg.wcss.pl:2222/SpinLabUtilities.git


# Changing status of the file
git update-index --assume-unchanged <file>
git update-index --no-assume-unchanged <file>


# Update module (odpowiedni katalog)
git fetch origin
git rebase origin/master
pip install . --upgrade
pip install Directory/ --upgrade --no-dependencies


pip install -r file
pip install -r requirements.pip	   # requirement file
pip install -e path_to_source
pip freeze > requirements.txt
pip freeze | grep django



Gerrit
##########################################################################################################

git status
git add /files.py
git commit --amend                 # bez --amend jeśli to nasz pierwszy commit
git review                         # or git review branch_name

# jesli nie bylo wczesniejszych commit-ow to:
# sciagamy hooka
scp -p -P 2222 jacek.karnasiewicz@spinlab-pg.wcss.pl:hooks/commit-msg .git/hooks/
git commit
git push origin HEAD:refs/for/master
# wrazie problemow z Id
git commit --amend                 # i wklejamy changed-Id do zakomentowanych lini




Gerrit and Nereid
##########################################################################################################

git clone git+ssh://karnasiewicz@nereid.wcss.wroc.pl/var/lib/prjs/SpinLab/SpinLabReports.git
git clone git+ssh://jacek.karnasiewicz@spinlab-pg.wcss.pl:2222/SpinLabCore.git
# Clone only one of the branches
git clone git+ssh://jacek.karnasiewicz@spinlab-pg.wcss.pl:2222/Polymers.git -b disk --single-branch

# Tworzymy repozytorium z danego brancha
1) git clone git+ssh://jakub.kunicki@spinlab-pg.wcss.pl:2222/LKE.git
2) git checkout -b IEL origin/IEL
# ??
git clone -b my-branch https://git@github.com/username/myproject.git



# ?!
# git cherypick?!
# git hunk
# merged commits
# nie kompresuje commita --no --thin

# git reset hard head~1 - unwanted commits

mkdir name


git commit -m 'Fixes bug in ...'
git log
git remote add origin https://github.com/try-git/try_git.git
git push -u origin master # after that git push

git pull origin master
git diff HEAD # most recent changes
git diff --staged -M # wykryj operacje przeniesienia
git reset file_name # unstage file
git checkout -- file_name #  get rid of all the changes since the last commit for file_name

git branch clean_up # new branch
git checkout clean_up # switch to other branch
git rm '*.txt' # remove the actual files from disk, and also stage the removal of the files for us
git commit -m 'Remove all'
git checkout master
git merge clean_up # merge your changes from the clean_up branch into the master branch
git branch -d clean_up
git push
git push remotename branch_name








# New branch from branch on server
# (commitujemy zmiany, przechodzimy na orginalnego brancha lokalnego, robimy pulla, pozniej merge z branchem lokalnym i push na serwer)
git fetch origin
git rebase origin branch_name	# still local

git add . / git commit

git checkout origin_branch_name
git pull
git merge actual_branch_name
git push origin branch_name 		# on server


git blame


# Remove file and its history
git clone https://...
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch YOUR-FILE-WITH-SENSITIVE-DATA' --prune-empty --tag-name-filter cat -- --all
echo "YOUR-FILE-WITH-SENSITIVE-DATA" >> .gitignore
git add .gitignore
git commit -m "Add YOUR-FILE-WITH-SENSITIVE-DATA to .gitignore"
git push origin --force --all
git push origin --force --tags

# Force all objects in your local repository to be dereferenced and garbage collected with the following commands
git for-each-ref --format='delete %(refname)' refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now

# Show history of the file
gitg path/to/file

# update (checkout) a single file from remote origin master
git checkout origin/master -- path/to/file

echo '__pycache__' >> .gitignore
echo '*.pyc' >> .gitignore

# Różnica między kodem lokalnym a repozytorium
git diff --staged

git commit -am 'pierwszy test jednostkowy'

git diff --staged -M 					# wykryj operacje przeniesienia



git reset --hard HEAD 					# undo all changes




# Back to taged commit
...
git commit -m ''
git tag revisit_this_point
...
git checkout -b more-isolation
git reset --hard revisit_this_point



# Tag
git tag -f LIVE
export TAG='date +DEPLOYED-%F/%H%M'
git tag $TAG
git push -f origin LIVE $TAG

# TDD 362





# Git essencial training

# HEAD
pointer to 'tip' of current branch in repository
last state of repository, what was last checked out

# STATUS
report the difference between our working directory, the staging index,
and the repository

# DIFF
# comparing whats in the repository, the version that HEAD is pointing at(-),
# versus whats in our working directory(+)
git diff

git diff --color-words file_name 		# color changes

# comparing whats in the repository, versus whats in our staging index
git diff --staged				# the same as git diff --cached

# RENAME/MOVE
git mv file_name new_file_name

# UNDOING CHANGES IN WORKING DIRECTORY
git checkout -- file_name # stay on the same branch and get this file from repository

# UNDOING CHANGES IN STAGING INDEX (changes back to working directory)
git reset HEAD file_name # look at last commit and reset yourself to that

# UNDOING COMMITS CHANGES(ONLY LAST COMMIT CAN BE CHANGE)
git commit --amend -m "New message" # SHA(commit id) changes

# RETRIVING OLD VERSION OF THE FILE
git checkout commit_id -- old_version_of_the_file_name

# UNDOING CHANGES FROM OLD COMMITS
git revert commit_id

# UNDO MULTIPLE COMMITS
git reset [option] commit_id
	# does not change staging index or working directory
	# any changes that came after that commit are in staging index
	--soft
	# changes staging index to match repository
	# does not change working directory
	# any changes that came after that commit are in working directory
	--mixed (default)
	# changes staging index and working directory to match repository
	# !that means any changes that came after that commit are completely obliterated
	--hard

# THROW AWAY THE UNTRACKED FILES
git clean -n   # show info
git clean -f   # force remove
git clean -fd  # remove any untracked files and directories

# IGNORING FILES (.gitignore)
# global ignoring files (user level ignoring - not in repository level)
git config --global core.excludesfile ~/.gitignore_global

# remove from git and from disk (then use commit)
git rm file.py
# remove this file just from staging index, not from repository
# stop tracking changes
git rm --cached file_name

# TRACKING EMPTY DIRECTORY (git doesnt track empty directory)
# put empty file in it, e.g. .gitkeep

# REFERENCING COMMITS
# HEAD~x going from the HEAD and moving back 'x' commits
# parent commit
HEAD~1
# grandparent commit
HEAD~2

# TREE LISTING
git ls-tree HEAD/master catalog_name/

# LOG
git log --since="2 weeks ago" --until="3 days ago"
# what has happened to the file_name file from commit_id to the last one
# -p option is for detail info
git log -p commit_id.. file_name

# statistics about what changed in each commit
git log --stat --summary

git log --oneline --graph --all --decorate

# viewing commits
git show commit_id

# COMPARING COMMITS
# differences between the directory at commit_id and my current working directory
git diff commit_id

# what has changed from commit_id to now in the file_name file
git diff commit_id file_name

# the snapshot at commit_id_1 versus the snapshot at commit_id_2
git diff commit_id_1..commit_id_2 file_name
git diff --stat --summary -w commit_id..HEAD

# BRANCH
# comparing branches
git diff --color-words master..branch_name

# show whether one branch completely contains another branch or not
# show all branches that are completely included in this branch
git branch --merged

# renaming branches
git branch -m branch_name branch_new_name


# MERGING
# merging from branch which is receiver
git merge branch_name

# fast-forward commits don't create new commit
# forces git to create a merge commit anyway)
git merge --no-ff branch_name

# do a merge only if you can do fast-forward
git merge --ff-only branch_name

# resolving merge conflicts
# abort the merge
git merge --abort
# or
# resolving merge conflicts
git add .
git commit

# STASH
git stash list
git stash show -p stash@{0}
git stash save "message"

# retriving stashed changes
git stash pop 					# removes from stash
git stash apply stash@{3} 		# leaves a copy in stash

# deleting stashed changes
git stash drop stash@{2}

# deleting all stashed changes
git stash clear

# REMOTES
# list of the remote server
git remote

# add remote server
git remote add remote_alias url

# create a new remote called origin that points to remote server at url
git remote add origin https://...

# remove remote
git remote rm <alias>

# first push to remote repository
# e.g origin master
git push -u <remote_alias> <branch_name>
# -u track remote branch, it is tthe same as:
git branch --set-upstream <branch_name> <remote_alias>/<branch_name>

# remote branches
git branch -r

# remote and local branches
git branch -a

# cloning repository
git clone <url.git> <folder_name>						# -b <branch_name>

# normal pushes
git push <remote_alias> <branch_name>

# info
git diff origin/master..master
git log --oneline origin/master

# FETCH
# synchronize origin/master with remote repository
git fetch <remote_alias>								# e.g git fetch origin

# PULL
# git pull = git fetch + git merge

# create branch from remote branch
git branch <branch_name> <remote_alias>/<branch_name>
git checkout -b <branch_name> <remote_alias>/<branch_name>

# deleting remote branch
git push <remote_alias> --delete <branch_name>

# creating alias
# git logg
git config --global alias.logg "log --graph --decorate --oneline --abbrev-commit --all"
