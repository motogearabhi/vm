git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"

git push origin refs/heads/*:refs/heads/* --force


git push origin refs/tags/*:refs/tags/* --force







for branch in $(git branch -r | grep -v HEAD); do
  b=${branch#origin/}
  git checkout -B "$b" "$branch"
  git push github "$b" --force
done
