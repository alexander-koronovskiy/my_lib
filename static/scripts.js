$('.vertical-menu > a').click(function() {
    if ($(this).attr('id') === 'file') {
        var path = $(this).text();

        $.ajax({
            url: "/graphics",
            type: "get",
            data: {jsdata: path},
            success: function(response) {$("#main-content").html(response);}
        });
    }
});
