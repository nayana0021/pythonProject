const csrfTokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
const csrfToken = csrfTokenInput ? csrfTokenInput.value : null;

const jjims = document.querySelectorAll(".product-item");

jjims.forEach((deleteButton) => {
  const dButton = deleteButton.querySelector(".deleteButton");

  dButton.addEventListener("click", (e) => {
    e.preventDefault();
    const jjimId = deleteButton.dataset.id;

    fetch(`/coffee/jjim/delete/${jjimId}`, {
      method: "delete",
      headers: {
        "X-CSRFToken": csrfToken,
      },
    })
      .then((response) => {
        console.log("Response Status Code:", response.status);
        console.log("Response Status Text:", response.statusText);
        console.log(jjimId);
        if (!response.ok) {
          return new Error("삭제실패");
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);

        if (data["is_jjimed"]) {
          var jjimElements = document.querySelectorAll(".product-item");
          jjimElements.forEach((jjimElement) => {
            if (jjimElement.dataset.id === jjimId) {
              jjimElement.remove();
            }
          });
          alert("찜 목록에서 제거되었습니다.");
        } else {
          console.error("찜 삭제 실패");
        }
      })
      .catch((error) => console.log(error));
  });
});
