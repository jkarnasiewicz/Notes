Git (Distributed version control system/rozproszony system kontroli wersji)
Three-tree architecture (working -> staging index -> repository)

# Systemy kontroli wersji:
# niebezpiecznie jest przechowywac duze zmiany lokalnie bez jakiejkolwiek kopii zapasowej w postaci
# zmian zatwierdzonych w centralnym repozytorium
# czeste zatwierdzanie lokalnych zmian bez wzgledu na to, czy aplikacja dziala poprawnie, czy nie,
# wprowadza niestabilnosc do repozytorium i utrudnia prace wszystkim czlonka projektu
1. scentralizowny (SVN, CVS)
	tworzenie galezi oraz ich scalanie jest z reguly trudne w obsludze, w niektorych systemach
	moze byc prawdziwym koszmarem
	poniewaz system jest scentralizowany, wprowadznie zmian nie jest mozliwe w przypadku braku
	polaczenia z serwerem repozytorium(np. w firmowej sieci) co zmusza do zatwierdzania zmian hurtowo
	taki kontrole wersji nie sprawdzaja sie dobrze w przypadku gdy wiele firm na stale utrzymuje swoje
	niezalezne galezie kodu zrodlowego
2. rozproszony (GIT)
	kazdy uzytkownik posiada swoje wlasne pelnoprawne i niezalezne repozytorium kodu projektu
	mozliwosc dokonywania dwustronnej synchronizacji pomiedzy swoim a pozostalymi repozytoriami

# Metodyki
1. Git Flow
2. GitHub Flow

##########################################################################################################

# GENERAL INFORMATION
git --version
git help config
git blame

# status
# report the difference between our working directory, the staging index,
# and the repository
git status

# HEAD
# pointer to 'tip' of current branch in repository
# last state of repository, what was last checked out

# referencing commits
# HEAD~x going from the HEAD and moving back 'x' commits
# parent commit
HEAD~1										# HEAD^
# grandparent commit
HEAD~2 										# HEAD^^

# tracking empty directory (git doesnt track empty directory)
# put empty file in it, e.g. .gitkeep

# tree listing
git ls-tree HEAD/master catalog_name/



# CONFIG
git config --system 						# configuration for all users in system
git config --global 						# configuration per user
git config 									# configuration per project
git config --list

git config --global user.name "Name"
git config --global user.email email_address
git config --global color.ui true  # pretty command colors
git config --global core.editor "app_name -wl1"

# creating alias
# git logg
git config --global alias.logg "log --graph --decorate --oneline --abbrev-commit --all"

# ignoring files (.gitignore)
# echo '__pycache__' >> .gitignore
# echo '*.pyc' >> .gitignore
# global ignoring files (user level ignoring - not in repository level)
git config --global core.excludesfile ~/.gitignore_global



# REMOTES
# list of the remote server
git remote

# more information
git remote -v

# add remote server
git remote add remote_alias url

# create a new remote called origin that points to remote server at url
git remote add origin https://...

# update
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git 			# SSH remote URLs
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git 		# HTTPS remote URLs

# remove remote
git remote rm <alias>

# first push to remote repository
# e.g origin master
git push -u <remote_alias> <branch_name>
# -u track remote branch, it is the same as:
git branch --set-upstream <branch_name> <remote_alias>/<branch_name>

# set-url
git remote set-url origin ssh://jacek.karnasiewicz@spinlab-pg.wcss.pl:2222/SpinLabUtilities.git

# normal pushes
git push <remote_alias> <branch_name>



# LOG
git log

# what has happened to the file_name file from commit_id to the last one
# -p option is for detail info
git log -p commit_id.. file_name

git ... -i ...                     			# more information with -i
git log -n 5					   			# last 5 commits
git log --since=2016-06-15
git log --until=2016-10-17
git log --since="2 weeks ago" --until="3 days ago"
git log --author="Joe"
git log --grep="fixes bug" 		   			# search the commit messages

git log gerrit/master
git log --pretty=oneline --all --graph      # commits tree
git log -10 --all --date-order				# last 10 commits with date order

# statistics about what changed in each commit
git log --stat --summary

git log --oneline --graph --all --decorate



# SHOW
# viewing commits detail
git show commit_id



# DIFF (COMPARING COMMITS)
# comparing whats in the repository, the version that HEAD is pointing at(-),
# versus whats in our working directory(+)
git diff

git diff --color-words file_name 			# color changes

# comparing whats in the repository, versus whats in our staging index
git diff --staged							# the same as git diff --cached

# differences between commit_id and my current working directory
git diff commit_id

# what has changed from commit_id to now in the file_name file
git diff commit_id file_name

# the snapshot at commit_id_1 versus the snapshot at commit_id_2
git diff commit_id_1..commit_id_2 file_name
git diff --stat --summary -w commit_id..HEAD



# INIT/CLONE
git init catalog_name						# Initialize a git repository, or git init .

# cloning repository
git clone <url.git> <folder_name>			# -b <branch_name>



# ADD
git add ./file_name.py
git add '*.txt'

# add new files and modified files to the index add also removed files
git add -A




