
const button = document.getElementById("generate");
const promptBox = document.getElementById("prompt");
const result = document.getElementById("result");
const imageInput = document.getElementById("image");
const styleInput = document.getElementById("style");

button.addEventListener("click", async () => {
    const prompt = promptBox.value.trim();

    if (!prompt) {
        result.textContent = "Please describe your video first.";
        return;
    }

    button.disabled = true;
    button.textContent = "Preparing...";

    result.textContent =
        "DIBRA AI is preparing your video request. Actual video generation will be connected in the next development stage.";

    console.log({
        prompt: prompt,
        style: styleInput.value,
        image: imageInput.files[0]?.name || null
    });

    button.disabled = false;
    button.textContent = "Generate Video";
});
