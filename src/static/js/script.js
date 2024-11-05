async function promptFridge() {
    // get DOM references
    const spicy = document.getElementById("spicinessSlider").value;
    const model = document.getElementById("modelDropdown").value;
    const region = document.getElementById("regionDropdown").value;
    const responseArea = document.getElementById("responseArea");

    const button = document.getElementById("networkButton");
    if (button.innerHTML === "Offline" && model !== "local") {
        alert("Jeeves cannot take your order.\n\nHe's out cooking on the interwebs.");
        return;
    }

    // show loading spinner while waiting for response
    responseArea.innerHTML = '<div class="spinner"></div>';

    if (model === "local") {
        try {
            // send a request to the server
            const response = await fetch("/recipe", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({ spicy, model, region })
            });
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();
            responseArea.innerHTML = generateLocalRecipeHTML(data);
        } catch (error) {
            console.error("Error:", error);
            alert("Failed to get response from the server.");
        }
    } else {
        try {
            // send a request to the server
            const response = await fetch("/recipe", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({ spicy, model, region })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            jsonData = JSON.parse(data);

            if (!jsonData.dish_name) {
                throw new Error("Missing dish_name property in response");
            }
            if (!jsonData.ingredients) {
                throw new Error("Missing ingredients property in response");
            }
            if (!jsonData.steps) {
                throw new Error("Missing steps property in response");
            }

            // display the response
            responseArea.innerHTML = generateJeevesRecipeHTML(jsonData.dish_name, jsonData.ingredients, jsonData.steps);
        } catch (error) {
            console.error("Error:", error);
            alert("Failed to get response from the server.");
        }
    }
}

function generateLocalRecipeHTML(recipe) {
    return `
        <h2>Private Fridge Serves!</h2>
        <p>${recipe}</p>
    `;
}

function generateJeevesRecipeHTML(dishName, ingredients, steps) {
    return `
        <h2>Private Fridge serves: ${dishName}</h2>
        <h3>Ingredients:</h3>
        <ul>
            ${ingredients.map(ingredient => `<li>${ingredient}</li>`).join("")}
        </ul>
        <h3>Steps:</h3>
        <ol>
            ${steps.map(step => `<li>${step}</li>`).join("")}
        </ol>
    `;
}

function connection() {
    const button = document.getElementById("networkButton");
    const status = button.innerHTML;
    if (status === "Online") {
        button.innerHTML = "Offline";
        button.style.backgroundColor = "#FF8A8A";
    } else {
        button.innerHTML = "Online";
        button.style.backgroundColor = "#A0D683";
    }
}
