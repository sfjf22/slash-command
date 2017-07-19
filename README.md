# Slack Assignment - A Slash Command

## Description
This task is to demo that when a Slash command is triggered, relevant data will be sent to an external URL in real-time and resulting response will be posted back to Slack. In our example, we will see that a message of a randomly generated number (representing a playing card) will be posted in the channel from which the command is triggered.

![Image of Channel](https://user-images.githubusercontent.com/30242361/28382180-26ec9422-6c72-11e7-981e-d55ead47fece.png)

## How it works
1. A new team is created in Slack: sfjf22
1. A new Slash command 'drawrandomcard' is created: https://sfjf22.slack.com/apps/A0F82E8CA-slash-commands
1. An external URL is required to properly configure the Slash command such that Slack knows where to send the request to. For the purpose of this demo, localtunnel is being used in my setup. (More about setting up localtunnel below).
![Image of Channel](https://user-images.githubusercontent.com/30242361/28382190-2f7dc250-6c72-11e7-8afe-7a1f2544deee.png)
1. The Python script **bin/draw_random_card.py** will be running in a remote host (exposed to the world by localtunnel) with this command: **$ python bin/draw_random_card.py**.
1. The script draw_random_card.py is meant to run as a service listening to port number 8080. When a request comes in, it will verify if it's for 'drawrandomcard'. It will then send a randomly generated number between 0 and 51 back to Slack.

## localtunnel
1. This demo is required to send message to an external URL for processing. Therefore, we need to expose a development env to the world such that Slack can communicate with. We would achieve this with localtunnel.
1. Details of localtunnel can be referenced here: https://localtunnel.github.io/www/
1. Installation can be done rather easily by **$ npm install -g localtunnel**
1. Start the server by **$ lt --port 8080**
1. After localtunnel starts, it will display the URL that the external clients can communicate with the local server as shown below. This URL should be copied to the 'Slash Commands' page - 'Integration Settings' section - URL field (as shown in the above screenshot) to complete the configuration of the Slash command.
```
$ lt --port 8080
your url is: https://zevgafhuqo.localtunnel.me
```
Then Slash command will be able to send the request to your local development server.
