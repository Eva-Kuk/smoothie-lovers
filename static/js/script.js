// jQuerry Initialization from materializecss
$(document).ready(function(){
    $(".sidenav").sidenav();
    $(".dropdown-trigger").dropdown();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();

// jQuerry Initialization from materializecss
    $('#textarea1').val('New Text');
    M.textareaAutoResize($('#textarea1'));


// CREDIT: Code taken from Miniproject Materialize Validation
  validateMaterializeSelect();
  function validateMaterializeSelect() {
      let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
      let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
      if ($("select.validate").prop("required")) {
          $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
      }
      $(".select-wrapper input.select-dropdown").on("focusin", function () {
          $(this).parent(".select-wrapper").on("change", function () {
              if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                  $(this).children("input").css(classValid);
              }
          });
      }).on("click", function () {
          if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
              $(this).parent(".select-wrapper").children("input").css(classValid);
          } else {
              $(".select-wrapper input.select-dropdown").on("focusout", function () {
                  if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                      if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                          $(this).parent(".select-wrapper").children("input").css(classInvalid);
                      }
                  }
              });
          }
      });
  }
});

//CREDIT: from seanyoung247 https://github.com/seanyoung247/Plum
// Adding list item to the ingredients list in add_recipe page
$( "#ingredients .green-btn" ).click(function(e) {
  let listItem = `<li class='collection-item'>
                    <div class='input-field'>
                      <input name='ingredients' type='text' maxlength='120' required>
                    </div>
                    <a class="btn-floating btn-small red-btn">
                    <i class="fas fa-minus"></i></a>
                  </li>`;
  $( this ).parent().before(listItem);
});
  
// Removing list item from the  ingredients list and steps in add_recipe page
$( "#method, #ingredients").on("click", ".red-btn", function(e) {
  $( this ).parent().remove();
});

// Adding a list item to the method list
$( "#method .green-btn" ).click(function(e) {
  let listItem =  `<li class='collection-item'>
                    <div class='input-field'>
                    <input name='method' type='text' maxlength='120' required>
                    </div>
                    <a class="btn-floating btn-small red-btn">
                    <i class="fas fa-minus"></i></a>
                  </li>`;
  $( this ).parent().before(listItem);
});