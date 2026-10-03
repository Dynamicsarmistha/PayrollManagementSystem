document.addEventListener("DOMContentLoaded", function () {

    console.log("Payroll Management System loaded successfully.");

    // --------------------------------------------------
    // Auto-hide Django messages
    // --------------------------------------------------
    const messages = document.querySelectorAll(".alert, .message");

    messages.forEach(function (message) {
        setTimeout(function () {
            message.style.transition = "opacity 0.5s ease";
            message.style.opacity = "0";

            setTimeout(function () {
                message.remove();
            }, 500);

        }, 3000);
    });


    // --------------------------------------------------
    // Delete confirmation
    // --------------------------------------------------
    const deleteForms = document.querySelectorAll(
        'form[action*="delete"]'
    );

    deleteForms.forEach(function (form) {

        form.addEventListener("submit", function (event) {

            const confirmed = confirm(
                "Are you sure you want to delete this record?"
            );

            if (!confirmed) {
                event.preventDefault();
            }

        });

    });


    // --------------------------------------------------
    // Payroll salary calculation
    // --------------------------------------------------
    const basicSalary = document.querySelector(
        '[name="basic_salary"]'
    );

    const allowances = document.querySelector(
        '[name="allowances"]'
    );

    const deductions = document.querySelector(
        '[name="deductions"]'
    );

    const netSalary = document.querySelector(
        '[name="net_salary"]'
    );


    function calculateNetSalary() {

        if (!basicSalary || !allowances || !deductions) {
            return;
        }

        const basic = parseFloat(basicSalary.value) || 0;
        const allowance = parseFloat(allowances.value) || 0;
        const deduction = parseFloat(deductions.value) || 0;

        const result = basic + allowance - deduction;

        if (netSalary) {
            netSalary.value = result.toFixed(2);
        }
    }


    if (basicSalary) {
        basicSalary.addEventListener(
            "input",
            calculateNetSalary
        );
    }

    if (allowances) {
        allowances.addEventListener(
            "input",
            calculateNetSalary
        );
    }

    if (deductions) {
        deductions.addEventListener(
            "input",
            calculateNetSalary
        );
    }


    // --------------------------------------------------
    // Prevent negative salary values
    // --------------------------------------------------
    [basicSalary, allowances, deductions].forEach(function (field) {

        if (field) {

            field.addEventListener("input", function () {

                if (parseFloat(field.value) < 0) {
                    field.value = 0;
                }

                calculateNetSalary();

            });

        }

    });

});