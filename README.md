---
description: this is a multi-container web app using FLASK and redis build with MIGHTY docker-compose
title: very basic multi-container web app
---

# New Commit Instructions
 - This repo following the best practices for git commit as per what [__Linus would like__][Linus repo]  
 - There are two __Git global config options__ needs to be configured in order to maintain the __Git Commit__
 ```bash
  git config --list --show-orgin # this is to show the current configured options
  git config --global core.editor vim
  git config --global commit.template ~/.commit_template
  vim ~/.commit_template # to start typing your template
 ```
 - A good example for the commit body would be like this
 ```bash
 # If applied, this commit will...
# [Add/Fix/Remove/Update/Refactor/Document] [issue #id] [summary]


# Why is it necessary? (Bug fix, feature, improvements?)
-
# How does the change address the issue? 
-
# What side effects does this change have?
-
 ```
 - For more details please refer to [git commit practices your future self will thank you for][dev]
# Installation
* fork the project
```bash
git clone https://github.com/ahaffar/flask_redis.git
```
* install dcoker compose

 1-  ```sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose```

 2-  chmod +x /usr/local/bin/docker-compose


* run docker compose
```
docker-compose up
```

[Linus repo]: https://github.com/torvalds/subsurface-for-dirk/commit/b6590150d68df528efd40c889ba6eea476b39873
[dev]: https://victoria.dev/verbose/git-commit-practices-your-future-self-will-thank-you-for/