# RENAME/MOVE
git mv file_name new_file_name



# REMOVE
# remove from git and from disk (then use commit)
git rm file.py
# remove this file just from staging index, not from repository
# stop tracking changes
git rm --cached file_name



# THROW AWAY THE UNTRACKED FILES
git clean -n   								# show info
git clean -f   								# force remove
git clean -fd  								# remove any untracked files and directories



# BRANCH
git branch 						   # list of branches
git branch -r 					   # show only remote branches
git branch -a 					   # show remote and local branches
git branch branch_name 			   # new branch
git checkout branch_name 		   # change to branch_name
git checkout -b branch_name		   # create and change to new branch

git branch -d branch_name 		   # delete branch_name
git branch -D branch_name 		   # force delete

git branch -m branch_new_name      # branch rename

# comparing branches
git diff --color-words master..branch_name

# show whether one branch completely contains another branch or not
# show all branches that are completely included in this branch
git branch --merged

# renaming branches
git branch -m branch_name branch_new_name

# create branch from remote branch
git branch <branch_name> <remote_alias>/<branch_name>
git checkout -b <branch_name> <remote_alias>/<branch_name>

# deleting remote branch
git push <remote_alias> --delete <branch_name>



# STASH
# stash list
git stash list

# stashing
git stash
git stash save "message"

# details
git stash show -p stash@{0}

# retriving stashed changes
git stash pop 								# removes from stash
git stash apply stash@{3} 					# leaves a copy in stash

# deleting stashed changes
git stash drop stash@{2}

# deleting all stashed changes
git stash clear

# Stash changes, and add them to new branch
git stash
git checkout -b branch_name
git stash pop



# FETCH
# synchronize <remote_alias>/master with remote repository		# e.g. origin/master
git fetch <remote_alias>										# e.g git fetch origin



# PULL
# git pull = git fetch + git merge



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



# REBASE
# Jeśli są zmiany w masterze wprowadzone przez kogoś innego
git fetch origin
# Jeśli pojawi się informacja: "Your branch and origin/master have diverged"
git rebase origin/master
# i po edycji zmian w plikach
git add .
git rebase --continue
git push



# SQUASHING COMMITS
# Squashing commits with rebase
git rebase -i HEAD~4               # 4 - number of last commits to squash
# pick or squash commits
# then comment unnecessary comments and id's and put one message
# or
git reset --soft "HEAD^"           # probably have to change commit Id or remove it
git commit --amend



# UNDOING CHANGES WITH CHECKOUT, RESET, COMMIT AND REVERT
# undoing changes in working directory
git checkout -- file_name 					# stay on the same branch and get this file from repository

# undoing changes in staging index (changes back to working directory)
git reset HEAD file_name 					# look at last commit and reset yourself to that

# undoing commits changes (ONLY LAST COMMIT CAN BE CHANGE)
git commit --amend -m "New message" 		# SHA(commit id) changes

# retriving old version of the file
git checkout commit_id -- old_version_of_the_file_name

# undoing changes from old commits
git revert commit_id

# undoing multiple commits
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



# UPDATE-INDEX
# Changing status of the file
git update-index --assume-unchanged <file>
git update-index --no-assume-unchanged <file>



# CHERYPICK
# Apply the change introduced by the commit at the tip of the master branch
# and create a new commit with this change.
git cherry-pick master

# Apply the changes introduced by all commits that are ancestors of
# master but not of HEAD to produce new commits
git cherry-pick ..master

# Apply the changes introduced by the fifth and third last commits
# pointed to by master and create 2 new commits with these changes
git cherry-pick master~4 master~2



# Tag
# export TAG='date +DEPLOYED-%F/%H%M'
# git tag $TAG
...
git commit -m ''
git tag revisit_this_point
...
git checkout -b more-isolation
# Back to taged commit
git reset --hard revisit_this_point



# APPLICATIONS
# gitg or gitk
# Show history of the file
gitg path/to/file





# EXAMPLES
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



# gerrit
git status
git add /files.py
git commit --amend                 			# bez --amend jeśli to nasz pierwszy commit
git review                         			# or git review branch_name

# jesli nie bylo wczesniejszych commit-ow to:
# sciagamy hooka
scp -p -P 2222 jacek.karnasiewicz@spinlab-pg.wcss.pl:hooks/commit-msg .git/hooks/
git commit
git push origin HEAD:refs/for/master
# wrazie problemow z Id
git commit --amend                 			# i wklejamy changed-Id do zakomentowanych lini



# gerrit and nereid
git clone git+ssh://karnasiewicz@nereid.wcss.wroc.pl/var/lib/prjs/SpinLab/SpinLabReports.git
git clone git+ssh://jacek.karnasiewicz@spinlab-pg.wcss.pl:2222/SpinLabCore.git
# Clone only one of the branches
git clone git+ssh://jacek.karnasiewicz@spinlab-pg.wcss.pl:2222/Polymers.git -b disk --single-branch

# Tworzymy repozytorium z danego brancha
1) git clone git+ssh://jakub.kunicki@spinlab-pg.wcss.pl:2222/LKE.git
2) git checkout -b IEL origin/IEL
