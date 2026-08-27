# Moving the app to tracker.thealtitudemindset.com

Do these in order. Steps 1 and 3 are yours; 2 and 4 are mine.

## 0. Export first — this is the one irreversible bit

`localStorage` is scoped to an origin. The moment the app lives on a new domain, it
is a **different origin**, and the history stored under `hazikdijoo-a11y.github.io`
will not follow it. Nothing is deleted, but the new address starts empty.

Open the app at the current address, hit **Export…**, and keep the `.json`. After the
move, open the new address and **Import…** it back.

## 1. Add the DNS record  (you)

At whoever manages DNS for `thealtitudemindset.com`:

    Type:   CNAME
    Name:   tracker
    Value:  hazikdijoo-a11y.github.io.
    TTL:    default

Not an A record, and not pointing at the repo name — the value is the github.io host.
Check it with:

    dig +short tracker.thealtitudemindset.com

## 2. Flip the repo to the custom domain  (me)

Once that resolves, I commit `CNAME` to the repo root and update `manifest.json`'s
`id` and paths for the new root. GitHub then issues a TLS certificate automatically,
which usually takes a few minutes and occasionally up to an hour.

Until the certificate is live the site may briefly show a warning. That is expected
and clears itself.

## 3. Verify in the repo's Pages settings  (you)

Settings → Pages should show the custom domain with a green tick and
**Enforce HTTPS** available. Tick it.

## 4. Build the Android package and publish assetlinks  (me, then you)

Order matters: the app must be built first, because the signing fingerprint does not
exist until it is. Then `.well-known/assetlinks.json` is filled in with that
fingerprint and pushed. If you use Play App Signing — you should — take the SHA-256
from the Play Console under Setup → App integrity, not from the local keystore.

Get that wrong and the app still runs, but with a browser URL bar across the top.
