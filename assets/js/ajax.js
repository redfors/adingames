$(function () {

    $('.ajax').on('click', function () {
        typeUser = $('#type-user').val();
        if (typeUser == 'adventiser') {
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
                // location.reload();
                let url = "http://redfors.ru/";
                $(location).attr('href', url);
            },
            error: function () {
                console.log('Error');
            }
        });
    });
});