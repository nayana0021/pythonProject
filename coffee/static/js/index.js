// 페이지 이동
// document.querySelector(".pagination").addEventListener("click", (e) => {
//   e.preventDefault();

//   let href = e.target.getAttribute("href");

//   document.querySelector("#page").value = href;

//   document.querySelector("#actionForm").submit();
// });

// 상세 페이지 이동
// const products = document.querySelectorAll(".product-card");

// products.forEach((card) => {
//   card.addEventListener("click", (e) => {
//     const id = e.currentTarget.dataset.id;

//     let actionForm = document.querySelector("#actionForm");
//     actionForm.action = "/coffee/" + id;
//     actionForm.submit();
//   });
// });

// 상세 및 찜 기능
const products = document.querySelectorAll(".product-card");

products.forEach((card) => {
  // 찜하기 버튼 기능
  const jjimButton = card.querySelector(".heart-icon");
  const heartIconPlus = card.querySelector(".heart-icon-plus");
  const heartIconMinus = card.querySelector(".heart-icon-minus");

  jjimButton.addEventListener("click", (e) => {
    // 로그인 확인 코드
    // 컨펌창 확인 누르면 로그인 페이지로 이동
    if (!isAuthenticated) {
      var jjimConfirmation = confirm("로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?");
      if (jjimConfirmation) {
        // window.location.href = "/user/login";
        window.location.href = "/user/login/?next=" + window.location.pathname;
      } else {
        return;
      }
    } else {
      // 로그인되어있다면 찜 기능
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
    }
  });

  card.addEventListener("click", (e) => {
    if (!e.target.closest(".heart-icon")) {
      const id = e.currentTarget.dataset.id;
      let actionForm = document.querySelector("#actionForm");
      actionForm.action = "/coffee/" + id;
      actionForm.submit();
    }
  });
});

// // 실패
// // 메인페이지에서 찜들 확인하기
// function jjimsCheck() {
//   // 로그인했을때 찜 목록에 있는지 확인
//   if (isAuthenticated) {
//     fetch(`/coffee/index/`)
//       .then((response) => {
//         if (!response.ok) {
//           return new Error("에러");
//         }
//         return response.json();
//       })
//       .then((data) => {
//         console.log(data);
//         if (data["is_jjimed"]) {
//           heartIconPlus.style.display = "none";
//           heartIconMinus.style.display = "block";
//         } else {
//           heartIconMinus.style.display = "none";
//           heartIconPlus.style.display = "block";
//         }
//       })
//       .catch((error) => console.log(error));
//   } else {
//     return;
//   }
// }
// jjimsCheck();

// 찜 버튼 로그인확인
// var loginConfirm = document.getElementById("loginConfirmButton");

// loginConfirm.addEventListener("click", function () {
//   var userConfirmation = confirm("로그인이 필요합니다. 로그인 페이지로 이동하시겠습니까?");
//   if (userConfirmation) {
//     // 여기에 로그인 페이지로 이동하는 코드를 추가할 수 있습니다.
//     // 예: window.location.href = '로그인 페이지 URL';
//     window.location.href = "/user/login/";
//   } else {
//     // 사용자가 취소한 경우에 수행할 동작을 추가할 수 있습니다.
//     return;
//   }
// });
