# Right Ascension Conversion (optimisation trick)
A handy Python 3 utility that avoids having to continually calibrate a
telescope's RA axis for a given viewing location.

The code assumes the telescope's RA scale is calibrated by first setting
the reference RA co-ordinate, with the telescope pointing due-south, to the
value that would be present at the chosen location at midnight. When a
telescope is calibrated like this we just have to add the current time of day
(UTC) to the desired RA co-ordinate in order to obtain a value on the user's
calibrated (fixed) RA axis.

This 'trick' avoids the user from having to continually calibrate the RA scale
as the night progresses (because the sky is always moving). Adjusting the RA
scale, especially on entry-level telescopes, is often tricky in darkness.
Instead, with this 'trick', for any given viewing location the user simply
needs to calibrate the RA axis once, even during bight sunshine and without
the need of any visible celestial objects!

## Calibrating the telescope RA axis

## Running the utility.
Clone the repository and, from a suitable Python environment, run the
utility directly: -

    $ python -m venv ~/.venv/ra-converter
    $ source ~/.venv/ra-converter/bin/activate
    $ python ra-converter.py

---
