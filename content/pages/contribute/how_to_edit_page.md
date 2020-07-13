Title: How to edit a wiki page
Date: 01-01-20 16:40
Template: wiki_leaf_page

---

### Make sure you have followed the instructions [here](/contribute/how_to_setup_dev_env/){:target="_blank"}  on setting up your development environment

---
<br>
<br>

# Steps to editing a page

---
<br>
<br>

### 1) Find the page

In your web browser navigate to the page you want to make edits to.

Example:
[http://techartorg.github.io/python3/python3-snippets/latest_installed_program](http://techartorg.github.io/python3/python3-snippets/latest_installed_program){:target="_blank"}

At the top right of the page you will find a `Edit on GitHub` link.

Click that link!

This link will take you to the GitHub page for the corresponding Markdown file.

Example:
[https://github.com/techartorg/techartorg.github.io/edit/master/content/pages/python3/python3-snippets/latest_installed_program.md](https://github.com/techartorg/techartorg.github.io/edit/master/content/pages/python3/python3-snippets/latest_installed_program.md){:target="_blank"}

At the top of the page you will see the full path to the file you want to edit.

Example:
`content/pages/python3/python3-snippets/latest_installed_program.md`

---
<br>
<br>

### 2) Make the edits

- Open the file in your favorite Text Editor
- Make the changes you wanted
- Test your changes by running the local server
    - Run server
        - on macOS/Linux run: `make devserver`
        - om Windows run: `start peldev.bat && start pelserv.bat`
    - Go to http://localhost:8000/

---

<br>
<br>

### 3) Create a Pull Request

- Commit & Push
- Go to the [Pull Request page for the TAO wiki](https://github.com/techartorg/techartorg.github.io/pulls){:target="_blank"}
- Create a New Pull Request based on your fork of the Wiki

