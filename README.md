# Flight Deals Finder

This application helps users find the best flight deals based on current prices stored in a Google Sheet and real-time
flight offers fetched from the Amadeus Flight Offers API. It notifies users via SMS using Twilio when a lower price than
the current lowest price is found.

## Setup

### Prerequisites

- Python 3.x installed
- `pip` package manager installed

### Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/flight-deals-finder.git 
cd flight-deals-finder
```

2. Install dependencies:

```
pip install -r requirements.txt
```

Replace `your_amadeus_api_key`, `your_amadeus_api_secret`, `your_twilio_account_sid`, `your_twilio_auth_token`, `your_twilio_phone_number`,
and `your_sheety_auth_token` with your actual credentials.

### Usage

Run the main script to search for cheapest flight deals for the next month and get notifications:

### Functionality

- **FlightSearch Class (`flight_search.py`)**:
    - Fetches authentication token from Amadeus API.
    - Retrieves airport IATA code for a given city.
    - Searches for the best flight deals within a specified date range and notifies if a lower price is found than the
      current lowest price stored in the Google Sheet.

- **DataManager Class (`data_manager.py`)**:
    - Manages data stored in the Google Sheet (using Sheety API).
    - Retrieves current lowest flight prices for various cities.

- **NotificationManager (`notification_manager.py`)**:
    - Sends SMS notifications using Twilio API.

