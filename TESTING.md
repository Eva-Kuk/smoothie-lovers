# Testing

- [Encountered Issues](#ecountered-issues)
- [Code Validation](#code-validation)
- [Testing User stories](#testing-user-stories)
- [Testing Functionality](#testing-functionality)
- [Testing Compatibility](#testing-compatibility)
- [Testing Accessibility](#testing-accessibility)
- [Testing Performance](#testing-performance)
- [Further Testing](#further-testing)


## Encountered Issues
---

**Project Bugs And solutions**
---
While working on this project I encountered the following problems which I tried to solve in the following way:
1. **BUG:** Problem with connecting Flask to MongoDB Atlas, data didnt display in browser as expected but the GET 200 was received. 
In app.py wrong variable targeted instead of recipes the tasks was targeded.
- **SOLUTION:** Change the name from tasks to recipes

![connectin flask problem](wireframes/testing/connecting-flask-problem.png)
![connectin flask problem solved](wireframes/testing/connecting-flask-problem-solved.png)

2. **ISSUE:** While working on adding registration functionality on Register form the` Attribut Error: 'NoneType" object has no attribite 'encode'` was received 
- **SOLUTION:** Two typos was found `with` typo in base.html form line 80 and `password` typo in register.html line 22

![attribute none type error](wireframes/testing/attribute-none-type-error.png)
![base with typo](wireframes/testing/base-with-typo.jpg)
![register password typo](wireframes/testing/register-password-typo.png)

3. **ISSUE:**  While binding data to the recipe edit form I encountered a data binding problem with ingredients sections in edit_recipe form.
The data did not want to display at all or all listed ingredients were displayed in each line depense on how many ingredients were listed in the recipe.
- **SOLUTION:** The problem was in looping over `{{ ingredients }}` in `for ingredient in recipe.ingredients` and the value should be `{{ ingredient }}`

![ingredient edit recipe](wireframes/testing/ingredient-edit-recipe.jpg)

4. **ISSUE:**  While binding data to the recipe edit form I encountered a data binding problem with methods sections in edit_recipe form.
The data did not want to display or all.
- **SOLUTION:** The problem was the wrong property in for loop `{% for method in recipe.methods %}` should be `{% for method in recipe.method %}`

![method edit recipe](wireframes/testing/method-edit-recipe.jpg)

5. **BUG:** When trying to get a new account for the user, the register form stopped working and an error appeared `Incorrect Username and/or Password`
- **SOLUTION:** The problem was accidentally changed url_for address from `register` to `login`, which was restored to the correct one
![register wrong value](wireframes/testing/register-wrong-value.jpg)
 6. **ISSUE** Problem with the same height display of cards with different contents, cards break in the row and move to another making uneven amound in deferent row.
-**SOLUTION:** It took a good while to find the solution and trying different options, finnaly with a big help og tutor support it has been set using flexbox and some other style in the styles.css. The classes names were oryginaly set polish before commit were changed to english.

![equal card issue css before](wireframes/testing/equal-card-issue-css-before.png)

![equal card issue html](wireframes/testing/equal-card-issue-html.jpg)

![equal card issue css polish](wireframes/testing/equal-card-issue-css-polish.jpg)

![equal card issue css english](wireframes/testing/equal-card-issue-css-english.jpg)

![equal card issue](wireframes/testing/equal-card-issue.jpg)
## Code Validation
---

## Testing User stories
---

## Testing Functionality



### Checking for broken links
---


### Responsive Design
---


 **Encountered problems while testing the site on different devices**
 



## Testing Compatibility
---

---
## Testing Performance
---


## Testing Accessibility
----


- **Accessibility for mobile devices on LightHouse**


## Further Testing


### Overflow
