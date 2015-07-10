# DjangoCMS Live-Draft Switch

Returns classic DjangoCMS-style live-draft switch to DjangoCMS.



## Wait, what?

With 3.1 release, DjangoCMS crew decided to replace the fabulous live-draft toggle / switch with 
plain dumb boring buttons.

![The change in 3.1](https://raw.githubusercontent.com/frnhr/djangocms-livedraftswitch/master/docs/img/djangocms_toolbar_dilema.jpg).

**I DON'T THINK SO!!!11number_one**

This is a quick'n'dirty response to that change. It's a JavaScript (jQuery, what else?!) hack 
that replaces those new buttons with something resembling the old toggle. 

![Toggle that this app provides](https://raw.githubusercontent.com/frnhr/djangocms-livedraftswitch/master/docs/img/the_new_toggle.jpg).



## Oh common, that's not really a problem!

Well, it's not, really. But IMHO it's a step in the wrong direction, be it a tiny one. 
And anyways, I find it simpler to quickly whip up this app together then to explain to my clients 
that nothing has really changed.
  
  
  
## But it's different then it was
 
It's improooooved :)

The differences are cosmetic. And I like to think this one is a bit better, because:

 - User can see what mode they are in, as well as what mode they will be switching to. This is not 
   a big deal, but it just might help a new user with their first edit ever.
 - Orange Draft indicator is more visible then the classic gray dot.
 
 
 
## Ok, how do I install this thing?

    pip install djangocms-livedraftswitch
    
Add before `cms` app:
    
    INSTALLED_APPS = (
        ...
        'djangocms-livedraftswitch',  # before cms app
        'cms',
        ...
    )

If you don't like Pypi, you can dump `djangocms-livedraftswitch` directory somewhere 
in `PYTHONPATH`.
 

## Compatibility?

Not tested much really...

Works with DjangoCMS 3.1.2 and Django 1.7.9.

Browsers: 

 * Google Chrome 64
 * Firefox 38
 * Safari 8.0.7  - animation is a bit jerky
 * IE 10+
 * IE 9 - no animation


## Is that a demo project there?
 
If you clone this repo, you'll get a full demo project. Not much of one, though, just a default 
DjangoCMS setup with this app installed. But this repo includes a SQLite database, so you can test
it right away. Login with `admin` and `admin`.

 