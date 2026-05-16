$("#id_image").on("change", function() {
    let file = this.files[0];
    if (file) {
      let reader = new FileReader();
      reader.onload = function(e) {
        $("#profile-preview").attr("src", e.target.result);
      };
      reader.readAsDataURL(file);
    }
});
