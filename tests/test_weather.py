from lib.weather import Weather
from unittest.mock import patch

def test_weather_instantiates():
    weather = Weather()

    assert isinstance(weather, Weather)

#2. @patch('random.choice')
def test_weather_sunny_returns_sunglasses(): #2. (mock_choice)
    weather = Weather()

    #2. mock_choice.return_value = 'sunny'

    #1. with patch("random.choice", return_value='sunny'):
    #1.    result = weather.lets_go_out()

    with patch('random.choice') as mock_choice:
        mock_choice.return_value = 'sunny'
        result = weather.lets_go_out()

        assert result == 'Its sunny, take sunglasses!'

@patch('random.choice')
def test_weather_rainy_returns_raincoat(mock_choice):
    weather = Weather()

    mock_choice.return_value = 'rainy'

    assert weather.lets_go_out() == 'Its rainy, take a raincoat!'