document.addEventListener("DOMContentLoaded", function(){

    const stockInput = document.getElementById("stock-search");
    const stockList = document.getElementById("stock-list");
    const form = document.getElementById("stockForm");
    const resultsDiv = document.getElementById("results");
    
    stockInput.addEventListener("input", async function () {
        
        const query = stockInput.value.trim();

        if (query.length < 2) {
            stockList.innerHTML = "";
            return;
        }

        const response = await fetch(`/search?query=${query}`);

        const data = await response.json();

        stockList.innerHTML = "";

        data.forEach(stock => {

            const item = document.createElement("div");

            item.textContent = `${stock.symbol} - ${stock.name} (${stock.region})`;

            item.classList.add("stock-item");

            item.onclick = () => {

                stockInput.value = stock.symbol;

                stockList.innerHTML = "";
            };

            stockList.appendChild(item);

        });
    });

    form.addEventListener("submit", async function (event) {
        
        event.preventDefault();

        const ticker = stockInput.value.trim();
        if (!ticker) return;

        resultsDiv.innerHTML = "<p>Loading predictions...</p>";

        const response = await fetch("/predict", {

            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify({ tickers: [ticker] })

        });

        const data = await response.json();
        displayResults(data);
    });

    function displayResults(data) {
        
        resultsDiv.innerHTML = "";
        data.predictions.forEach(stock => {
           
            const stockDiv = document.createElement("div");

            if (stock.prediction !== null && stock.prediction !== undefined) {
                stockDiv.innerHTML = `<h2>${stock.ticker}: $${stock.prediction.toFixed(2)}</h2>`;
            } else {
                stockDiv.innerHTML = `<h2>${stock.ticker}: No data available</h2>`;
            }

            resultsDiv.appendChild(stockDiv);

        });
    }
});