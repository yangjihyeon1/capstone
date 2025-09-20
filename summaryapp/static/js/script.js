document.addEventListener("DOMContentLoaded", () => {
    const summarizeBtn = document.getElementById("summarize-btn");
    const summaryBox = document.getElementById("summary-box");

    summarizeBtn.addEventListener("click", () => {
        // TODO: Django API랑 연결 예정
        summaryBox.innerText = "👉 요약 결과가 여기에 표시됩니다 (임시 텍스트)";
    });

    const fileInput = document.getElementById("file-input");
    fileInput.addEventListener("change", (event) => {
        if (event.target.files.length > 0) {
            alert("파일 선택됨: " + event.target.files[0].name);
        }
    });
});
