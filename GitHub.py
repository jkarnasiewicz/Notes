GitHub
Git(Distributed version control system/rozproszony system kontroli wersji)
##########################################################################################################

git init # Initialize a git repository
git clone # Clone existing one

git pull 				# is like git fetch + git merge
git status
git add ./file.py
git add '*.txt'
git add -A              # add new files and modified files to the index
                        # add also removed files
git rm file.py
git rm -r --cached file_name/dir_name 					# remove from git but not from disk
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

git config --global user.name "Name"
git config --global user.email email_address
git config --global color.ui true  # pretty command colors

gitg or gitk
git diff                           # differences
git log
git log gerrit/master              # commits that's already on server (origin/branch_name)
git log --pretty=oneline --all --graph      # commits tree
git log -10 --all --date-order				# last 10 commits with date order
git ... -i ...                     # more information with -i

git remote -v
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


git commit -m 'Add cute...'
git log
git remote add origin https://github.com/try-git/try_git.git
git push -u origin master # after that git push

git pull origin master
git diff HEAD # most recent changes
git diff --staged # changes recently added
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