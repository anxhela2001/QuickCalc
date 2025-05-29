function evaluateExpression() {
  const expression = document.getElementById("expression").value.trim();
  const resultDiv = document.getElementById("result");

  const validExprPattern = /^[0-9+\-*/().\s]+$/;

  if (!expression) {
    resultDiv.innerHTML = `<p style="color:red;">Please enter an expression.</p>`;
    return;
  }

  if (!validExprPattern.test(expression)) {
    resultDiv.innerHTML = `<p style="color:red;">Error: Only numbers and valid math operators (+, -, *, /, (), .) are allowed.</p>`;
    return;
  }

  const payload = { expression };

  fetch("http://localhost:5000/evaluate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        resultDiv.innerHTML = `<p style="color:red;">Error: ${data.error}</p>`;
      } else {
        resultDiv.innerHTML = `<p>Result: ${data.result}</p>`;
      }
    })
    .catch((error) => {
      resultDiv.innerHTML = `<p style="color:red;">Error: ${error}</p>`;
    });
}

window.addEventListener("DOMContentLoaded", () => {
  const inputField = document.getElementById("expression");
  const resultDiv = document.getElementById("result");

  inputField.addEventListener("input", () => {
    resultDiv.innerHTML = "";
  });
});
