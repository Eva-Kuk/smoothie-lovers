![althomepage](static/images/logo.png)

- [Overview](#overview)
- [User stories](#user-stories)
    - [New User Stories](#new-user-stories)
    - [Registered User Stories](#registrered-user-stories)
    - [Admin User Stories](#admin-user-stories)
    - [Site Owner Stories](#site-user-stories)
- [UX](#ux)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
- [Features](#features)
- [Technologies used](#technologies-used)
- [Resources](#resources)
- [Testing](#testing)
- [Code validity](#code-validity)
- [Version Control](#version-control)
- [Deployment](#deployment)
    - [Database Deployment](#database-deployment)
    - [Deployment Platform](#deployment-platform)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

## **Smoothie Lovers**

## Demo
---
![altamiresponsive](wireframes/readme/am-i-responsive.jpg)

- A live demo can be found [here](https://eva-kuk.github.io/smoothie-lovers/)
- A github repository can be found [here]()


## Overview
---
- This is my third of Milestone Project 3 which is part of the Code Isntitute's FullStack Software Development Diploma Course and the main requirements is to build a full-stack website allowing users to manage a common dataset.
This project demonstrates the skills and knowledge of using the HTML5, CSS3, JavaScript, Python,the Flask framework, Jinja templating language and MongoDB in Back-End development which I have learned recently on the course.
- This is a Smoothie Lovers page, which was designed for all people who love smoothies and would like to find and share their own recipes with others. This page can also be used as a storage for users recipes collection and allow users to freely share their recipes with each other and to have handy to see the recipes anytime they need it. 
- The aim of the project is to create a recipe book wepsite with smoothies recipes which will be divided into 4 different categories to choose from. Upon registration, the user will receive their own accounts and will be able to save, modify and store their own recipes as well as share them with other registered users. 
The website is created in a responsive design that is very handy to see recipes from mobile devices to tablets or larger screens.
- The website was created for educational purposes.

## User stories
---
## New User Stories
1. As a  new visitor, I want to navigate the site easily, so that I can find what I need effectively.
2. As a new visitor, I want to be able to access the website on a desktop and also mobile devices, so that I won't be restricted from which device I can access the site. 
3. As a new visitor, I want to be able to follow or connect with the owner of the website on social media, so that I can see what else they are doing.
4. As a new visitor, I want to be able to contact the website owner, so thatI will be able to share my feedback regarding the website, ask any questions or recommendations that I may have.
5. As a new visitor, I want to browse other users recipes on the website without register, so that I can decide if I want to have account on that website.
6. As a new visitor, I want to have Register/Log In functions, so that I can have my own profile where I can keep track on my own recipes.
7. As a new visitor, I want to be able to filter recipes by ingredient, so that I can find recipes using ingredients I like.
8. As a new visitor, I want to see if there is any good kitchen tools recomendations, so that I can get some ideas what I might need to make smoothies.
7. As a user, I want to easily understand the purpose of this site.

## Registered User Stories
9. As a registered user, I want to add my own recipes for safe keeping I can easily find them and share it with others users from the website.
10. As a registered user, I want to edit my recipes, so that I can change them as I want.
11. As a registered user, I want to be able to remove my own recipes, so that I can maintain what recipes I have in my profile.
12. As a registered user, I want to get a confirmation message before deleting the recipe, so I won't delete recipe by mistake.

## Admin User Stories
13. As an admin user, I want to be able to edit/remove any recipes, so that I can maintain a the website well at a high level.
14. As an admin user, I want to be able to add/edit/remove categories, so that I can adapt to the changing needs of the website users.

## Site Owner Stories
15. As a site owner, I want to be able to promote a kitchen tools, so that the users can choose for themself the best option on trhe market.

## UX
---
This website design will target people, who are smoothie lovers and would like to have place where they can explore new smoothies recipes, keep and share their own recipes with others.
The main goal of this project was to create an online smoothie recipe book that will contain a collection of different smothis descriptions added by registered users in four different categories and will allow registered users to register to have their own account, add, edit, delete recipes and share them with other users. The collection consists of the following categories:
1. **Stay Healthy** - This category will include all smoothies recipes that contain ingredients which support our immune system to strengthen our body to prevent from colds, as well as these one that contain anti-inflammatory ingredients to keep our intestines in good condition, also these turbo charging our bodies with minerals and vitamins called vitamin bombs, so if put it in one word all these recipes that will keep us in a good health.
2. **Stay Young** - This category will include all smoothies recipes  contain ingredients that are powerful sources of radical-fighting antioxidants, anti-aging, rehydration and detoxifying rich-ingredients to keep our skin looking younger and in good condition at all ages.
3. **Stay Fit** - This category will include all smoothies that contain ingredients for all weight-watchers who counting their calories and want to loose some weight, to speed up our metabolism, but also smoohites for those who workout at the gym, who want to build up their mussles and are looking for high-protein meals so for all who want to keep in shape.
4. **Stay Happy** - This category includes all our favorite cocktails, not necessarily containing super healthy ingredients, but we like them because they are delicious.

1. ## **Strategy**
My goal for this project is to create a website with smoothies recipes where users will be able to store their recipes and share them with other users.
It is intended to be used as an full-stack


### Project purpose:
- To create recipe online book, by 

### Site owner goals:
- Provide the contact form, so the users be able to get in touch with their queries
- Promote
- Provide
- Include
### Customer Goals:
- Easy to find 
- Easy to find links to social media accounts to follow the news about the website.
- Easy to find contact form for possible enquiries about profile or recipes.
2. ## **Scope**
To achieve user and owner’s goals, below are the minimum features to be included in this project. Also, CRUD functionality (Create, Read, Update, and Delete) is required for this project so these are implemented as a part of essential features.

CREATE— A function we can call when a new recipe is being added to the database. The user can supply the values for `category_name`, `recipe_name`, `ingredients_list`,`recipe_description `, `recipe_method` and `image_url`. The website admin has the capability to create new recipes category for selection.

READ — A function we call to retrive the information from database and display the results of all the recipes available currently in our database to read. All visitors to the website can browse all recipes without having to create an account.

UPDATE — A function we can call when information about a particular recipe needs to be changed. The user can edit the values for `recipe_name`, `ingredients_list`,`recipe_description `, `recipe_method` and `image_url`. After the function is called, the corresponding entry in the recipes database will contain the new fields provided. This option is only available to the creator of each recipe.The admin only can edit the values for `category_name`.

DELETE — A function we can call to remove a particular recipe from the catalog. After this function is called. This option is only available to the creator of the recipe


### Functional Requirements
- Mobile-first website that is responsive on all devices.

- Categories Stay Healthy, Stay Young, Stay Fit, Stay Happy) pages where users can choose recipes by the categories.
- Utencils page where users can see some kitchen tools halping to prepare and store smoothiea linked to the seller’s website.
- Login page where users can log in to the website.
- Logout function that users can log out the website.
- Profile page where users can see all their recipes and access to create, post, edit and delete recipes.
- Create Recipe page where users can create and post their recipes.
- Edit Recipe page where users can edit their recipes.
- Delete Recipe function that users can delete their recipes.
- Manage Category page and functions that only admin user (owner) can create, edit and delete categories.
- Search by a keyword(s) function that users can search for specific recipes
- 404 page that appears for invalid URL and takes users back to Home page of the website safely
- Register page where users can create an account to add, edit recipes.
- To have a straight forward interface, that allows the user to make choices about the content they wish to display.
- Provides users with pure UX.

### Content Requirements
- Much of the content on this site will be provided by users. 
- To ensure that the site immediately shows its purpose All the recipes are shown on Home page.

3. ## **Structure**


4. ## **Skeleton**
## Wireframe mockups:
**HOME/RECIPE PAGE**
![homepage](wireframes/home-page.png)

**COLLECTIONS PAGES:Stay Healthy/Stay Young/Stay Fit/ Stay Happy**

![collections](wireframes/collections-pages.png)

**UTENCILS PAGE**
![utensils](wireframes/utensils-page.png)

**SINGLE RECIPE PAGE**
![singlerecipe](wireframes/single-recipe-page.png)

**ADD/EDIT/DELETE EXISTING RECIPE PAGE**
![addeditdeleterecipe](wireframes/add-edit-delete-recipe-page.png)

**PROFILE PAGE**
![profile](wireframes/profile-page.png)

**MANAGE CATEGORIES PAGE**
![managecategories](wireframes/manage-categories-page.png)

**REGISTER PAGE**
![register](wireframes/register-page.png)

**LOGIN PAGE**
![singlerecipe](wireframes/login-page.png)

**CONTACT PAGE**
![contactpage](wireframes/contact-page.png)

**5. Surface**
**Colors**


 **Typography**


 **Images**

## Features
---
**Existing Features**

#### Navigation bar:


#### Footer:

#### Home Page:

#### About Page:

#### Attractions Page:

#### Contact Page

### HOME PAGE

 
 ### ABOUT PAGE


### ATTRACTIONS PAGE 


### CONTACT PAGE 


**Features Left to Implement when skills develop**

## Technologies Used


**1. Languages**

**2. Integrations**


  
**5. Other**

---
## Resources

---
## Testing
- Click [here](TESTING.md) for the full testing process.

Overview
- [Encountered Issues](TESTING.md#encounteredissues)
- [Code Validation](TESTING.md#code-validation)
- [Testing User stories](TESTING.md#testing-user-stories)
- [Testing Functionality](TESTING.md#testing-functionality)
- [Testing Compatibility](TESTING.md#testing-compatibility)
- [Testing Accessibility](TESTING.md#testing-accessibility)
- [Testing Performance](TESTING.md#testing-performance)
- [Further Testing](TESTING.md#further-testing)

---
## Code validity


## Version Control


## Deployment

### Database Deployment

### Deployment Platform

---

## Credits

**Media**

**Content**

**Code Snippets**

## Acknowledgments
