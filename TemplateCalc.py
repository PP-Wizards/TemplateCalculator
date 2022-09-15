from datetime import timedelta
from itertools import accumulate
import math
from typing import List
import numpy as np
import slider

from calculators import BaseCalculator
from helpers.gamemodes import GameMode
from helpers.Score import Score

class BucketPerformanceCalculator(BaseCalculator.BaseCalculator):
    def __init__(self, beatmap_: slider.Beatmap, score_: Score, acc=None, mods_=None, tillerino=False, gameMode=GameMode.Standard):
        
        # Init your own variables here
        self.banana = True

        # At the end, init super
        super().__init__(beatmap_, score_, acc, mods_, tillerino, gameMode)

    # This HAS to exist and set self.pp at the end of its calculation.
    # You do not need to run it manually
    def calculate_pp(self):
        dt_enabled = int(self.score.mods) & 64 > 0
        hr_enabled = int(self.score.mods) & 1 > 0
        ez_enabled = int(self.score.mods) & 2 > 0
        hd_enabled = int(self.score.mods) & 16 > 0
        ht_enabled = int(self.score.mods) & 32 > 0

        cachedHitobjects = self.beatmap.hit_objects(double_time=dt_enabled, half_time=ht_enabled, hard_rock=hr_enabled, easy=ez_enabled)

        

        # iterate over all hitobjects, using the bucketsize
        for hitobject in cachedHitobjects:

            assert isinstance(hitobject, slider.beatmap.HitObject) # After this, intellisense will work
            # Depending on if you pass double_time, HR, ez etc. the hitobject here will already have its time + position updated
            # Its up to you to do the rest of the calculation, e.g. cirlesize, hitwindow etc.
            
            # You can then check if something is a Circle, slider or spinner by
            if isinstance(hitobject, slider.beatmap.Circle):
                pass
            
            pass

        self.pp = 69.420

        return self.pp
