let selectedFile = null
let chartInstance = null

const fileInput = document.getElementById("file")
const dropZone = document.getElementById("drop-zone")
const fileName = document.getElementById("file-name")

// -----------------------------
// FILE CLICK (FIX DOUBLE OPEN)
// -----------------------------
dropZone.addEventListener("click", () => {
    fileInput.click()
})

// -----------------------------
// FILE SELECT
// -----------------------------
fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        selectedFile = fileInput.files[0]
        fileName.innerText = selectedFile.name
    }
})

// -----------------------------
// DRAG OVER
// -----------------------------
dropZone.addEventListener("dragover", (e) => {
    e.preventDefault()
    dropZone.classList.add("active")
})

// -----------------------------
// DRAG LEAVE
// -----------------------------
dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("active")
})

// -----------------------------
// DROP FILE
// -----------------------------
dropZone.addEventListener("drop", (e) => {
    e.preventDefault()
    dropZone.classList.remove("active")

    const file = e.dataTransfer.files[0]

    if (!file || file.type !== "application/pdf") {
        alert("Please upload a PDF file")
        return
    }

    selectedFile = file
    fileName.innerText = file.name
})

// -----------------------------
// GAUGE CHART
// -----------------------------
function drawGauge(score) {
    const ctx = document.getElementById("gaugeChart").getContext("2d")
    const percent = Math.round(score * 100)

    if (chartInstance) chartInstance.destroy()

    chartInstance = new Chart(ctx, {
        type: "doughnut",
        data: {
            datasets: [{
                data: [percent, 100 - percent],
                backgroundColor: [
                    percent > 70 ? "#00ff99" : percent > 40 ? "#ffcc00" : "#ff4444",
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

    document.getElementById("loader").style.display = "block"
    document.getElementById("result").innerHTML = ""

    const formData = new FormData()
    formData.append("file", selectedFile)

    try {
        const res = await fetch("http://localhost:8000/upload-resume", {
            method: "POST",
            body: formData
        })

        const data = await res.json()

        console.log("API:", data)

        document.getElementById("dashboard").style.display = "block"

        if (!data.recommendations || data.recommendations.length === 0) {
            document.getElementById("result").innerHTML = "<p>No matches found</p>"
            return
        }

        const bestScore = data.recommendations[0].final_score
        drawGauge(bestScore)

        let html = ""

        data.recommendations.forEach(job => {

            const skills = (job.matched_skills || [])
                .map(s => `<span class="skill-tag">${s}</span>`)
                .join("")

            html += `
                <div class="result-card">
                    <div style="display:flex; justify-content:space-between;">
                        <strong>Job ${job.job_id}</strong>
                        <span>${(job.final_score * 100).toFixed(0)}%</span>
                    </div>

                    <div style="font-size:0.85rem; margin:10px 0;">
                        TF-IDF: ${job.tfidf_score.toFixed(2)} |
                        BERT: ${job.bert_score.toFixed(2)} |
                        Skills: ${job.skill_score.toFixed(2)}
                    </div>

                    <div class="tag-container">${skills}</div>
                </div>
            `
        })

        document.getElementById("result").innerHTML = html

        document.getElementById("dashboard").scrollIntoView({ behavior: "smooth" })

    } catch (err) {
        console.error(err)
        alert("Backend error — make sure FastAPI is running")
    }

    document.getElementById("loader").style.display = "none"
}