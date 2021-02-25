# Binaural-Relaxation

The idea is, to implement binaural beats, in python and make a Django based web application that could go on the route of being a SaaS later on.

### This is a tool meant for you to explore your consciousness, best if used in combination with existing practices like yoga, meditation or sadhana

## About Me :

I'm a developer and musician, the idea of tinkering around with brainwaves and using it to create real feelings and emotions inside a human being is something that I have been absolutely amazed by. Lesser known but it's worth giving a shot especially in the troubled times such as now, when mental health is becoming so volatile and people need something to relax, I have decided to re-implement the project I made in my final year in python and share it with all the amazing human beings around me.

## The Project :

I had named it Musical Healing Therapy.
The idea was simple, People should be given a choice to trick their brain in feeling a certain way.

The driving factor being this is that any stable frequency evokes a cortical response. The brain synchronises its dominant brainwave frequency with that of the external stimulus. This is called Brainwave Entrainment.

Putting it to practice using sinusoidal waveforms (sine waves), we find that:

A binaural beat is an auditory illusion perceived when two different pure-tone sine waves, both with frequencies lower than 1500 Hz, with less than a 40 Hz difference between them, are presented to a listener dichotically (one through each ear).

Thanks to the extremely capable and curious resarchers, we now have some basis to begin with. To use it, we have four states available to us :

**Delta - Binaural beats in the delta (1 to 4 Hz) range have been associated with deep sleep and relaxation.**

**Theta - Binaural beats in the theta (4 to 8 Hz) range are linked to REM sleep, reduced anxiety, relaxation, as well as meditative and creative states.**

**Alpha - Binaural beats in the alpha frequencies (8 to 13 Hz) are thought to encourage relaxation, promote positivity, and decrease anxiety.**

**Beta - Binaural beats in the lower beta frequencies (14 to 30 Hz) have been linked to increased concentration and alertness, problem solving, and improved memory.**

We will be using the following States in the project. ( The frequencies can change, Left 400Hz and Right 401Hz will give a 1Hz brainwave )

1 Hz - Delta | Lethargic
2 Hz - Delta | Deep Sleep
3 Hz - Delta | Dreamless
4 Hz - Theta | Drowsy
6 Hz - Theta | Fantasy
8 Hz - Alpha | Relaxed
12 Hz - Alpha | Conscious
16 Hz - Beta | Focused
24 Hz - Beta | Active

We will also mix it runtime with music so that it becomes fun and trust me it works subconsciously ;) ( we were amazed at the response in competitions. people were blown )

## Previous Technologies :

Java SE - For the generation of beats, mixing and .wav file generation ( Beat Generator Module )

Java Runnable Interface - To make multi threaded execution of mixing the beats ( Wav Mixer Module )

Java Servlets - For the server side code which responded with the exchange of generated output to the JSP Frontend.

Java Server Pages (JSP) - For the browser frontend

Javascript ES5 - To handle real time playback of the wav file in the browser.

Sadly I didn't have much idea of caching, redis so there was nothing of this sort in the project.

I wanted to re-invent the wheel since I was a student and this project meant all the real learning at the time to me.

It was done in 2017, I was quite immature realting to async programming, multi threaded execution and stuff. I hope to make it really optimized this time!

## New ( Proposed Technologies ) :

Python - For core generation/processing/mixing/output

Django - Backend ( RestFul / GraphQL ) ? need to implement and see if there's any significant differences

Vue.js - Web Frontend

Redis - Audio Cache ( For the Mixer, hoping to solve latency and delay issues I had by multi threaded loading, which practically made sure my third instance crashed xD )

PostgreSQL - Because I love it and we need a database :)

## Stuff that I would absolutely love to add :

- Mood recogniztion of the background music, I would love to have a program analyzing source track at runtime and selecting apt mood, so that I could use the creative commons library and mix relevant sounds on the fly. kind of an autotmation. maybe?

- Maybe a more intutive and awesome UI

- More backing tracks ( Artists, please! )

## Dependencies :

AccelBrainBeat 1.0.5 | Primary

EDIT: the following only work with python 3.6 i have 3.8 :/
PyAudioMixer 0.0.4
PyAudio 0.2.11
NumPy

I will save a lot of wheel reinvention using this and can truly focus on the backend!

also, I'm thinking to name it Enlightenment. what do you guys think?

## Implementation :

Core Python Modules :
Beat Generator - This will give us a audio output with a binaural beat for the specified number of seconds.
Audio Filter - Some sort of a limiter and de-noising (we want beat to be as clean as we can get).
Audio Enhancement - State specific eq tunings to give it that extra ah.
Cache Connector - This will serve as a cache on demand. ( python - redis manager kinda thingy )
Memory Flush - We would need this in case we need to reset the state for any reason.
Wav Mixer - This will serve as a multi channel mixer, will take the binaural beat, carrier waves, and audio input ( contributions of artists and my own compositions )
Wav Output - This will dump the mixer contents and render a .wav file which will be immediately sent to the client over websockets.

Django Modules:
User - profiles, auth, usage, history.
Set of static pages - INFO/ README/ SAFETY_GUIDELINES/ DISCLAIMER/
Blog - for the users to share their experiences
Playback - The main module which will handle the playback of beats
Custom Analytics - To keep track of how the files are being distributed and system performance across clients
Payment Integration? - let's see definitely not in the starting phase
ADS? - Never.

**As this is under development, installation, use and reviews will be added later, contributors would know how to install ;)**

## Contributions :

Programmers : PR's welcome.
Musicians : I welcome you to my discord, let's talk music and relaxation there
Artists : Artwork is welcome, please visit discord!

## I haven't thought of a monetary aspect to this yet, probably will go the SaaS route if enough people show interest, as it's a lot of work to actively maintain it for an audience, it's okay when people just try it out but active members mean a lot more scaling, let's build it first :D

## Discord :

**https://discord.gg/7aq3yqaPfr**

# Disclaimer :

With great possibilites, there always come unexpected turns that no one can forsee.
Though brainwave entrainment is generally considered safe and I really know what I'm trying to implement, things might not simply work for you.

The chance of causing any actual harm is too low, as you will not be listening to them for a long time, instead short focused bursts.
( I found this worked the safest, during testing of my final year project )

Secondly, I'm no medical professional, just a curious tinkerer. Please make sure you don't do anything ignorantly and always be safe as the motive is to help.

# Join me:

Wether you are just a curious user, an interested programmer or an annoyed medical professional ( just kidding haha ), Please feel free to reach out as I want to keep this dream alive and running, probably help thousands sooth themselves with the power of music, brainwaves and technology :D

feel free to contact me : akash@blabber.xyz
