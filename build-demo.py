#!/usr/bin/env python3
"""Regenerate demo.html from index.html. Run after any change to the app."""
import json

src = open('index.html').read()

names = ['Fajr','Hydrate 3L','Gym','Ground school','Sim practice','Charts review',
         'Read 20pp','Journal','Meditate','Plan tomorrow','Steps 8k','Sleep by 11',
         'No sugar','Stretch','Walk outdoors','Vitamins']
habits = [{'id': 'h%d' % (i+1), 'name': n, 'createdOn': '2026-08-01'}
          for i, n in enumerate(names)]
log = {h['id']: {} for h in habits}

def fill(day, frac):
    for i, h in enumerate(habits):
        if ((i * 7 + day * 13) % 100) / 100.0 < frac:
            log[h['id']][str(day)] = 'done'

for day, frac in [(1,.95),(2,.95),(3,.95),(4,.6),(5,.95),(8,.95),(9,.35),(10,.95),
                  (11,.95),(12,.6),(14,.95),(15,.95),(16,.95),(18,.9)]:
    fill(day, frac)

demo = {'version': 1, 'habits': habits,
        'months': {'2026-08': {'flightDays': [6, 7, 17], 'log': log}},
        'lastExport': '2026-08-17'}

out = src

key = "  var STORAGE_KEY = 'course-tracker.v1';"
assert out.count(key) == 1
# DEMO_SEED must be assigned before loadState() runs, hence here and not
# beside freshState(): declarations hoist, var assignments do not.
out = out.replace(key,
    "  var STORAGE_KEY = 'course-tracker.demo.v1';\n"
    "  var DEMO_SEED = " + json.dumps(demo, separators=(',', ':')) + ";")

fresh = """  function freshState() {
    return {
      version: 1,
      habits: [{ id: newId(), name: 'Daily Study', createdOn: todayKey() }],
      months: {},
      lastExport: null
    };
  }"""
assert out.count(fresh) == 1
out = out.replace(fresh, """  function freshState() {
    return JSON.parse(JSON.stringify(DEMO_SEED));
  }""")

sw = "  if ('serviceWorker' in navigator && location.protocol.startsWith('http')) {"
assert out.count(sw) == 1
out = out.replace(sw, "  if (false) {   /* demo never registers a worker */")

out = out.replace("<title>Course Tracker by The Altitude Mindset</title>",
                  "<title>Course Tracker — live demo</title>")
out = out.replace('<link rel="manifest" href="./manifest.json">', '')
out = out.replace('<p class="byline">by The Altitude Mindset</p>',
                  '<p class="byline">by The Altitude Mindset &middot; demo</p>')

open('demo.html', 'w').write(out)
print('demo.html regenerated:', len(out), 'bytes')
