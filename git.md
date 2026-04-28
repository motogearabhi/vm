git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"

git push origin refs/heads/*:refs/heads/* --force


git push origin refs/tags/*:refs/tags/* --force









git branch -r | grep azure/ | grep -v HEAD | while read branch; do b=${branch#azure/}; git checkout -B "$b" "$branch"; git push origin "$b"; done
