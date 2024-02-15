// 장바구니 로그인 확인 및 이동
// var cartConfirm = document.getElementById("cartConfirm");

// cartConfirm.addEventListener("click", function () {
//   var cartConfirmation = confirm("로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?");
//   if (cartConfirmation) {
//     window.location.href = "/user/login";
//   } else {
//     return;
//   }
// });

// 처음으로 아이콘과 db연동되어 찜 추가 삭제에 따라 아이콘이 다르게 보이지만 페이지 이동으로 들어간 경우 아이콘이 안바뀌는 코드였다
// 상세 제품 datasetid 얻어오기
const detailProduct = document.querySelector(".row");
const productId = detailProduct.dataset.id;

// 찜 버튼 로그인 확인 및 이동 - 로그인 안된 경우
var jjimConfirm = document.getElementById("jjimConfirm");

jjimConfirm.addEventListener("click", (e) => {
  // dataset id 잘 가져오는지 확인
  console.log(productId);

  if (!isAuthenticated) {
    var jjimConfirmation = confirm("로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?");

    if (jjimConfirmation) {
      // window.location.href = "/user/login";
      window.location.href = "/user/login/?next=" + window.location.pathname;
    } else {
      return;
    }
  } else {
    // 로그인을 했다면 찜 기능하도록 작성
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
          // 이미 찜한 상태이니까 체크된 아이콘 보여줘야함
          jjimConfirm.innerHTML = `찜<span class="material-symbols-outlined">
            heart_check
            </span>`;
          alert("찜 목록에 추가되었습니다.");
        } else {
          // 찜 해야하니까 기존 아이콘 보여줘야함
          jjimConfirm.innerHTML = `찜<span class="material-symbols-outlined">
            favorite
            </span>`;
          alert("찜 목록에서 제거되었습니다.");
        }
      })
      .catch((error) => console.log(error));
  }
});

function jjimCheck() {
  // 로그인했을때 찜 목록에 있는지 확인
  if (isAuthenticated) {
    fetch(`/coffee/jjim/check/${productId}/`)
      .then((response) => {
        if (!response.ok) {
          return new Error("에러");
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        if (data["is_jjimed"]) {
          // 이미 찜한 상태이니까 체크된 아이콘 보여줘야함
          jjimConfirm.innerHTML = `찜<span class="material-symbols-outlined">
                  heart_check
                  </span>`;
        } else {
          // 찜 해야하니까 기존 아이콘 보여줘야함
          jjimConfirm.innerHTML = `찜<span class="material-symbols-outlined">
                  favorite
                  </span>`;
        }
      })
      .catch((error) => console.log(error));
  } else {
    return;
  }
}
jjimCheck();
