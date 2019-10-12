# smart surveillance system for museum

<h3>Requirements</h3>
To run this you need a CUDA enabled GPU on your computer. (<b>Highly recommended</b>)<br>
It will also run on computers without GPU i.e. it will run on your processor giving you very poor FPS(around 0.6 to 1FPS), you can use AWS too.

<h3>About the project</h3>
One needs to collect lots of images of the artifacts or objects for training the model.
<br>
Once the training is done you can simply use the model by editing the 'options' in webcam files and labels of your object.
<br>

<h3>Features</h3>
<ul>
  <li>It continuously tracks the artifact.</li>
  <li>Alarm triggers when artifact goes missing from the feed.</li>
  <li>It marks the location where it was last seen.</li>
  <li>Captures the face from the feed of suspects.</li>
  <li>Alarm triggering when artifact is disturbed from original position.</li>
  <li>Multiple feed tracking(If artifact goes missing from feed 1 due to occlusion a false alarm won't be triggered since it looks for the artifact in the other feeds)</li>
</ul>

## How to run(Only for me)
```git
git clone
python35 .\setup.py build_ext --inplace
```
- Create a ```bin``` folder.
- Download yolov2 weight and tiny-yolo-v2 weight files from [here](https://pjreddie.com/darknet/yolov2/) and save inside ```bin```.

```git
python35 .\webcam-without-alarm-more-fps.py
```

<b>Watch the demonstration (<a href="https://youtu.be/I3j_2NcZQds">click me</a>)</b>

### Support Me
If you liked this Repository, then please leave a star on this repository. It motivates me to contribute more in such Open Source projects in the future.
### Happy Coding =)
