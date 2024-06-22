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

## The python scripts directory

This contains some random pieces of Python code!

- ...-worker-test.py: Run this with the correct exposed API URL to test out the functionality of your deployed worker quickly! You'll probably need the request module.
- htmlify.py: make a source.txt file with the content you want and it should convert all newlines to a \<br\> tag, and tab out things.