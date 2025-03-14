document.addEventListener("DOMContentLoaded", function () {
    async function generateLyrics() {
        const prompt = document.getElementById("prompt").value;

        if (!prompt) {
            alert("Please enter a theme!");
            return;
        }

        try {
            const response = await fetch("/generate_lyrics", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ keywords: prompt })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            document.getElementById("output").innerText = data.lyrics;
        } catch (error) {
            console.error("Error:", error);
            alert("An error occurred while generating lyrics.");
        }
    }

    document.getElementById("generate-btn").addEventListener("click", generateLyrics);
});
