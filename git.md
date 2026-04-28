git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"

git push origin refs/heads/*:refs/heads/* --force


git push origin refs/tags/*:refs/tags/* --force
