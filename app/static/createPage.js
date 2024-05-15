function form_validation() {
    const limit = 6;

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation');

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            let totalChecked = $('.dropdown-menu input[type="checkbox"]:checked').length;

            // Check if form is valid using Bootstrap's custom validation
            if (!form.checkValidity() || totalChecked > limit || totalChecked > 0) {
                event.preventDefault();
                event.stopPropagation();
                
                // Show an error message if too many checkboxes are checked
                if (totalChecked > limit) {
                    alert('You can only select up to ' + limit + ' options across all dropdowns.');
                }
            }
            
            form.classList.add('was-validated');
        }, false);
    });
}

$(window).on("load", function() { 
});

$(document).ready(function() {
    $('#createQuestion').click(form_validation());
});