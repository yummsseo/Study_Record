document.addEventListener("DOMContentLoaded", function () {
  const selectAll = document.getElementById("select_all");
  const checkboxes = document.querySelectorAll(".subject_checkbox");
  let allSelected = false;

  selectAll.addEventListener("click", function () {
    allSelected = !allSelected;
    checkboxes.forEach(function (checkbox) {
      checkbox.checked = allSelected;
    });
    selectAll.textContent = allSelected ? "전체 해제" : "전체 선택";
  });
});
