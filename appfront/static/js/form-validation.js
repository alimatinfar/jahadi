'use strict';
$(document).ready(function () {
    $(function () {
        // [ Add phone validator ] start
        $.validator.addMethod(
            'phone_format',
            function (value, element) {
                return this.optional(element) || /^\(\d{3}\)[ ]\d{3}\-\d{4}$/.test(value);
            },
            'Invalid phone number.'
        );

        $.validator.addMethod(
            "regex",
            function (value, element, regexp) {
                return this.optional(element) || regexp.test(value);
            },
            "Please check your input."
        );

        // [ Initialize validation ] start
        $('#validation-form123').validate({
            ignore: '.ignore, .select2-input',
            focusInvalid: false,
            rules: {

                'username': {
                    required: true,
                },
                'password': {
                    required: true,
                    minlength: 8
                },
                'first_name': {
                    required: true,
                },
                'last_name': {
                    required: true,
                },
                'email': {
                    required: true,
                },
                'mobile': {
                    required: true,
                    regex: /^[0-9]{3}$/
                    // digits: true,
                    // minlength: 10,
                    // maxlength: 12
                },
                'national_code': {
                    required: true,
                    digits: true,
                    minlength: 10,
                    maxlength: 10
                },
                'date_birth': {
                    required: true,
                },
                'address': {
                    required: true,
                },

                'father_name': {
                    required: true,
                },

                // Checkbox groups  //
            },
            messages: {
                'username': {
                    required: "این فیلد را پر کنید!",
                },
                'password': {
                    required: "این فیلد را پر کنید!",
                    minlength: "حداقل 8 کاراکتر وارد کنید!"
                },
                'first_name': {
                    required: "این فیلد را پر کنید!",
                },
                'last_name': {
                    required: "این فیلد را پر کنید!",
                },
                'email': {
                    required: "این فیلد را پر کنید!",
                },
                'mobile': {
                    required: "این فیلد را پر کنید!",
                    regex: "REGEX"
                    // minlength: "حداقل 10 عدد وارد کنید!",
                    // maxlength: "کمتر از 12 عدد وارد کنید!",
                    // digits: "لطفا فقط عدد وارد بفرمایید!"
                },
                'national_code': {
                    required: "این فیلد را پر کنید!",
                    minlength: "۱۰ کاراکتر وارد کنید! کمتر است",
                    maxlength: "۱۰ کاراکتر وارد کنید! بیشتر است",
                    digits: "لطفا فقط عدد وارد بفرمایید!"
                },
                'date_birth': {
                    required: "این فیلد را پر کنید!",
                },
                'address': {
                    required: "این فیلد را پر کنید!",
                },
                'father_name': {
                    required: "این فیلد را پر کنید!",
                },

            },

            // Errors //

            errorPlacement: function errorPlacement(error, element) {
                var $parent = $(element).parents('.form-group');

                // Do not duplicate errors
                if ($parent.find('.jquery-validation-error').length) {
                    return;
                }

                $parent.append(
                    error.addClass('jquery-validation-error small form-text invalid-feedback')
                );
            },
            highlight: function (element) {
                var $el = $(element);
                var $parent = $el.parents('.form-group');

                $el.addClass('is-invalid');

                // Select2 and Tagsinput
                if ($el.hasClass('select2-hidden-accessible') || $el.attr('data-role') === 'tagsinput') {
                    $el.parent().addClass('is-invalid');
                }
            },
            unhighlight: function (element) {
                $(element).parents('.form-group').find('.is-invalid').removeClass('is-invalid');
            }
        });

    });
});
