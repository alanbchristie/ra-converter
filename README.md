# Fixed-axis location of Right Ascension (RA) objects

[![lint](https://github.com/alanbchristie/ra-converter/actions/workflows/lint.yaml/badge.svg)](https://github.com/alanbchristie/ra-converter/actions/workflows/lint.yaml)
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/alanbchristie/ra-converter)
![GitHub](https://img.shields.io/github/license/alanbchristie/ra-converter)

A trick to rapidly locate celestial objects using a telescope and a fixed
[Right Ascension] (RA) axis.

These instructions and the accompanying Python 3 utility, allow you to avoid
having to continually calibrate a telescope's RA axis for a given viewing
location.

When a telescope is calibrated as described you just have to add an adjusted
viewing time to any desired RA co-ordinate in order to obtain a value
on the telescope's fixed (one-time-calibrated) RA axis. i.e. the axis does not
need to be altered while the viewer remains at a given location.

You will need: -

- A telescope with an [Equatorial mount]
- An app that uses a smartphone's compass to provide you with real-time
  RA co-ordinates (I use [SkyView] on an iPhone 11)
- A compass (or smartphone with a compass)

> This trick is based on the fact that although the celestial co-ordinates
  do change over time (due to [Axial precession]) the change is negligible.

An experimental real-time solution based on this technique that runs on the
Raspberry Pi Pico can be found in the following Raspberry Pi Pico repository: -

- https://github.com/alanbchristie/mp-pico-ra-calculator

## Background
I have my first telescope, but I'm just learning.

Even though I've just started, there is already one thing that I have found
particularly annoying on my telescope (a SkyWatcher [StarQuest-130P]) ...
It's the calibration of the RA axis.

It's an entry-level telescope, albeit a very good one, but the RA axis is a 
thin aluminium cover that wraps around the RA axis on the underside of the
mount, as shown below.

![My RA axis](images/IMG_4005.jpg)

Unfortunately turning the disk on this model turns out to be quite fiddly -
it's not on bearings, is not lubricated, and it often gets stuck!

I started to realise that this was going to turn out to be really annoying.

So I sat there, thinking ... _"Hold on! I've got to do this every night?
In the dark? Continuously?"_.

The trouble with the _"commonly accepted"_ method - i.e. "finding a star you
recognise" and then adjusting the ring after pointing your telescope at it
just seemed, to me, to be too complicated.

It relies on a number of actions: -

1. You need to know your stars, at least one, probably more including their
   RA values
2. You have to be able to see your chosen star. You might not be able to
   because of an obstruction (tree/house) or cloud cover
3. It needs to be dark - you can't see many stars when the Sun's shining!
4. You have to keep adjusting the RA ring as the night passes
   (because RA 0h 0m is moving relative to your location)

As a software engineer with a passion for automation I thought
"There has to be a better (faster) way".

So I got to thinking ... if you set the RA axis ring once (and you know what
time snf dsy it was when you did it) you can use any new time to calculate
an _offset_ that can be used against your fixed axis.

And this is the trick I employ here.

The result is a method where, for any given viewing location
(any longitude), you simply need to calibrate the telescope's RA axis
once, during the day when it's convenient. You just need to remember the date
you did it.

Then, given a new day and time of day and _target_ RA co-ordinate, you
calculate a co-ordinate *offset* using the difference and apply that to your
scale. You don't need to re-calibrate the RA ring as long as you observe
the sky from the same location (longitude).

## Calibrating the RA axis
**Step 1**

Set your telescope up at your viewing location. You will need to follow the
standard setup procedure - i.e. polar-align the mount.

**Step 2**

Turn the telescope on its RA axis so that it is pointing directly
**South** (or **North** if you're in the southern hemisphere). You can do this
using a standard compass (using **True North** rather than **Magnetic North**)
to locate any distant landmark or feature that is directly South (or North) of
your position.

In this picture the telescope has been removed for clarity.

![My RA axis](images/IMG_4007.jpg)

**Step 3**

Standing clear of any large metal objects (and the tripod) use your smartphone
app ([SkyView]) and turn to face South, making sure the app is displaying
real-time RA co-ordinates. SkyView is quite good for this
as it highlights the key compass points and the real-time co-ordinates
using a handy reticule.

Take a note of the current time and the RA co-ordinate of the southern compass
point (positioning the reticule as this screenshot illustrates)...

![My RA axis](images/IMG_4010.jpg)

In this example the current RA co-ordinate of the South compass point is
(approximately) `14h47m`.

**Step 4**

Adjust the RA co-ordinate to the value that would be found at the South 
compass point if it were midnight, i.e. subtract the current time from your
current reading.

In the above example the RA co-ordinate of South is `14h47m` so,
if the measurement was taken at 8AM subtract 8 hours
from the co-ordinate. In our example this would result in a
value of `6h47m`.

> That's the RA-co-ordinate of **South**, at your location, at midnight

Record this new RA co-ordinate (`6h47m`) and the current date
(i.e. `4th Jan` in my case).

The RA co-ordinate is essentially a constant ... if your telescope is
pointing directly South, from the same viewing location, it will be pointing
at `RA 6h47m` (in our example) at midnight on the same date every year
(`4th Jan` in my case).

Be aware that the RA coordinate will advance by approximately 4 minutes
every day (because the rotation of the earth actually only takes `23h56m`).
In a month the RA co-ordinate seen directly South will have advanced by
approximately 2 hours but after a year `RA 6h47m` will again be directly south
of your location. Leap years will compensate for the 4-minute drift.

> Remember, if you're in a location that observes Daylight Saving Time,
  you will want to adjust your telescope RA axis every time it changes
  (every 6 months or so), unless you want to or are able to use UTC
  as your "clock".

You could do all this at midnight and not do the maths, but at midnight
it's dark, cold and unnecessary.

**Step 5**

Now it's time to align your telescope's RA axis.

Using the midnight co-ordinate you calculated above, set your RA axis
to that value. In our case it's `6h47m`.

![My RA axis](images/IMG_4013.jpg)

That's it.

Now, to locate any celestial object, you just need to know the
object's RA co-ordinate and the current time of day (remembering to account
for Daylight Saving Time as mentioned earlier, if you need to).

## Locating objects using the fixed RA calibration
Let's say you want to locate **Capella** in the constellation of [Auriga].

You look up the object's co-ordinate and realise you need to turn your telescope
to `5h16m` (the RA co-ordinate of **Capella**). But, as your RA axis is
statically calibrated for _midnight_ on a particular day you can't use it
directly. Instead, you have to adjust the target co-ordinate using the
current time and the relative number of days that have elapsed since you last
calibrated the telescope. As the axis is calibrated in hours and minutes
this is (relatively) easy.

**An example for the day of calibration**

So, if it's 11PM on the day you calibrated the telescope just add `23h` to
your target co-ordinate (`5h16m`). This yields the new value `4h16m`, which
is the corrected value for your fixed RA axis.

Rotate your telescope to `4h16m` and, with the correct declination
(`+45 degrees 59 minutes`) you should be (roughly) centred on **Capella**.

**An example on days after calibration**

If it's 11PM and 10 days have elapsed since you calibrated the telescope add
`23h` plus `10 x 4` to the target co-ordinate, i.e. `5h16m plus 23h40m`,
which, for us, is `4h56m`.

> The number of days you add is relative to the date and month of calibration,
  i.e. the value's range is 0 to 364. Each year, on the calibration date,
  your daily offset returns to zero.

In summary - we have a handy trick - the rapid location of
objects using celestial coordinates without all the fiddly adjusting of the RA
axis - especially on cheaper telescopes!

## Running the software utility
You can of course, in your head, add the current time to your target
value. 

If you can do that in your head than all the better, because you won't need
to run this software. But, if you aren't good at mental arithmetic this
code will help you.

Clone the repository and, from a suitable Python environment, run the
utility directly: -

    $ python -m venv ~/.venv/ra-converter
    $ source ~/.venv/ra-converter/bin/activate
    $ python ra_converter.py

Enter the days that have elapsed since you calibrated the telescope and
RA co-ordinate of your object, and the code will use the current time
and present you with the _adjusted_ co-ordinate that you need to use
on your telescope.

---

[auriga]: https://en.wikipedia.org/wiki/Auriga_(constellation)#/media/File:Auriga_IAU.svg
[axial precession]: https://en.wikipedia.org/wiki/Axial_precession
[daylight saving time]: https://en.wikipedia.org/wiki/Daylight_saving_time
[equatorial mount]: https://en.wikipedia.org/wiki/Equatorial_mount
[right ascension]: https://en.wikipedia.org/wiki/Right_ascension
[skyview]: https://apps.apple.com/us/app/skyview/id404990064
[starquest-130p]: https://www.skyatnightmagazine.com/reviews/telescopes/sky-watcher-starquest-130p-newtonian-reflector-review/
