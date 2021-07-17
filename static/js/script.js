// Initialization from materializecss
$(document).ready(function(){
    $(".sidenav").sidenav();
    $(".dropdown-trigger").dropdown();
    $('.tooltipped').tooltip();
    $('select').formSelect();
  });



// Adding list item to the ingredients list in add_recipe page
$( "#ingredients .add-list-item" ).click(function(event) {
  let listItem = `<li class='collection-item'>
                    <div class='input-field'>
                      <input name='ingredients' type='text' maxlength='80' required>
                    </div>
                    <a class="btn-floating btn-small remove-list-item">
                    <i class="fas fa-minus"></i></a>
                  </li>`;
  $( this ).parent().before(listItem);
});
  
// Removing list item from the  ingredients list and method in add_recipe page
$( "#method, #ingredients").on("click", ".remove-list-item", function(event) {
  $( this ).parent().remove();
});

// Adding a list item to the method list
$( "#method .add-list-item" ).click(function(event) {
  let listItem =  `<li class='collection-item'>
                    <div class='input-field'>
                      <textarea name='methods' class='materialize-textarea' required></textarea>
                    </div>
                    <a class="btn-floating btn-small remove-list-item">
                    <i class="fas fa-minus"></i></a>
                  </li>`;
  $( this ).parent().before(listItem);
});