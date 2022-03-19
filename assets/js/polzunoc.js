$(".polzunok-1").slider({
    min: 0,
    max: 3,
    value: 1,
    range: "min",
    animate: "fast",
});
var opt = $(".polzunok-1").data().uiSlider.options,
min = opt.min,
raz = opt.max - min;
for (var i = 0; i <= raz; i++) {
    $(".polzunok-1").append($('<b>'+(min++)+'</b>').css('left',(i/raz*100)+'%'));
}
