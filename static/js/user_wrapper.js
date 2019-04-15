$("document").ready(function () {

    $.validator.addMethod("hasDigit", function (value, element) {
        return this.optional(element) || /(?=.*[0-9])/.test(value);
    }, "Пароль має повинен мати хоча б одну цифру");

    $.validator.addMethod("hasLetter", function (value, element) {
        return this.optional(element) || /(?=.*[a-zA-Z])/.test(value);
    }, "Пароль має повинен мати хоча б одну букву");

    // $("#signup-form").submit(function (e) {
    //     e.preventDefault();
    //     e.stopPropagation();
    // });

    $("#signup-form").validate({
        rules: {
            login: {
                required: true,
                minlength: 5,
            },
            email: {
                required: true,
                email: true,
            },
            password1: {
                required: true,
                minlength: 8,
                hasDigit: true,
                hasLetter: true,
            },
            password2: {
                required: true,
                equalTo: "#password_again",
            }
        },
        messages: {
            login: {
                required: "Обов'язкове поле",
                minlength: "Введіть щонайменш 5 символів",
            },
            email: {
                required: "Обов'язкове поле",
                email: "Необхідно формат адреси email",

            },
            password1: {
                required: "Обов'язкове поле",
                minlength: "Введіть щонайменш 8 символів",
            },
            password2: {
                required: "Обов'язкове поле",
                equalTo: "Паролі не співпадають",
            },
        }
    });


});


