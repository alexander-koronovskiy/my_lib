$('.vertical-menu > a').click(function() {
  if ($(this).attr('id') === 'name') {
    alert($(this).text())
  }
})
