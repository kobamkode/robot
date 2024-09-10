# Robot
[TL;DR]
Me try to learn Computer Vision on Ragnarok Online.

======
My learning target is detect objects which are monsters, item drops, on danger character HP and SP. 
There are several videos on YouTube that teach how to do the similar things with YOLO model.

So I think I need to breakdown the tasks:
- First I need to train a new dataset by taking a lot of in-game screenshots.
- Use label-studio to labelling the images.
- Train the label-studio exported data into YOLO model.
- ...

## Dependencies
- X11
- scrot => 1.11.1 (support WID)
- wmctrl

## Usage
- `python -m venv venv` isolates project environment.
- `source venv/bin/activate` activates project environment.
- `make screenshot` starts screenshot on primary monitor (if you use multi monitors).
