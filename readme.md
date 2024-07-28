# Very random side projects!

## so what is this again?

Well, I assume you've read the title...
Anything here may work. Or not. I'm not sure.
The overall goal of this project does not exist!
This repository was made to consolidate all my experiments.

## The workers directory

So... this is a collection of code for the Cloudflare Workers platform.
Paste the code into the Workers web editor and it'll likely work!

- helloworld-worker.js: Self explanatory? This will make an API that returns... *hello world*. Try GET-ing from the endpoint!
- Whisper-worker.js: adapted from the template! Please deploy from the cloudflare template first to make sure the AI bindings are set up properly... (It won't work otherwise. Trust me, I've tried.) GET from it with the header "fileUrl" specified to a URL, and authKey to something you decided previously. Nothing too big for the free tier - it will exceed execution time limits. (And workers AI limits)
- randomredirect-worker.js: This will 302 redirect people to random URLs!
- finder-worker.js: This worker will find files in various storage services!
- create-3d-triangles-workers.py: This Python script can be used in tandem with a simple Python worker to return a random HTML page!

## The python scripts directory

This contains some random pieces of Python code!

- ...-worker-test.py: Run this with the correct exposed API URL to test out the functionality of your deployed worker quickly! You'll probably need the request module.
- htmlify.py: make a source.txt file with the content you want and it should convert all newlines to a \<br\> tag, and tab out things.
- trpg-helper.py: a file to help you out for TRPG sessions. Currently adapted to me and my friend's ruleset for a cleric.
- create-3d-trangles.py: a file that makes a txt file containing randomly colored, circularly-placed triangles and tetrahedrons for use in an a-frame environment.
- uploadfile.py: a file that provides a *very* simple Terminal-based UI to upload files to a S3 compatible storage or Backblaze B2 (Warning: dynamic imports!)
- webNowPlayingLogger.py: logs the playing song and artist to a file
- wnpLogRead.py: helps read said file
- gemini-api-multimodal.py: Lets you ask Gemini about images
- mc-serverdeploy.py: See website for guide on using this file.
- llm-comparison.py: Makes you chat to a random chatbot, and reveals who it was when the chat ends.
- mcs-deploy-config series: Helps you deploy a minecraft server. See site for more info.

You might want to look at the requirements in the file before running them.

## The musicLab directory

This is where songs I made for fun reside!
It was made in [Song Maker Plus](https://www.songmakerpl.us/), which allows anyone to create songs.
To listen to them, you could try playing the MIDI file directly, or see more [here](https://hackclub.jclink.link/documentations/music.html).

For more information, [visit my website!](https://hackclub.jclink.link/documentations)