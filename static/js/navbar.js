$(".fh5co-project").hover(
    function () {
      $(this).find(".like-icon").css("display", "block");
    },
    function () {
      $(this).find(".like-icon").css("display", "none");
    }
  );

  let jumlahSuka = 0;

  function suka(iconSuka) {
    jumlahSuka++;
    const elemenJumlahSuka =
      iconSuka.parentElement.querySelector(".like-count");
    elemenJumlahSuka.textContent = jumlahSuka;
  }



$(".fh5co-project").hover(
function () {
$(this).find(".like-icon").css("display", "block");
$(this).find(".download-icon").css("display", "block");
},
function () {
$(this).find(".like-icon").css("display", "none");
$(this).find(".download-icon").css("display", "none");
}
);
