// 상세 및 찜 기능
const products = document.querySelectorAll(".product-card");

products.forEach((card) => {
  // 찜하기 버튼 기능
  const jjimButton = card.querySelector(".heart-icon");
  const heartIconPlus = card.querySelector(".heart-icon-plus");
  const heartIconMinus = card.querySelector(".heart-icon-minus");

  jjimButton.addEventListener("click", (e) => {
    const productId = card.dataset.id;

    fetch(`/coffee/jjim/${productId}/`)
      .then((response) => {
        if (!response.ok) {
          return new Error("에러");
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);

        if (data["is_jjimed"]) {
          heartIconPlus.style.display = "none";
          heartIconMinus.style.display = "block";
          alert("찜 목록에 추가되었습니다.");
        } else {
          heartIconMinus.style.display = "none";
          heartIconPlus.style.display = "block";
          alert("찜 목록에서 제거되었습니다.");
        }

        // 추천 전체 수
        document.querySelector(".like_jjimed").innerHTML = data["likes"];
      })
      .catch((error) => console.log(error));
  });

  // 찜 버튼을 제외한 영역 클릭 시 상세 페이지로 이동
  card.addEventListener("click", (e) => {
    if (!e.target.closest(".heart-icon")) {
      const id = e.currentTarget.dataset.id;
      let actionForm = document.querySelector("#actionForm");
      actionForm.action = "/coffee/" + id;
      actionForm.submit();
    }
  });
});
