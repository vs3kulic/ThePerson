# Contributing to this project

## 👋 Hello!

Thanks for considering contributing to this open-source project! Both beginners 
and experts are very welcome here.

This project is purely for entertainment purposes, so do have fun and spill 
your creativity.

---

## 📝 Table of Contents

- [Contributions You Can Make](#-contributions-you-can-make)
- [Pull Request Steps](#-pull-request-steps)
- [Task Issues](#-task-issues)
- [Making Your First Contribution](#-making-your-first-contribution)
- [Code Guidelines](#-code-guidelines)
- [Reporting a Bug](#-reporting-a-bug)
- [Suggesting a Feature](#-suggesting-a-feature)

---

## ✨ Contributions You Can Make

There are many ways you can contribute: Adding a feature, fixing code, 
finding and reporting bugs, improving documentation, and more!

Any addition to the project will be very much appreciated, even small ones.

## 👣 Pull Request Steps

1. Create a fork of [the repository][repo]
2. Clone the forked repository to your local machine
3. Create a new branch with a meaningful name (include the type of change 
   followed by a slash; hierarchical branch naming)

   | Prefix       | Description                                    |
   |--------------|------------------------------------------------|
   | `bugfix`     | Bug fix (minor, not urgent)                    |
   | `hotfix`     | Urgent, critical fix                           |
   | `feature`    | New feature/functionality                      |
   | `docs`       | Documentation only                             |
   | `format`     | Formatting fixes                               |
   | `refact`     | Code improvements that do not affect behaviour |
   | `wip`        | Work in progress                               |
   | `experiment` | Temporary, experimental code                   |
   | `mix`        | A combination of different fixes/changes       |
   | `misc`       | Other (not recommended)                        |

   - e.g.) `feature/feature-name`, `fix/issue-12`
   
4. Make and commit your changes
5. Push commits to GitHub (if you have made changes locally on your machine)
6. Create a pull request and await review

We will likely need to discuss the changes you make and apply some tweaks 
and polishes before approval.

You should receive a notification/email once your changes have been merged 
onto the main branch of this project.

## 📋 Task Issues

Some issues will be opened in the [Issues tab][repo-issues] on GitHub, labeled 
`task`. 

If you are interested in completing a task: 
- **Leave a comment requesting assignment under the issue**
- Wait for a thumbs-up from a maintainer
- Follow the steps above to create a fork and PR with your changes
- Start coding!

When writing the pull request:
- Start the title the PR with `TASK: `.
- In your PR description, **ensure you specify the issue number at the bottom**

```markdown
# TASK: Title of task (#123)

This is a description of the task completed. 
Blah blah blah.

Closes #123
```

Where `#123` is the issue number.

Other issue-closing keywords you can use:
* close
* closes
* closed
* fix
* fixes
* fixed
* resolve
* resolves
* resolved

## 🧰 Making Your First Contribution

If you're new here or are not familiar with contributing to repositories on 
GitHub, [here's a repo][first-contribs] with information that might help.

## 🧭 Code Guidelines

Here are **3 rules** I have with writing (Python) code:

> 1. Try to follow PEP 8 as much as possible

Unfortunately I am the type of person who likes beautiful, formatted code.
**However, it is completely fine if you are unfamiliar with PEP 8 or styling 
guidelines**.

Key things to keep in mind include:
- **Line lengths** (try to keep line **below 80 characters**; PEP 8 says 79 but 
  whichever works)
- **Naming conventions** (module, variable, class, and function names)
  - `variable_must_be_named_like_this`
  - `functions_too`
  - `also_modules`
  - `ClassesMustBeNamedLikeThis`
- **Docstring and comments formatting**
- **Line separations** (2 blank lines around classes and functions, etc.)
- **Order of import statements** (standard → third-party → local)

Take a look at existing code on the repo to get an idea of the code style.

===============================================

> 2. The Zen of Python

Lo, the Bible of Python:

```python
import this
```
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

===============================================

> 3. Don't be boring

Give your code some _personality_. Avoid dull, flavorless code. You can even 
add a little joke comment if your code starts to look sleep-inducing.

---

## 🐛 Reporting a Bug

To report a bug or issue:
1. On the repository on GitHub, go to the [Issues][repo-issues] tab.
2. Select "New issue"
3. This is a tiny project, and I don't really have rules on how you should 
   write an issue report. Just include a descriptive title and helpful 
information in the description.
4. Submit the issue.

---

## ☝️ Suggesting a Feature

If you do not wish to code any features yourself, feel free to either open 
an issue as described above, mentioning and explaining the new feature you 
would like to see, or add a comment under a [discussion][repo-disc].

[repo]: https://github.com/TheGittyPerson/ThePerson
[repo-issues]: https://github.com/TheGittyPerson/ThePerson/issues
[repo-disc]: https://github.com/TheGittyPerson/ThePerson/discussions
[first-contribs]: https://github.com/firstcontributions/first-contributions
