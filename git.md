# Git and GitHub

## How do you remove the most recent commit pushed to remote repo and keep your local code intact?

```git
git push -f origin HEAD^:master
```