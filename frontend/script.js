let selectedFile = null
let chartInstance = null

const fileInput = document.getElementById("file")
const dropZone = document.getElementById("drop-zone")
const fileName = document.getElementById("file-name")
const status = document.getElementById("statusText")

// -----------------------------
// FILE SELECT
// -----------------------------
dropZone.addEventListener("click", () => fileInput.click())

fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        selectedFile = fileInput.files[0]
        fileName.innerText = selectedFile.name
    }
})

// -----------------------------
// DRAG & DROP
// -----------------------------
dropZone.addEventListener("dragover", e => {
    e.preventDefault()
    dropZone.classList.add("active")
})

dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("active")
})

dropZone.addEventListener("drop", e => {
    e.preventDefault()
    dropZone.classList.remove("active")

    const file = e.dataTransfer.files[0]

    if (!file || file.type !== "application/pdf") {
        alert("Upload PDF only")
        return
    }

    selectedFile = file
    fileName.innerText = file.name
})

// -----------------------------
// GAUGE
// -----------------------------
function drawGauge(score) {

    const ctx = document.getElementById("gaugeChart").getContext("2d")

    if (chartInstance) chartInstance.destroy()

    const percent = Math.round(score)

    chartInstance = new Chart(ctx, {
        type: "doughnut",
        data: {
            datasets: [{
                data: [percent, 100 - percent],
                backgroundColor: [
                    percent > 70 ? "#00ff99" :
                    percent > 40 ? "#ffcc00" :
                    "#ff4444",
                    "rgba(255,255,255,0.1)"
                ],
                borderWidth: 0
            }]
        },
        options: {
            rotation: -90,
            circumference: 180,
            cutout: "85%",
            plugins: { legend: { display: false } }
        }
    })

    document.getElementById("scoreText").innerText = percent + "%"
}

// -----------------------------
// UPLOAD FUNCTION
// -----------------------------
async function upload() {

    if (!selectedFile) {
        alert("Please select a PDF resume first")
        return
    }

    const loader = document.getElementById("loader")
    const resultDiv = document.getElementById("result")
    const dashboard = document.getElementById("dashboard")

    loader.style.display = "block"
    resultDiv.innerHTML = ""

    // 🔥 LOADING STAGES
    status.innerText = "📄 Reading resume..."

    setTimeout(() => {
        status.innerText = "🧠 Extracting skills..."
    }, 700)

    setTimeout(() => {
        status.innerText = "⚡ Running AI model..."
    }, 1400)

    setTimeout(() => {
        status.innerText = "🔍 Matching jobs..."
    }, 2100)

    const formData = new FormData()
    formData.append("file", selectedFile)

    try {
        const res = await fetch("http://localhost:8000/upload-resume", {
            method: "POST",
            body: formData
        })

        const data = await res.json()

        status.innerText = "✅ Completed"

        setTimeout(() => {
            loader.style.display = "none"
            status.innerText = ""
        }, 800)

        dashboard.style.display = "block"

        drawGauge(data.overall_score)

        if (!data.recommendations || data.recommendations.length === 0) {
            resultDiv.innerHTML = "<p>No matches found</p>"
            return
        }

        let html = ""

        data.recommendations.forEach((job, index) => {

            const isTop = index === 0 ? "🔥 BEST MATCH" : ""

            const matched = (job.matched_skills || [])
                .map(s => `<span class="skill">${s}</span>`)
                .join("")

            const missing = (job.missing_skills || []).length > 0
                ? job.missing_skills.map(s => `<span class="skill missing">${s}</span>`).join("")
                : `<span style="color:#00ff99;">No major skill gaps 🎯</span>`
            
            html += `
                <div class="result-card">

                    <div style="display:flex; justify-content:space-between;">
                        <strong>${job.job_title}</strong>
                        <span>${(job.final_score * 100).toFixed(0)}%</span>
                    </div>

                    <div style="color:#00ff99; font-size:0.8rem;">
                        ${isTop}
                    </div>

                    <p>${job.job_description}</p>

                    <p style="font-size:0.8rem; color:#94a3b8;">
                        ${job.explanation}
                    </p>

                    <div>
                        <small>BERT: ${job.bert_score.toFixed(2)}</small>
                        <div class="bar"><div class="fill" style="width:${job.bert_score * 100}%"></div></div>

                        <small>TF-IDF: ${job.tfidf_score.toFixed(2)}</small>
                        <div class="bar yellow"><div class="fill" style="width:${job.tfidf_score * 100}%"></div></div>
                    </div>

                    <div><b>Matched:</b><br>${matched}</div>
                    <div><b>Missing:</b><br>${missing}</div>

                    <p style="color:#ffcc00;">${job.suggestion}</p>

                </div>
            `
        })

        resultDiv.innerHTML = html

        dashboard.scrollIntoView({ behavior: "smooth" })

    } catch (err) {
        console.error(err)
        loader.style.display = "none"
        status.innerText = ""
        alert("Backend error")
    }
}