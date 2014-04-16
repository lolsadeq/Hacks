#!/bin/bash
# requires xsel and festival packages
# sends the selected area from X to the speech synth
xsel | festival --tts --pipe
