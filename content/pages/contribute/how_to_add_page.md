Title: How to add a page to the Wiki
Date: 01-01-20 16:40
Template: wiki_leaf_page

---

### Make sure you have followed the instructions [here](/contribute/how_to_setup_dev_env/){:target="_blank"}  on setting up your development environment

---

<br>
<br>

# Things to note:

<br>

### Page location

All of the pages need to be placed under `content/pages/`

<br>
### Page format

All of the pages should use the following Markdown format:

```yaml
Title: <NAME OF YOUR PAGE example: Python snippet for finding ...>
Date: <DATE example: 01-01-20 16:40> 
Template: <PAGE template type : wiki_branch_page OR wiki_leaf_page >

THE CONTENT OF THE PAGE...
```

<br>
### Page template types

*wiki_branch_page* - a page that contains a list of links to the child pages (example: [techartorg.github.io/contribute](techartorg.github.io/contribute){:target="_blank"} )

*wiki_leaf_page* - a page that contains information (example: this page)

<br>
<br>
----

# Steps to adding a page


<br>

### 1) Select a category for your page 

Select one of the existing categories to place your page under.

Categories:

- blender
- coding
- contribute
- houdini
- math
- max
- maya
- pipelines
- python3
- rigging
- shaders
- tips
- tools
- unity
- unreal
- vfx

---
<br>
<br>

### 2.1) Create a subcategory Markdown file and Folder `(optional)`

<br>

If you need to create a `subcategory` under the `category` you have selected, create a new Markdown file and a folder with the same name.

Here is an example of creating a `python-tips` subcategory under the `python` category folder

```text
└── content/pages/
    ├── python.md            #  python category Markdown file
    └── python/              #  python category folder
        ├── python-tips.md   #  {NEW} python-tips subcategory Markdown file
        └── python-tips/     #  {NEW} python-tips subcategory folder
```

The Markdown file:

- should have the `Template` metadata set to `wiki_branch_page`
- the body of the file should be empty

```yaml
Title: <NAME OF YOUR PAGE example: Python snippet for finding ...>
Date: <DATE example: 01-01-20 16:40> 
Template: wiki_branch_page

```

---
<br>
<br>

### 2.2) Create the Markdown file

Under the `subcategory` folder create your new Markdown file.

Example:

```text
└── content/pages/
    ├── python.md                 #  python category Markdown file
    └── python/                   #  python category folder
        ├── python-tips.md        #  python-tips subcategory Markdown file
        └── python-tips/          #  python-tips subcategory folder
            └── my-python-tip.md  #  {NEW} python tip Markdown file
```

Here we create a `my-python-tip.md` file under `content/pages/python/python-tips/`.


The Markdown file:

- should have the `Template` metadata set to to `wiki_leaf_page`
- the body of the file should be contain the information you want to share

```yaml
Title: <NAME OF YOUR PAGE example: Python snippet for finding ...>
Date: <DATE example: 01-01-20 16:40> 
Template: wiki_leaf_page

```

---

<br>
<br>

### 3) Test your change

- Test your changes by running the local server
    - Run server
        - on macOS/Linux run: `make devserver`
        - om Windows run: `start peldev.bat && start pelserv.bat`
    - Go to http://localhost:8000/

---

<br>
<br>

### 4) Create a Pull Request

- Go to the [Pull Request page for the TAO wiki](https://github.com/techartorg/techartorg.github.io/pulls){:target="_blank"}
- Create a New Pull Request based on your fork of the Wiki