# 1. Prerequisites

## 1. Link repository to Azure

To link your repository the Azure remote, you need to follow these steps:
- Clone the repository (from github or azure)
- Add your ssh key (id_rsa.pub) to your azure account
- Add azure as a remote using this command
```
git remote add azure git@ssh.dev.azure.com:v3/WikiLibs/Parser/Parser
```

Now you should be able to do everything on the Azure repository

## 2. Prepare your working environment

To have a common norm, you should use Visual Studio Code, and setup it :
- Install flake8 as your Python linter
```
pip install flake8
```
- In VS Code, add the following settings (you can access it using ctrl+','):
```
"python.linting.pylintEnabled": false,
"python.linting.flake8Enabled": true,
"python.linting.flake8Path": "/usr/local/bin/flake8" (or whatever path)
```

# 2. Workflow

Here's a quick recap of your workflow.
Don't forget to check the **Pro Tips** section bellow.

## 1. Create a new issue/ticket in Azure DevOps

Before coding anything, you need to create a ticket on DevOps :
- Go to the Boards Boards section in DevOps
- Create a new item in the "To Do" column, and set the following fields
    - Name, summing up the work to do
    - Description, telling in the details what you are going to do
    - Priority, if applicable
    - Effort, corresponding in the charge of work (ex: 1 for a day of work)
    - Tags, to have a quick view of what's going on (check tags in the board parameters)
    - Assign people to the ticket


## 2. Create a new feature branch

When you are ready to start your ticket, move it into the "On feature branch" column in DevOps Boards. Then, you can create your new feature branch :
- Checkout master and pull to changes
```
git checkout master && git pull azure master
```
- Create a new branch corresponding to your ticket
```
git checkout -b feature/nbTicket-your-incredible-feature

# ex: feature/34-add-new-langage-to-parser
```

Now you can work on your feature.

## 3. Push your feature

When your feature is ready, your just push your branch using :
```
git push azure feature/nbTask-your-awesome-feature
```

## 4. Create a Pull Request

You feature branch is pushed, but you can't manually merge it to *dev* and *master*. To do this, you need to create a PR (Pull Request) for both *dev* and *master* :
- Go into Repos/Pull Requests in DevOps
- Create a new PR
    - Select *[your-branch]* into *[dev or master]*
    - Title : [NbTask] Ticket content *(ex: [34] Create documentation for DevOps)*
    - Label : *Dev* or *Master*
    - Description : describe your PR
    - Click on Create
- Be sure you created a PR for both dev and master
- When your PRs will be created, a reviewer will be assigned for revision. When the review is done, you will be able to merge your PR.

**IMPORTANT: at first, you must only merge with dev, even if both PR are validated. When it's merged with dev and you have checked that your feature is OK and EVERYONE told you it's OK, THEN you can merge with master**

# 3. Pro Tips

## 1. Commits

Do a lot of commits. Thanks to that, if something goes wrong, you'll be able to revert to an old commit easily.

Also, don't do mixed things into a single commit. For exemple, don't do both front and back into one commit.

## 2. Commit norm

Follow this commit norm :
```
[NbTicket] What has been done in the commit

# ex: [56] Added new unit tests
#     [56] Removed test.txt
#     [56] Added python extension handling to parsing
```

## 3. Misc

- Try to have a look at the Git cheatsheet in the repo documentation, you'll find some useful commands !
- If you have a doubt, ask someone.