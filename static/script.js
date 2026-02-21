async function analyzeMessage() {
    const message = document.getElementById("message").value;

    const response = await fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    if (data.error) {
        document.getElementById("result").innerHTML = data.error;
        return;
    }

    let color = "#28a745"; // green safe

    if (data.final_score >= 70) {
        color = "#dc3545"; // red high risk
    } 
    else if (data.final_score >= 30) {
        color = "#ffc107"; // yellow suspicious
    }

    document.getElementById("result").innerHTML = `
        <h2 style="color:${color}">${data.risk_level}</h2>
        <h3>Fraud Type: ${data.fraud_type}</h3>

        <div style="background:#ddd;border-radius:20px;width:100%;height:25px;margin:15px 0;">
            <div style="
                width:${data.final_score}%;
                background:${color};
                height:100%;
                border-radius:20px;
                text-align:center;
                color:white;
                font-weight:bold;">
                ${data.final_score.toFixed(1)}%
            </div>
        </div>

        <p><b>Why flagged:</b> ${data.explanation}</p>
        <p><b>Detected Suspicious Words:</b> 
            ${data.keywords.map(word => `<span style="color:red;font-weight:bold;">${word}</span>`).join(", ")}
        </p>

        <h4>Safety Advice:</h4>
        <ul>
            ${data.tips.map(t => `<li>${t}</li>`).join("")}
        </ul>
    `;
}