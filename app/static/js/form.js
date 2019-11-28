(function ($) {

  'use strict';

  // ------------------------------------------------------- //
  // Add Form Fields Functionality
  // ------------------------------------------------------ //
  $(function () {
    var max_fields = 20; //maximum input boxes allowed
    var wrapper = $("#items.template-fields-field"); //Fields wrapper
    var add_button = $(".add_field_button"); //Add button ID
    var add_media = $(".add_media_button"); //Add media file
    var rnum = Math.floor(Math.random() * 64);


    var x = 1; //initlal text box count

    $(add_button).click(function (e) { //on add input button click
      e.preventDefault();
      if (x < max_fields) { //max input box allowed
        x++; //text box increment
        $(wrapper).append('<div class="form-group"><label for="template_field_">New Text ' + rnum + x + ':</label>' +
          '<input class="form-control" type="text" name="template-field_' + rnum + x + '" value="' + 'Typing New text here"/>' +
          '<button type="button" href="#" id="' + 'page-field-' + rnum + x + '" name="remove_field" class="btn btn-danger btn-shadow btn_remove remove_field">X</button></div>'); //add input box
      }
    });

    $(add_media).click(function (e) {
      e.preventDefault();
      if (x < max_fields) {
        x++; //media box increment
        $(wrapper).append('<div class="form-group"><label for="template_field_">Image:</label>' +
          '<input class="form-control" type="file" name="template-field_' + 'image" />' +
          '<button type="button" href="#" id="' + 'page-mediafile-' + rnum + x + '" name="remove_field" class="btn btn-danger btn-shadow btn_remove remove_field">X</button></div>')
      }
    });

    $(wrapper).on("click", ".remove_field", function (e) { //user click on remove field
      e.preventDefault(); $(this).parent('div').remove(); x--;
    })

  });

})(jQuery);