$(function () {
let url = window.location.hostname;
    $('.ajax').on('click', function () {
        typeUser = $('#type-user').val();
        if (typeUser === 'adventiser') {
            data = {'typeUser': 'playgrounds'}
        } else {
            data = {'typeUser': 'adventiser'}
        }

        $.ajax({
            url: '/index/',
            method: 'GET',
            data: data,
            success: function () {
                $('.ajax').removeAttr('checked')
                let reload;

                if (url === 'localhost') {
                    reload = "http://localhost:8000/";
                } else {
                    reload = "http://redfors.ru/";
                }

                $(location).attr('href', reload);
            },
            error: function () {
                console.log('Error');
            }
        });
    });
});