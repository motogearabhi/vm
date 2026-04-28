git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"

git push origin refs/heads/*:refs/heads/* --force


git push origin refs/tags/*:refs/tags/* --force







for branch in $(git branch -r | grep azure/ | grep -v HEAD | sed 's|azure/||'); do
  git checkout -B "$branch" "azure/$branch"
  git push origin "$branch"
done
