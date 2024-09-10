# ROBot

Me try to learn [ computer vision | object detection ] on Ragnarok game.

===

I'm so excited to learn how to make a model that can detect objects in a game! 
I want it to be able to spot monsters, item drops, and dangerous situations where a character's HP is almost 0%.

So I think I need to breakdown the tasks:
- Train a new dataset by taking a lot of in-game screenshots.
- Use labeling application to help labeling the images.
- Train the labeled data into a model.
- ...

## Dependencies
- X11
- scrot => 1.11.1 (support WID)
- wmctrl

## Usage
- `python -m venv venv` isolates project environment.
- `source venv/bin/activate` activates project environment.
- `make screenshot` starts screenshot on primary monitor (if you use multi monitors).
