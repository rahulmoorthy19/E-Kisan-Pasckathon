$(function() {
   $('.nav .list li').on('click', 'a', function () {
      $(this).parent().addClass('active').siblings().removeClass('active');
    });
});