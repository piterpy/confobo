# Confobo

Confobo is a Majordomo Telegram Bot aiming to help professional conference organizers to communicate with the coneference attendies.

## Features

### Schedule

* Allows to view the conference schedule for the selected conference day
* Allows user to select preferred talks and events
* Reminds of the preferred talks and events

### Feedback

* Allows to select the event/talk user is being attending
* Allows to vote (choice out of 5 stars) for the current event
* Allows to pass a question to the speaker/host of the current event
* Allows to send a message to the conference's helpdesk

### Venue

* Shows the conference venue address on the map
* Helps to find POIs near the venue

### Broadcast

* Allows to subscribe to a list of the broadcast channels
* Sends broadcast messages from the organizers for the subscribed channels

### Identification/Authentification

* Confobo uses a list of the one-time passwords to authenticate the conference attendies

### Administration

* Confobo uses a private git repo to load the current data (one-time passwords list, the current schedule, new broadcast messages, etc)

## Installation

**TBD**

## How to Contribute

**TBD**

## Development stages

### Stage 0
* Bot exists,
* Bot responds to commands:
	* /help - shows list of commands
	* /start - provides initial info about the bot
	* /stop - a stub for removing of the user from all subscription lists
	* /schedule [day] - a stub to view the conference schedule for the selected conference day
	* /vote streamId - a stub to vote (choice out of 5 stars) for the current event
	* /helpdesk - a stub to send a message to the conference's helpdesk

### Stage 1
* Bot responds to commands:
	* /start - creates keyboard
	* /stop - removes the user from all subscription lists
	* /schedule [day] - Allows to view the conference schedule for the selected conference day
	* /vote streamId [speakerId]- Allows to vote (choice out of 5 stars) for the current event
	* /helpdesk [roomId] - Allows to send a message to the conference's helpdesk
* Tests are written for key functionality
* DB scheme is created. It stores users, their preferred talks and events, votes, questions for each talk, questions to helpdesk

### Stage 2
* Confobo uses a list of the one-time passwords to authenticate the conference attendies
* User can select preferred talks and events (e.g. buttons under each talk: remind me, subscribe, ask a question, etc. )
* Bot reminds of the preferred talks and events
* Allows to select the event/talk user is being attending
* Allows to pass a question to the speaker/host of the current event
* Tests are added for key functionality

### Stage 3
* Shows the conference venue address on the map
* Helps to find POIs near the venue
* Tests are added for key functionality

## Authors

* [Serge Matveenko](https://github.com/lig)
* [Mikhail Krivushin](https://github.com/Deepwalker)
* [Julia Vikulina](https://github.com/JuliaVikulina)

## License

[MIT](LICENSE)
