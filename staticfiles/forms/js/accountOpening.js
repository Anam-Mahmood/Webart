$(function () {
        $( document.getElementById(birth_date) ).datepicker({
            dateFormat : 'mm/dd/yy',
            changeMonth : true,
            changeYear : true,
            yearRange: '-110y:c+nn',
            maxDate: '-1d'
        });


         $( document.getElementById(passport_expiry) ).datepicker({
            dateFormat : 'mm/dd/yy',
            changeMonth : true,
            changeYear : true,
            yearRange: 'c+nn: +110y',
            minDate: '1d',
        });
 });

