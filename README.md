# Recipe site

## Milestone Project 3

## Table of contents

## UX

## User Stories
### Target Audience

#### As a first time user of the site I want to be able to:

- Understand what the site is for and how to navigate the site.
- Register for an account.

#### Returning Visitor Goals

As a returning registered user of the site I want to be able to:

- Log in to my account.
- Apply for opportunities.

#### Admin User

As an administrator for the site I want to be able to:

- Log in to my account.
- Create, edit, delete and view.

#### User Journey

### All user goals

### Returning user goals

### Future Development


## Features

## Wireframes

## Functionality

### Future Implementations

### Accessibility

## Database Schema

## Technology

### Languages Used
HTML, CSS, JavaScript, Python

### Database Used


### Frameworks Used


### Libraries & Packages Used

[Flask](https://flask.palletsprojects.com/en/2.2.x/)

[Jinja](https://jinja.palletsprojects.com/en/3.1.x/)


### Programs Used

[Heroku](https://id.heroku.com/login) for deployment

[Git](https://gitpod.io/) - For version control.

[GitHub](https://github.com/) - To save and store the files for this project.

[Pip](https://pip.pypa.io/en/stable/index.html) - A tool for installing Python packages.


## Testing

### User Stories



#### HTML Validation


#### CSS Validation


#### JavaScript Validator


#### Lighthouse


#### CI Python Linter

[CI Python Linter](https://pep8ci.herokuapp.com/)

![Python](/static/images/readmd-images/ci_pythonlinter.jpg)

### Defensive Programming

I have used defensive programming through my app to ensure that users who are not logged in, or users who did not create the opportunities or categories are unable to edit. This is achieved by checking whether there is a user in session, and then also checking to see if the session user is the same user who created the opportunity. Had I more time I would have liked to have developed a custom 404 pages that would direct users back to the home page, should any errors occur whilst they are using the app.

I have made use of modals to provide helpful warnings to the admin if records are to be deleted, double check that the admin definately wanted to do this.

## Deployment

The site was deployed to Heroku. Please follow the below steps.
Deployment steps

- add the list of requirements by writing in the terminal "pip3 freeze > requirements.txt"
- Add six and colorama==0.4.4 as they didn't seem to add automatically
- Git add and git commit the changes made
- Log into Heroku or create a new account and log in
- top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen
- Write app name - it has to be unique, it cannot be the same as this app
- Choose Region - I am in Europe
- Click "Create App"
- The page of your project opens. 
- Choose "settings" from the menu on the top of the page
- Go to section "Config Vars" and click button "Reveal Config Vars"
- Go to git pod and copy the content of "creds.json" file
- In the field for "KEY" enter "CREDS" - all capital letters
- Paste the content of "creds.json" and paste to field "VALUE" Click button "Add"
- Add another key "PORT" and value "8000"
- Go to section "Build packs" and click "Add build pack"
- in this new window - click Python and "Save changes"
- click "Add build pack" again
- in this new window - click Node.js and "Save changes"
- take care to have those apps in this order: Python first, Node.js second, drag and drop if needed
- Next go to "Deploy" in the menu bar on the top
- Go to section "deployment method", choose "GitHub"
- New section will appear "Connect to GitHub" - Search for the repository to connect to
- type the name of your repository and click "search"
- once Heroku finds your repository - click "connect"
- Scroll down to the section "Automatic Deploys"
- Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy
- Click "Deploy branch"

Once the program runs: you should see the message "the app was sussesfully deployed" 23. Click the button "View"
Forking the GitHub repository

By forking out of this repository you will be able to view and edit the code without affecting the original repository.

- Locate the GitHub repository. Link can be found here.
- Click the button in the top right-hand corner "Fork"
- This will take you to your own repository to a fork that is called the same as the original branch.

### Making a local clone

- Locate the GitHub repository. Link can be found [here](https://github.com/ahaffg/gag-cyc).
- Next to the green Gitpod button you will see a button "code" with an arrow pointing down
- You are given the option to open with GitHub desktop or download zip
- You can also copy https full link, go to git bash and write git clone and paste the full link

## Credits


### Media


## Acknowledgment
My fantastic mentor [Martina Terlević](https://www.linkedin.com/in/martinaterlevic/?originalSubdomain=de) for always being so helpful and flexible, as well as all round awesome human!