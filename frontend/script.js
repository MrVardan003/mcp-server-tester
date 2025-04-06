document.getElementById("test-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const installation_code = document.getElementById("installation_code").value;
  const api_key = document.getElementById("api_key").value;
  const config = document.getElementById("config").value;
  const valid_json_input = document.getElementById("valid_json_input").value;

  const payload = {
    installation_code,
    api_key,
    config,
    valid_json_input
  };

  try {
    const res = await fetch("http://localhost:5000/api/test", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    document.getElementById("output").textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    console.error(err);
    document.getElementById("output").textContent = "Error connecting to server.";
  }
});
