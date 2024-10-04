// Event listener for the search button
document.getElementById('searchBtn').addEventListener('click', function() {
    let city = document.getElementById('city').value;
    if (city === "") {
        alert("Please enter a city name");
        return;
    }
    
    // Your OpenWeatherMap API key
    let apiKey = "ec4c7da7168bc89007247ded1f50579b";  // Replace with your actual OpenWeatherMap API key
    let apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=imperial`;

    // Fetch the weather data
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            displayWeather(data);
        })
        .catch(error => {
            console.log("Error: " + error);
            alert("Could not retrieve weather data.");
        });
});

// Function to display the weather data
function displayWeather(data) {
    // Get elements to display
    let weatherDisplay = document.getElementById('weatherDisplay');
    let city = data.name;
    let temperature = data.main.temp;
    let description = data.weather[0].description;
    let humidity = data.main.humidity;
    let windSpeed = data.wind.speed;

    // Display the weather data with Fahrenheit and MPH units
    weatherDisplay.innerHTML = `
        <h2>${city}</h2>
        <p>Temperature: ${temperature}°F</p>
        <p>Description: ${description}</p>
        <p>Humidity: ${humidity}%</p>
        <p>Wind Speed: ${windSpeed} mph</p>
    `;
}
