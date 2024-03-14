Simple Tautulli Script for sending a Youtube Link from last added Movie to Discord.


Requirements:

Get your Youtube API: [https://developers.google.com/youtube/v3/getting-started?hl=de]

Create A Discord Channel with a webhook access: [https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks]









1.
Add a folder in your Tautulli installation folder named "scripts" and place the file there.

2.
In Tautulli Settings go to Notification Agents,
Add A new Tautulli Script Notification Agent

3.
Enable the file


![Script_config](https://github.com/sudoWalker/tautulli-youtubelink-Discord-messenger/assets/5301174/09c6b90f-ea34-4578-9132-437adaaa96d9)




4.
Add a Trigger


![script_Recently_added](https://github.com/sudoWalker/tautulli-youtubelink-Discord-messenger/assets/5301174/5fbb457e-d619-44ee-bdf0-dc15e00644dd)




5.
In the Arguments Tab add this to recently Addded: {title} {year}


![script_arguments](https://github.com/sudoWalker/tautulli-youtubelink-Discord-messenger/assets/5301174/c1892ed1-511d-4f2b-a6e6-d552e68ac054)
